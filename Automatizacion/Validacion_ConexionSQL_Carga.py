# Importar librerias
from cryptography.fernet import Fernet
import pyodbc
import pandas as pd
import configC

# Generar una clave de encriptación
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encriptar las credenciales
encrypted_username = cipher_suite.encrypt(configC.username.encode())
encrypted_password = cipher_suite.encrypt(configC.password.encode())


# Desencriptar las credenciales
decrypted_username = cipher_suite.decrypt(encrypted_username).decode('utf-8')
decrypted_password = cipher_suite.decrypt(encrypted_password).decode('utf-8')


# Conectar a la base de datos
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER=megapp.database.windows.net,1433;'
    'DATABASE=Moneyball_DB;'
    f'UID={decrypted_username};'
    f'PWD={decrypted_password};'
)

# Cargar el archivo CSV
df = pd.read_csv('Team.csv')

# Validar y limpiar los datos
df['id'] = df['id'].astype(int)
df['full_name'] = df['full_name'].astype(str).str[:50]
df['abbreviation'] = df['abbreviation'].astype(str).str[:3]
df['nickname'] = df['nickname'].astype(str).str[:50]
df['city'] = df['city'].astype(str).str[:50]
df['state'] = df['state'].astype(str).str[:50]
df['year_founded'] = df['year_founded'].astype(int)
df = df[(df['year_founded'] >= 1890) & (df['year_founded'] <= 2025)]

# Crear la tabla Team
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE Team (
    id INT PRIMARY KEY NOT NULL,
    full_name NVARCHAR(50) NOT NULL,
    abbreviation NVARCHAR(3) NOT NULL,
    nickname NVARCHAR(50),
    city NVARCHAR(50),
    state NVARCHAR(50),
    year_founded INT CHECK (year_founded >= 1890 AND year_founded <= 2025)
)
''')
conn.commit()

# Insertar los datos en la tabla
for index, row in df.iterrows():
    cursor.execute('''
    INSERT INTO Team (id, full_name, abbreviation, nickname, city, state, year_founded)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', row['id'], row['full_name'], row['abbreviation'], row['nickname'], row['city'], row['state'], row['year_founded'])
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()