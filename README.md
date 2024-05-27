# Proyecto Básico de Python

Este es un proyecto básico en Python 3.12 que demuestra cómo configurar un entorno virtual y gestionar dependencias utilizando `requirements.txt`.

## Requisitos Previos

- Python 3.12 debe estar instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

## Configuración del Entorno Virtual

Sigue estos pasos para configurar el entorno virtual:

1. **Crear el Entorno Virtual**

   Navega al directorio raíz de tu proyecto y ejecuta el siguiente comando para crear un entorno virtual llamado `venv`:

   ```bash
   python3.12 -m venv venv
   ```
2. **Activa el entorno**

    ```bash
    source venv/bin/activate
    ```
3. **Instalar dependencias**

    ```bash
    pip install -r requirements.txt
    ```

4. **Desactivar el entorno**

    ```bash
    deactivate
    ```