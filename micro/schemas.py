from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, AnyHttpUrl


class ProjectImage(BaseModel):
    alt: str
    url: AnyHttpUrl


class ProjectBase(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    tags: list[str] = Field(default_factory=list)
    website: Optional[AnyHttpUrl] = None
    status: Optional[str] = None
    tech_stack: list[str] = Field(default_factory=list)
    images: list[ProjectImage] = Field(default_factory=list)
    content: Optional[str] = None
    created: datetime = Field(default_factory=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ProjectCreate(ProjectBase):
    title: str
    summary: str


class ProjectUpdate(ProjectBase):
    pass


class ProjectInDB(ProjectBase):
    key: str


class Project(ProjectInDB):
    pass
