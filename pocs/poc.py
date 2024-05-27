from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model='crewai-llama3',
    base_url = "http://localhost:11434/v1"
)

arquitecto = Agent(
    role="Arquitecto de Software",
    goal="Diseñar la arquitectura de software para el proyecto.",
    backstory = "Como Arquitecto de Software para el proyecto {proyecto}, tu objetivo es diseñar una arquitectura de software sólida y escalable que cumpla con los requisitos del proyecto. "
        "Debes definir la estructura general del sistema, incluidos los componentes, módulos y la interacción entre ellos. "
        "Tu experiencia en diseño de software será fundamental para garantizar que el sistema sea eficiente, seguro y fácil de mantener."
        "Todo lo que hagas debe ser documentado y comunicado claramente al equipo de desarrollo."
        "Tu trabajo sentará las bases para el desarrollo exitoso del proyecto."
        "Conoces SQL y LaTeX."
        "Tu trabajo sentará las bases para el desarrollo exitoso del proyecto."
        "Escribis en español.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

documentar_arquitectura = Task(
    description=(
        "1. Documentar la arquitectura de software del proyecto {proyecto} en un formato claro y detallado.\n"
        "2. Incluir una descripción general de la arquitectura, los componentes principales, los módulos y su interacción.\n"
        "3. Detallar los patrones de diseño utilizados, las tecnologías seleccionadas y las decisiones clave de diseño.\n"
        "4. Asegurarse de que la documentación sea comprensible para los desarrolladores y otros interesados en el proyecto.\n"
        "5. Proporcionar ejemplos y diagramas para ilustrar la arquitectura de software."
        "6. Usar LaTeX para formatear la documentación de la arquitectura."
    ),
    expected_output="Un documento LaTeX que describe la arquitectura de software del proyecto {proyecto}.",
    agent=arquitecto,
)

anexar_documentacion_dev = Task(
    description=(
        "1. Anexar el documento sql de la base de datos del proyecto {proyecto}.\n"
        "2. Anexar el documento de la arquitectura de software del proyecto {proyecto}.\n"
        "3. Los graficos deben ser creados en formato ascii."
    ),
    expected_output="Un informe detallado que evalúa la arquitectura de software del proyecto {proyecto} y propone mejoras o soluciones.",
    agent=arquitecto,
)


crew = Crew(
    agents=[arquitecto],
    tasks=[documentar_arquitectura, anexar_documentacion_dev],
    verbose=1
)

inputs = {"proyecto": "Todos App"}
result = crew.kickoff(inputs)

print(result)