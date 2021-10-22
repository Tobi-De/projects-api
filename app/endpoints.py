from typing import Optional

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import conint

from .core.deta import db
from .schemas import Project, ProjectCreate, ProjectUpdate

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get(path="/", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.post(path="/create", response_model=Project)
async def create_project(project_in: ProjectCreate):
    data = project_in.dict()
    data["created"] = project_in.created.isoformat()
    return db.insert(data)


@router.post(path="/update/{key}")
async def update(key: str, project_in: ProjectUpdate):
    db.update(project_in.dict(exclude_unset=True), key=key)
    return db.get(key)


@router.get("/read", response_model=list[Project])
async def read_projects(limit: conint(ge=0) = 100, last_key: Optional[str] = None):
    return db.fetch(limit=limit, last=last_key).items


@router.get("/{id}", response_model=Project)
async def read_project(key: str):
    return db.get(key=key)
