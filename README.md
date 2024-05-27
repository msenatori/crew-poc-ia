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
5. **Configurar llama3**

   Crear un archivo llamado ModelFile en el raiz (no lo subi)
   
   ```
   FROM llama3
   
   # Set parameters
   
   PARAMETER temperature 0.8
   PARAMETER stop Result
   
   # Sets a custom system message to specify the behavior of the chat assistant
   
   # Leaving it blank for now.
   
   SYSTEM """"""
   ```

   Crear el modelo

   ```bash
   ollama create crewai-llama3 -f .\Modelfile
   ```

   Validarlo.

   ```bash
   ollama list
   ```
