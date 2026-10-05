# Proyecto Final: Pipeline ETL de Gestión Hospitalaria

Asignatura: Extracción, Transformación y Carga de Datos (ETL)
Programa: Técnico Profesional en Depuración y Procesamiento de Datos para Inteligencia Artificial
Caso de Estudio: Gestión Hospitalaria (*Hospital Management*)
 
 DESCRIPCIÓN

Pipeline ETL desarrollado en Python para la extracción, transformación y carga de información relacionada con la gestión hospitalaria.

El proyecto utiliza un conjunto de datos de gestión hospitalaria obtenido desde Kaggle y procesa diferentes entidades relacionadas con el funcionamiento de un hospital, incluyendo pacientes, médicos, citas, tratamientos y facturación.

El pipeline implementa las tres etapas principales de un proceso ETL:

Extract: Obtención de los datos desde el dataset de Kaggle.
Transform: Limpieza, depuración, estandarización y validación de los datos.
Load: Carga de la información procesada en una base de datos SQLite.

El objetivo principal es convertir datos provenientes de una fuente externa en información estructurada, limpia y preparada para su almacenamiento y posterior análisis.


Fuente de Datos

El conjunto de datos utilizado en el proyecto corresponde a:

Hospital Management Dataset

Fuente:Kaggle

Dataset utilizado:

`kanakbaghel/hospital-management-dataset`

El conjunto de datos contiene información relacionada con diferentes procesos de gestión hospitalaria.


Entidades Procesadas

El pipeline trabaja con cinco conjuntos de datos principales:

| Entidad      | Registros |
| ------------ | --------: |
| Patients     |        50 |
| Doctors      |        10 |
| Appointments |       200 |
| Treatments   |       200 |
| Billing      |       200 |
|   Total      |      660  |

Estas entidades permiten representar diferentes aspectos del funcionamiento de una institución hospitalaria.

Patients

Contiene la información correspondiente a los pacientes registrados en el sistema.

 Doctors

Contiene información relacionada con los médicos disponibles en la institución.

 Appointments

Registra las citas médicas realizadas entre pacientes y médicos.

Treatments

Contiene información sobre los tratamientos asociados a los pacientes.

 Billing

Registra la información relacionada con los procesos de facturación.


 Estructura del Repositorio

ETL_Proyecto-HospitalMs/
│
├── data/
│   └── hospital.db
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

### Descripción de los archivos

| Archivo            | Descripción                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| `main.py`          | Orquesta y ejecuta el pipeline ETL completo.                             |
| `src/extract.py`   | Se encarga de obtener los datos desde Kaggle.                            |
| `src/transform.py` | Realiza la limpieza y transformación de los datos.                       |
| `src/load.py`      | Carga los datos procesados en SQLite.                                    |
| `requirements.txt` | Contiene las dependencias necesarias para ejecutar el proyecto.          |
| `.gitignore`       | Define los archivos y carpetas que no deben ser enviados al repositorio. |
| `data/hospital.db` | Base de datos SQLite generada como resultado del proceso ETL.            |



## Requisitos Previos

Para ejecutar el proyecto se requiere tener instalado:

Python 3
pip
Git
Visual Studio Code(recomendado)

También es necesario contar con acceso a Internet para obtener el dataset desde Kaggle.



Instalación

 1. Clonar el repositorio


git clone https://github.com/mailethpolo103-del/ETL_Proyecto-HospitalMs.git


Ingresar a la carpeta:


cd ETL_Proyecto-HospitalMs


2. Crear un entorno virtual

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

En Windows:

python -m venv venv


Activar el entorno:

.\venv\Scripts\activate




 3. Instalar las dependencias

Ejecutar:


pip install -r requirements.txt


 Ejecución del Pipeline

El proceso completo se ejecuta desde el archivo `main.py`.

Desde la raíz del proyecto ejecutar:

python main.py


El programa ejecutará las tres etapas del proceso:

Extract
   ↓
Transform
   ↓
Load


Al finalizar, los datos procesados quedan almacenados en una base de datos SQLite.



Etapa 1: Extract

La primera etapa corresponde a la extracción de datos.

El módulo:


src/extract.py


se encarga de obtener el conjunto de datos desde Kaggle.

El proyecto utiliza el dataset:


kanakbaghel/hospital-management-dataset

Durante esta etapa se identifican y cargan las diferentes tablas que hacen parte del conjunto de datos:

 Patients
 Doctors
 Appointments
 Treatments
 Billing

Los datos extraídos son enviados posteriormente a la etapa de transformación.


 Etapa 2: Transform

La segunda etapa corresponde a la transformación y limpieza de los datos.

Esta etapa se encuentra implementada en:


src/transform.py

Durante el proceso se realizan diferentes operaciones de preparación de los datos.

 Limpieza de datos

Se realizan procesos orientados a mejorar la calidad de la información, incluyendo:

 Eliminación de registros duplicados.
 Limpieza de valores de texto.
 Eliminación de espacios innecesarios.
 Estandarización de información textual.
 Identificación de valores nulos.
 Preparación de los tipos de datos.
 Validación de la información antes de realizar la carga.

El objetivo de esta etapa es garantizar que los datos que llegan a la base de datos tengan una estructura consistente.


 Control de Calidad de los Datos

Como parte de la transformación se realiza una revisión de la calidad de los datos.

Entre los aspectos revisados se encuentran:

Valores nulos

Se verifica la existencia de valores faltantes dentro de las diferentes tablas.

Después del proceso de transformación y carga realizado por el proyecto, las tablas procesadas no presentan valores nulos.

 Registros duplicados

Se realiza una revisión de registros repetidos para evitar almacenar información duplicada.

 Limpieza de texto

Los campos de texto son procesados para eliminar inconsistencias como espacios innecesarios y mejorar la uniformidad de la información.



 Etapa 3: Load

La tercera etapa corresponde a la carga de los datos transformados.

Esta etapa se encuentra implementada en:


src/load.py


Los datos procesados son almacenados utilizando SQLite.

La base de datos generada es:

data/hospital.db

Dentro de la base de datos se almacenan las cinco entidades principales:

patients
doctors
appointments
treatments
billing


 Base de Datos

El proyecto utiliza:

SQLite

La elección de SQLite permite disponer de una base de datos relacional ligera, portable y fácil de utilizar para el almacenamiento de los datos procesados.

La base de datos generada permite posteriormente realizar consultas y análisis sobre la información hospitalaria.


 Idempotencia

El pipeline está diseñado para que la carga de los datos pueda repetirse sin generar acumulaciones innecesarias de información.

Durante la etapa de carga, las tablas son reemplazadas por la información procesada nuevamente, evitando que una nueva ejecución agregue copias de los mismos registros.

Esto permite ejecutar nuevamente:


python main.py


sin generar duplicaciones progresivas en la base de datos.


 Resultados del Proceso

Después de ejecutar el pipeline se obtiene la siguiente distribución de información:

| Tabla          | Registros |
| -------------- | --------: |
| `patients`     |        50 |
| `doctors`      |        10 |
| `appointments` |       200 |
| `treatments`   |       200 |
| `billing`      |       200 |
|      Total     |   660 |

El resultado final corresponde a una base de datos SQLite estructurada y preparada para consultas y análisis posteriores.


 Tecnologías Utilizadas

El proyecto fue desarrollado utilizando las siguientes tecnologías:

Python
Pandas
NumPy
SQLite
Kaggle
Git
GitHub
Visual Studio Code


Flujo General del Proyecto

El proceso completo puede resumirse de la siguiente manera:


                    DATASET KAGGLE
                          │
                          ▼
                     EXTRACT
                          │
                          ▼
              ┌─────────────────────┐
              │   Datos originales  │
              └──────────┬──────────┘
                         │
                         ▼
                     TRANSFORM
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       Limpieza de texto     Eliminación de
                             duplicados
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                Validación de datos
                         │
                         ▼
                       LOAD
                         │
                         ▼
                 ┌───────────────┐
                 │ SQLite        │
                 │ hospital.db   │
                 └───────────────┘


 Características Principales

El proyecto cuenta con las siguientes características:

* Arquitectura ETL modular.
* Separación de las etapas Extract, Transform y Load.
* Obtención de datos desde Kaggle.
* Limpieza y transformación mediante Python.
* Uso de Pandas para el procesamiento de datos.
* Control de registros duplicados.
* Control de valores nulos.
* Limpieza de información textual.
* Almacenamiento en SQLite.
* Ejecución mediante un archivo principal `main.py`.
* Carga reproducible de los datos.
* Organización modular del código.


 Reproducibilidad

Para reproducir el proceso en otro equipo se deben seguir los siguientes pasos:


git clone https://github.com/mailethpolo103-del/ETL_Proyecto-HospitalMs.git


cd ETL_Proyecto-HospitalMs


Crear el entorno virtual:

python -m venv venv


Activarlo en Windows:


.\venv\Scripts\activate


Instalar las dependencias:


pip install -r requirements.txt


Finalmente ejecutar:


python main.py


El pipeline realizará nuevamente las etapas de extracción, transformación y carga.


 Control de Versiones

El proyecto utiliza Git para el control de versiones y GitHub como plataforma de almacenamiento del código fuente.

Repositorio:

ETL_Proyecto-HospitalMs

El archivo `.gitignore` permite evitar que archivos generados o de gran tamaño sean incluidos innecesariamente en el repositorio.


 Conclusiones

El desarrollo de este proyecto permitió implementar un pipeline ETL completo para el procesamiento de información hospitalaria.

A través de las etapas de extracción, transformación y carga, los datos provenientes de Kaggle son convertidos en información estructurada y almacenada en una base de datos SQLite.

El proyecto demuestra la aplicación práctica de técnicas de:

* Extracción de datos.
* Limpieza y depuración.
* Transformación de información.
* Control de calidad.
* Eliminación de duplicados.
* Validación de datos.
* Almacenamiento relacional.
* Automatización de procesos ETL.

El resultado final es una base de datos hospitalaria con 660 registros distribuidos en cinco entidades, lista para ser utilizada en procesos posteriores de consulta, análisis y procesamiento de datos.


 Autores

Proyecto académico – ETL
Programa: Técnico Profesional en Depuración y Procesamiento de Datos para Inteligencia Artificial
por: maileth polo muñoz y maileth polo muñoz
Asignatura: Extracción, Transformación y Carga de Datos (ETL)
