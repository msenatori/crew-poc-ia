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
    backstory = "As the Product Manager for the {project}, you play a critical role in ensuring the successful development of the web application. "
              "As the Product Manager for the {project}, you play a critical role in ensuring the successful development of the web application. "
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
    goal="Oversee the technical development and implementation of the web page, ensuring code quality and technical alignment with project goals.",
    backstory = "As the Tech Lead for the {project}, you are responsible for overseeing the technical aspects of the web application development. "
                "You will guide the Frontend Developer in implementing the design provided by the UI/UX Designer, ensuring that the code is clean, efficient, and maintainable. "
                "For the {project}, you need to ensure that all technical components are aligned with the project requirements and goals. "
                "You will also collaborate closely with the Product Manager to make sure that the technical deliverables meet the specified deadlines and quality standards. "
                "Your role includes reviewing code, providing technical guidance, and solving any technical challenges that arise during the development process. "
                "Your leadership will ensure the creation of a robust, high-quality, and functional static web page.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

ui_ux_designer = Agent(
    role="UI/UX Designer",
    goal="Design a user-friendly and visually appealing interface for the web page.",
    backstory = "As the UI/UX Designer for the {project}, your main responsibility is to create a user-friendly and visually appealing interface for the web application. "
                "You will collaborate with the Product Manager to understand the project requirements and the target audience's needs. "
                "For the {project}, you need to ensure that the design aligns with the project's goals and enhances the user experience. "
                "Your tasks include creating wireframes, mockups, and prototypes, and providing the Frontend Developer with all necessary design assets and guidelines. "
                "Your creativity and attention to detail will be crucial in delivering a design that not only looks good but also provides a seamless and enjoyable user experience.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

frontend_developer = Agent(
    role="Frontend Developer",
    goal="Implement the user interface design using HTML, CSS, and JavaScript, ensuring a responsive, interactive, and minimalist web page.",
    backstory = "As the Frontend Developer for the {project}, your primary responsibility is to implement the user interface design provided by the UI/UX Designer. "
                "You will work closely with the Tech Lead to ensure that the code is clean, efficient, and follows best practices. "
                "For the {project}, you need to translate the design mockups into a fully functional, responsive, interactive, and minimalist web page using HTML, CSS, and JavaScript. "
                "You will also collaborate with the Product Manager to ensure that the implementation meets the project requirements and deadlines. "
                "Your technical skills and attention to detail will be essential in delivering a high-quality static web page that provides an excellent user experience while maintaining a minimalist aesthetic.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)

define_requirements = Task(
    description=(
        "1. Gather and prioritize project requirements from stakeholders.\n"
        "2. Identify the target audience and define user personas, considering their interests and needs.\n"
        "3. Develop a detailed project plan, including clear objectives, key milestones, and deadlines.\n"
        "4. Collaborate with the UI/UX Designer to outline the essential features and user flow.\n"
        "5. Ensure alignment with the project's goals and overall vision.\n"
        "6. Define the criteria for success and key performance indicators (KPIs) for the project.\n"
        "7. Document the project scope and constraints, including any technical limitations or dependencies."
    ),
    expected_output="A comprehensive project requirements document with a detailed project plan, user personas, objectives, key milestones, and success criteria.",
    agent=product_manager,
)

coordinate_team = Task(
    description=(
        "1. Facilitate communication and collaboration between team members, including the UI/UX Designer, Frontend Developer, and Tech Lead.\n"
        "2. Organize and lead regular project meetings to track progress and address any issues or blockers.\n"
        "3. Ensure that each team member understands their roles and responsibilities within the project.\n"
        "4. Monitor the project timeline and adjust plans as necessary to stay on track.\n"
        "5. Gather and incorporate feedback from stakeholders and team members to refine project goals and deliverables.\n"
        "6. Manage project documentation and ensure all information is up-to-date and accessible to the team.\n"
        "7. Report project status and key updates to stakeholders regularly."
    ),
    expected_output="A well-coordinated team that communicates effectively, meets project milestones, and produces high-quality deliverables. Regular project status reports and updated project documentation.",
    agent=product_manager,
)

technical_guidance = Task(
    description=(
        "1. Provide technical guidance and support to the development team, ensuring best practices are followed.\n"
        "2. Review the UI/UX designs and provide feedback on technical feasibility and improvements.\n"
        "3. Oversee the implementation of the frontend code, ensuring it aligns with the project's technical requirements and standards.\n"
        "4. Perform code reviews and offer constructive feedback to the Frontend Developer.\n"
        "5. Identify and address any technical challenges or obstacles that arise during the development process.\n"
        "6. Ensure the project is scalable, maintainable, and optimized for performance.\n"
        "7. Collaborate with the Product Manager to ensure technical aspects align with project goals and deadlines."
    ),
    expected_output="A technically sound implementation of the project, with clean, efficient, and maintainable code. Regular technical reviews and feedback, along with solutions to any technical challenges encountered.",
    agent=tech_lead,
)

create_wireframes = Task(
    description=(
        "1. Develop wireframes and mockups that align with the project's goals and user requirements.\n"
        "2. Ensure that the wireframes include all necessary elements for a user-friendly, intuitive, and minimalist design.\n"
        "3. Incorporate feedback from the Product Manager and Tech Lead to refine the design.\n"
        "4. Define the visual style and design guidelines, including typography, color schemes, and layout principles.\n"
        "5. Create interactive prototypes to demonstrate user flow and interactions.\n"
        "6. Ensure the designs are responsive and adapt well to different screen sizes and devices.\n"
        "7. Collaborate with the Frontend Developer to ensure that the implementation aligns with the design vision.\n"
        "8. Save the wireframes and mockups in a format that can be easily read and understood by another LLM, such as JSON or a structured text format."
    ),
    expected_output="Detailed wireframes and mockups that serve as a blueprint for the development team, interactive prototypes, and design guidelines that ensure a cohesive and user-friendly design. Wireframes should be saved in a format that is easily interpretable by another LLM, such as JSON or a structured text format.",
    agent=ui_ux_designer,
)

implement_design = Task(
    description=(
        "1. Review the wireframes and design guidelines provided by the UI/UX Designer.\n"
        "2. Develop the front-end of the web application based on the provided wireframes and design specifications.\n"
        "3. Ensure that the implementation is responsive and works well across different devices and screen sizes.\n"
        "4. Use HTML, CSS, and JavaScript to translate the wireframes into functional web pages.\n"
        "5. Collaborate with the UI/UX Designer to ensure the design vision is accurately translated into code.\n"
        "6. Optimize the web pages for performance, ensuring fast load times and smooth interactions.\n"
        "7. Implement any interactivity or animations as specified in the wireframes.\n"
        "8. Conduct regular reviews and testing to ensure the design is implemented correctly and meets the project's requirements.\n"
        "9. Document the implementation process and any deviations from the wireframes, providing clear explanations."
    ),
    expected_output="A fully functional and responsive front-end of the web application, implemented in HTML and JavaScript, according to the provided wireframes and design specifications. Detailed documentation of the implementation process and any deviations from the original design.",
    agent=frontend_developer,
)
                
crew = Crew(
    agents=[product_manager, tech_lead, ui_ux_designer, frontend_developer],
    tasks=[define_requirements, coordinate_team, technical_guidance, create_wireframes, implement_design],
    verbose=2
)

result = crew.kickoff({"project": "Create a simple web page for a to-do list."})

with open("result.html", "w") as file:
    file.write(result)

print("El resultado se ha guardado en result.html")
