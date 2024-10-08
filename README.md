# Desafío Instancias de Usuario
## Descripción

Este proyecto tiene como objetivo procesar un archivo de usuarios en formato JSON, convertir cada entrada válida en una instancia de la clase `Usuario` y registrar los errores de formato o datos incompletos en un archivo de log. Está diseñado para manejar grandes cantidades de datos de usuarios y asegurar que cualquier error en la estructura de los datos sea registrado para su análisis posterior.

## Archivos del Proyecto

- **script.py**: Script principal que procesa el archivo de usuarios, convierte los datos válidos en instancias de `Usuario`, y maneja errores.
- **usuarios.txt**: Archivo de entrada con los datos de los usuarios en formato JSON. Cada línea debe contener un objeto JSON con los campos: `nombre`, `apellido`, `email`, y `genero`.
- **error.log**: Archivo de salida donde se registran los errores encontrados durante el procesamiento. Se limpia en cada ejecución para evitar la acumulación de errores previos.
- **usuario.py**: Contiene la clase `Usuario`, que define los atributos `nombre`, `apellido`, `email`, y `genero` para cada usuario.

## Requisitos

Para ejecutar este proyecto, se requiere tener instalado:
Sistema Operativo: Windows, Linux, MacOS Lenguaje de programación: Python 3.12

## Instalación del Proyecto

Clona el repositorio:

```bash
git clone https://github.com/KarenLimari/DE-Instancias_de_usuario.git
```

## Instrucciones para Ejecutar el Proyecto

```bash
cd script.py
```
## Autor

Karen Limari - Ambar Zambrano - Arlenis Gonzalez

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE.md para más detalles.