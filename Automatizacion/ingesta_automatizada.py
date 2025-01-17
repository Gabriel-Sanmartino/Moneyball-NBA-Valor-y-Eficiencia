from cryptography.fernet import Fernet
import pyodbc
import pandas as pd
import Automatizacion.configC as configC

print('Estableciendo conexion con Moneyball_DB')

# Generar una clave de encriptación
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encriptar las credenciales
encrypted_username = cipher_suite.encrypt(configC.username.encode())
encrypted_password = cipher_suite.encrypt(configC.password.encode())
encrypted_server_name = cipher_suite.encrypt(configC.server_name.encode())

# Desencriptar las credenciales
decrypted_username = cipher_suite.decrypt(encrypted_username).decode('utf-8')
decrypted_password = cipher_suite.decrypt(encrypted_password).decode('utf-8')
decrypted_server_name = cipher_suite.decrypt(encrypted_server_name).decode('utf-8')

# Conectar a la base de datos
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER=megapp.database.windows.net,1433;'
    'DATABASE=Moneyball_DB;'
    f'UID={decrypted_username};'
    f'PWD={decrypted_password};'
)

print("Conexión exitosa.")

print('Cargando archivos a comparar con Moneyball_DB')

# Cargar el archivo CSV
df = pd.read_csv('TeamAct.csv')

print('Verificar y eliminar filas con valores nulos')

# Verificar y eliminar filas con valores nulos
if df.isnull().values.any():
    print("Eliminando filas con valores nulos.")
    df = df.dropna()
else:
    print("No se encontraron valores nulos en el archivo CSV.")

print('Buscando duplicados...')

# Eliminar filas duplicadas en el CSV
df = df.drop_duplicates(subset='id')
print("Filas duplicadas eliminadas del archivo CSV.")

# Validar tipos de datos
df['id'] = df['id'].astype(int)
df['full_name'] = df['full_name'].astype(str).str[:50]
df['abbreviation'] = df['abbreviation'].astype(str).str[:3]
df['nickname'] = df['nickname'].astype(str).str[:50]
df['city'] = df['city'].astype(str).str[:50]
df['state'] = df['state'].astype(str).str[:50]
df['year_founded'] = df['year_founded'].astype(int)

print("Datos validados.")

print('Comparando base de datos con origen en busqueda de nuevos registros...')

# Obtener los IDs existentes en la base de datos
cursor = conn.cursor()
cursor.execute("SELECT id FROM Team")
existing_ids = [row[0] for row in cursor.fetchall()]

# Filtrar los nuevos IDs
new_data = df[~df['id'].isin(existing_ids)]

print("Se encontraron nuevos registros para insertar.")

print('Cargando nuevos registros...')

# Insertar los nuevos datos en la tabla con verificación de valores dentro de rangos
for index, row in new_data.iterrows():
    if row['year_founded'] < 1890 or row['year_founded'] > 2025:
        print(f"year_founded_error_valor_fuera_de_rango en la fila {index + 1}. Se insertará el valor mínimo 1890.")
        row['year_founded'] = 1890
    try:
        cursor.execute('''
        INSERT INTO Team (id, full_name, abbreviation, nickname, city, state, year_founded)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', row['id'], row['full_name'], row['abbreviation'], row['nickname'], row['city'], row['state'], row['year_founded'])
    except pyodbc.IntegrityError as e:
        print(f"Error al insertar el registro con id {row['id']}: {e}")
conn.commit()

print("Moneyball_DB actualizada exitosamente.")

# Cerrar la conexión
cursor.close()
conn.close()

print("Conexión a la base de datos cerrada.")