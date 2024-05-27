from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

llm = ChatOpenAI(
    model='crewai-llama3',
    base_url="http://localhost:11434/v1"
)

# Agentes
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

# Tareas
generate_html = Task(
    description=(
        "1. Create the main structure of the web page using HTML5.\n"
        "2. Include the following sections: header, main (with search and task list sections), and footer.\n"
        "3. Ensure the header contains navigation links (Back to previous page, Logout).\n"
        "4. The main section should have a search input and a list of tasks.\n"
        "5. The footer should contain copyright information and links (Terms of use, Contact).\n"
        "6. Use semantic HTML tags and ensure the code is properly indented."
    ),
    expected_output="An HTML file with the structure and content specified.",
    agent=frontend_developer,
)

generate_css = Task(
    description=(
        "1. Create a CSS stylesheet to style the HTML structure of the to-do list web page.\n"
        "2. Use a consistent color scheme with the following colors: #003366 (header and footer), #e0e0e0 (task items), and #f4f4f4 (background).\n"
        "3. Ensure the header and footer have a white text color and are styled for a clean, professional look.\n"
        "4. The search input should have rounded corners and a border.\n"
        "5. Task items should have a border-radius, padding, and margin for spacing.\n"
        "6. Ensure the page is responsive and works well on different screen sizes."
    ),
    expected_output="A CSS file with styles applied to the HTML structure as specified.",
    agent=frontend_developer,
)

# Crew
crew = Crew(
    agents=[frontend_developer],
    tasks=[generate_html, generate_css],
    verbose=2
)

inputs = {"project": "Create a simple web page for a to-do list."}
result = crew.kickoff(inputs)

# Guardar los resultados en archivos
html_content = result["generate_html"]
css_content = result["generate_css"]

with open("index.html", "w") as file:
    file.write(html_content)

with open("styles.css", "w") as file:
    file.write(css_content)

print("Los archivos HTML y CSS se han guardado correctamente.")