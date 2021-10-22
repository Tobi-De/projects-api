from typing import Optional

from deta import Deta
from fastapi import APIRouter
from pydantic import conint

from .core.config import settings
from .schemas import Project, ProjectCreate, ProjectUpdate

deta = Deta(settings.DETA_PROJECT_KEY)
db = deta.Base("projects")

router = APIRouter()


@router.get("/read", response_model=list[Project])
async def read_projects(limit: conint(ge=0) = 100, last_key: Optional[str] = None):
    return db.fetch(limit=limit, last=last_key).items


@router.get("read/{id}", response_model=Project)
async def read_project(key: str):
    return db.get(key=key)


@router.post(path="/create", response_model=Project)
async def create_project(project_in: ProjectCreate):
    data = project_in.dict()
    data["created"] = project_in.created.isoformat()
    return db.insert(data)


@router.post(path="/update/{key}", response_model=Project)
async def update_project(key: str, project_in: ProjectUpdate):
    db.update(project_in.dict(exclude_unset=True), key=key)
    return db.get(key)


@router.post(path="/delete/{key}")
async def delete_project(key: str):
    db.delete(key)
    return {"key": key}
