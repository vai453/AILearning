from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class StudentSchema(BaseModel):
    """Schema for Student model - used for create, update, and response."""
    id: Optional[int] = None
    name: str
    dob: Optional[date] = None
    address: Optional[str] = None
    course: Optional[str] = None
    batch: Optional[str] = None
    lastupdateddate: Optional[datetime] = None

    class Config:
        from_attributes = True  # Enable ORM mode to serialize SQLAlchemy models
