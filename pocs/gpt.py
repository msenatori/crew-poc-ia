from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model='crewai-llama3',
    base_url = "http://localhost:11434/v1"
)

product_manager = Agent(
    role="Product Manager",
    goal="Define the project requirements and coordinate the team to ensure the successful development of the web page.",
    backstory="As the Product Manager for the {project}, you play a critical role in ensuring the successful development of the web application. "
              "Your primary responsibilities include defining the project requirements, setting clear objectives, and coordinating the work between different team members. "
              "For the {project}, you need to ensure that the UI/UX Designer and Frontend Developer are aligned with the project goals and that the QA Tester verifies the functionality and quality of the web page. "
              "You will communicate with stakeholders to gather requirements and feedback, prioritize tasks, and ensure the project stays on track and meets deadlines. "
              "Your expertise will drive the team towards creating a high-quality, user-friendly, and effective static web page.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

tech_lead = Agent(
    role="Tech Lead",
    goal="Oversee the technical implementation and ensure the quality of the code.",
    backstory="As the Tech Lead for the {project}, your role is to oversee the technical aspects of the project. "
              "You ensure that the frontend development follows best practices, the code is clean and maintainable, and the final product meets all technical requirements. "
              "You also support the team in solving complex technical issues and ensure that the project stays on track technologically.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

ui_ux_designer = Agent(
    role="UI/UX Designer",
    goal="Design the user interface and user experience of the web page.",
    backstory="As the UI/UX Designer for the {project}, you are responsible for creating an intuitive and visually appealing design. "
              "Your designs will provide the blueprint for the frontend developer. "
              "You will create wireframes and design mockups that can be easily interpreted and implemented by other LLMs, ensuring the end product is user-friendly and meets the project's requirements.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

frontend_developer = Agent(
    role="Frontend Developer",
    goal="Develop the user interface of the web page using HTML/JS.",
    backstory="As the Frontend Developer for the {project}, you are tasked with implementing the user interface based on the wireframes and designs provided by the UI/UX Designer. "
              "Your code should be clean, efficient, and fully functional, resulting in a seamless user experience. "
              "You ensure that the design is faithfully translated into a working web page using HTML and JavaScript.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

define_requirements = Task(
    description=("Define the project requirements based on stakeholder input and user needs. "
                 "Ensure that all team members understand the objectives and scope of the project."),
    expected_output="A document outlining the project requirements, objectives, and scope.",
    agent=product_manager,
)

create_wireframes = Task(
    description=("Create wireframes and design mockups for the web page, ensuring they can be easily interpreted by other LLMs."),
    expected_output="Wireframes and design mockups in a format that can be used by the frontend developer.",
    agent=ui_ux_designer,
)

develop_ui = Task(
    description=("Develop the user interface based on the provided wireframes. "
                 "Ensure the design is translated into a working web page using HTML and JavaScript."),
    expected_output="A fully functional web page in HTML/JS.",
    agent=frontend_developer,
)

crew = Crew(
    agents=[product_manager, tech_lead, ui_ux_designer, frontend_developer],
    tasks=[define_requirements, create_wireframes, develop_ui],
    verbose=2
)

inputs = {"project": "Create a simple web page for a to-do list."}
result = crew.kickoff(inputs)

with open("result_gpt.html", "w") as file:
    file.write(result)

print("El resultado se ha guardado en result.html")