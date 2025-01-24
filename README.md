<h1 align="center">✨MONEYBALL NBA VALOR Y EFICIENCIA✨</h1>

![Consultora](https://github.com/user-attachments/assets/0c7091bc-4b1c-406a-8313-dfd8da292b46)

## Descripcion del proyecto📄:

- El proyecto se centra en el análisis del desempeño de jugadores de la NBA
- En el contexto en que los dueños de equipos buscan maximizar el valor de sus inversiones en jugadores, 
- garantizando que los salarios pagados estén alineados con su rendimiento
- Esto resulta crítico en un mercado competitivo donde las decisiones salariales pueden influir directamente en el éxito deportivo y financiero.

## Tecnologias Aplicadas⚙:

- Azure - Base de Datos
- Trello - Gestion de Proyectos
- VSC
- SQL
- Python (Pandas)
- Power BI


## Etapas del Proyecto📑:

Para este proyecto, se trabajó con la metodología SCRUM en 2 Sprints.
Esta forma de trabajo se basa en la colaboración, la flexibilidad y la entrega incremental de valor. 
Al estar dividido en ciclos cortos  (sprints), permite adaptarse rápidamente a las necesidades del cliente, priorizar tareas y entregar resultados funcionales de forma constante.

### **Sprint 1:**

### 1)Planificacion del Proyecto: 
- se ha utilizado Trello como herramienta para planificar tareas, asignar los responsables de cada una de ellas e
- indicar fechas y dependencias

### 2)Obtencion de los datasets:
- Se ha trabajado con los datasets asignados de Kaggle
- Ademas se ha investigado y conseguido informacion externa para complementar y enriquecer el analisis
- Se ha realizado un analisis exploratorio inicial de todos los datasets

### 3)Definicion de las formas de trabajo:
- Implementacion de Git/Github como herramienta de trabajo
- Creacion de usuarios, accesos
- Testeo preliminar de los accesos y las formas de trabajar
- Creacion de ramas (una por cada miembro del equipo)

### 4)Tareas de ETL
- Carga de los documentos en formato .csv para su revision
- Filtrado de datos
- Validacion de formato de los datos, cambios y ajustes cuando fuera necesario
- Relleno de datos faltantes
- Aplicacion de mejores practicas

### 5)Diseño de la BD
- Diseño del modelo relacional
![ModeloRelacional](https://github.com/user-attachments/assets/c5b3bb47-c824-4052-90e1-c8ad58edb2b9)
- Creacion del servidor en Microsoft Azure
- Creacion de la base de datos en el servidor
- Otorgamiento de permisos seguros para la conexión remota/local y generación de credenciales de acceso a los usuarios
- Verificacion de accesos
- Conexion a la base de datos mediante SGBD, SQL Server Management Studio
- Creacion de entidades (Tablas)
- Carga de datos

### 6)Automatizacion
- Diseño del diagrama de flujo de ingesta de datos
![Proceso de ingestaB drawio](https://github.com/user-attachments/assets/ea099aee-c1a7-439e-860c-6dc7d32c6361)
- Desarrollo de scripts para ETL e ingesta automatizada de datos
- Programacion de ejecucion automatica de los scripts
- Verificacion del correcto funcionamiento de la actualizacion programada de la base de datos
- Demo de la ingesta dirigido al PO (video)

### 7)Preparacion de la presentacion del Sprint 1 para el PO
- Definicion de los puntos a incluir
- Estructuracion de la presentacion en PowerPoint
- Asignacion de segmentos de la presentacion a cada miembro del equipo
- Definicion de una paleta de colores profesional para aplicar
- Asegurarse de incluir soportes visuales para reflejar y representar el proyecto para el cliente (e.g. demo del proceso de automatizacion)

### **Sprint 2:**

### 1)Planificacion del sprint 2
- Definicion de los obejtivos a alcanzar en el sprint
- Definicion de tareas a realizar (¿Como alcanzar los objetivos?)
- Clasificacion de las tareas segun la urgencia de su concrecion
- Establecimiento de deadlines
- Asignacion de responsables

### 2)Exploracion de herramientas y utiles de diseño
- Se ha analizado el uso de figma como herramienta de diseño
- Se exploraron funcionalidades y recursos de Canva
- Se ha explorado el uso de herramientas de AI para la extraccion de paletas de colores
- Se ha explorado el uso de herramientas de AI para generacion de logos

### 3)Creacion del archivo .pbix
- Conexion a base de datos
- Importacion de las entidades necesarias
- Validacion de los datos en Power Query
- Carga de los datos a Power BI
- Generacion del modelo (Validacion de relaciones)

### 4)Diseño MockUp
- Seleccion de logo de cliente (oklahoma city thunder)
- Extraccion de paleta de colores
- Maquetacion/Storytelling

### 5)Diseño del Dashboard en Power BI
- Generacion de medidas bases
- Generacion de medidas avanzadas (variaciones nominales, variaciones porcentuales, funciones de inteligencia de tiempo)
- Desarrollo de storytelling, estructura: marcos, navegacion segmentadores
- Generacion de elementos visuales nativos
- Exploracion de graficas no nativas de Power Bi
- Implementacion de graficos externos
- Incorporacion de funciones automatizadas (email)

### 6)Preparacion de la presentacion del Sprint 2 para el PO
- Definicion la estructura de la presentacion
- Asignacion de responsables a cada instancia
- Simulacion previa


## Estructura del repositorio:
El repositorio Moneyball-NBA-Valor-y-Eficiencia se ha organizado en dos secciones principales para facilitar la gestión y el seguimiento del proyecto:

###	Dashboard:
- Contiene el archivo Power BI (.pbix) que visualiza los resultados finales del proyecto para oklahoma city thunder.
- Incluye la documentación detallada sobre la creación y configuración del tablero.


###	Recursos y desarrollo:
- Agrupa todos los datos utilizados en el proyecto, tanto los proporcionados por oklahoma city thunder como los obtenidos de fuentes externas.
- Contiene los scripts y códigos fuente organizados por sprint (Sprint 1 y Sprint 2) para un mejor seguimiento del desarrollo.
- Incluye cualquier otro recurso adicional utilizado durante el proyecto.


## Glosario de documentos:

- Automatizacion (carpeta): Contiene toda la documentacion referente al proceso de ingesta de datos automatizado
- Dataset Final (carpeta): Guarda todos los archivos utilizados en el proceso final de carga de datos a "Moneyball_DB"
- Dataset (Carpeta): Contiene todos los archivos utilizados en el proceso de obtencion y consolidacion de la informacion necesaria para el desarrollo del proyecto
- ETL.ipynb: Jupiter notebook con el codigo utilizado para la realizacion del procceso de extraccion, transformacion y carga de los datos
- ETLSalarios.ipynb: Contiene el proceso de ETL aplicado a los datos de salarios obtenidos de fuentes externas
- PrimeraExploracion.ipynb: El codigo contenido permite la navegacion, observacio y exploracion del contenido de los datasets
- Validacion_ConexionSQL_Carga.py: Situado en la carpeta "Automatizacion". Contiene el codigo que permite validar los datos, conectarse a la base de datos y cargar los registros
- Inesta_Automatizada.py: Proceso de extraccion, transformacion y carga de nuevos datos. La ejecucion de este sript se genera de forma automatica a traves del programador de tareas de Windows
  



  

  


