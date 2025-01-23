# MONEYBALL NBA VALOR Y EFICIENCIA

## Integrantes del equipo: 
- Crowder, Maria - Project Manager 
- Loaiza, Angelica - Data Engineer
- Mendoza, Erick - Data Architect
- Sanmartino, Gabriel - Data Scientist

## Descripcion del proyecto:

- El proyecto se centra en el análisis del desempeño de jugadores de la NBA
- En el contexto en que los dueños de equipos buscan maximizar el valor de sus inversiones en jugadores, 
- garantizando que los salarios pagados estén alineados con su rendimiento
- Esto resulta crítico en un mercado competitivo donde las decisiones salariales pueden influir directamente en el éxito deportivo y financiero.

## Tecnologias Aplicadas:

- Azure - Base de Datos
- Trello - Gestion de Proyectos
- VSC
- SQL
- Python (Pandas)
- Power BI


## Etapas del Proyecto:

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
- Creacion del servidor en Microsoft Azure
- Creacion de la base de datos en el servidor
- Otorgamiento de permisos seguros para la conexión remota/local y generación de credenciales de acceso a los usuarios
- Verificacion de accesos
- Conexion a la base de datos mediante SGBD, SQL Server Management Studio
- Creacion de entidades (Tablas)
- Carga de datos

### 6)Automatizacion
- Diseño del diagrama de flujo de ingesta de datos
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

### 8)Preparacion de la presentacion del Sprint 2 para el PO
- Definicion de tareas y puntos a incluir
- Generacion de la estructura de presentacion 

### **Sprint 2:**

### 1)Planificacion del sprint 2
- Creacion del archivo.pbix
- Importacion de datos
- Limpieza y transformacion de datos
- Almacenamiento seguro de datos
- Creacion de medidas, columnas y relaciones en PowerBI
- Elaboracion del dashboard, generacion de elementos visuales (Storytelling)
- Incorporacion de filtros y segmentaciones, pruebas de calidad

### )


## Estructura del repositorio:
El repositorio Moneyball-NBA-Valor-y-Eficiencia se ha organizado en dos secciones principales para facilitar la gestión y el seguimiento del proyecto:

###	Dashboard:
- Contiene el archivo Power BI (.pbix) que visualiza los resultados finales del proyecto para oklahoma city thunder.
- Incluye la documentación detallada sobre la creación y configuración del tablero.


###	Recursos y desarrollo:
- Agrupa todos los datos utilizados en el proyecto, tanto los proporcionados por oklahoma city thunder como los obtenidos de fuentes externas.
- Contiene los scripts y códigos fuente organizados por sprint (Sprint 1 y Sprint 2) para un mejor seguimiento del desarrollo.
- Incluye cualquier otro recurso adicional utilizado durante el proyecto.


  

  


