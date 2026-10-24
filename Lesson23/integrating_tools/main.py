from  fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message": "Developer create successfully", "developer": developer}

@app.post("/projects/")
def create_projects(projects: Project):
    return {"message": "Projects create successfully", "projects": projects}

@app.get("/projects/")
def get_projects():
    sample_projects = Project(
        title="Sample Project",
        description = "This is a sample project",
        languages= ["Python", "JavaScript"],
        lead_developer = Developer(name = "John Doe", experince = 5)
    )
    return {"project": [sample_projects]}

