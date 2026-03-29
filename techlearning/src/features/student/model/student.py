from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    dob = Column(Date)
    address = Column(String(255))
    course = Column(String(100))
    batch = Column(String(50))
    lastupdateddate = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP")
    )

    def __init__(self, schema=None, **kwargs):
        """Accept either a Pydantic schema or individual keyword arguments."""
        if schema is not None and not isinstance(schema, dict):
            # Extract fields from Pydantic schema
            for field in ['id', 'name', 'dob', 'address', 'course', 'batch']:
                val = getattr(schema, field, None)
                if val is not None and field not in kwargs:
                    kwargs[field] = val
        
        super().__init__(**kwargs)

    def __repr__(self):
        return (
            f"<Student(id={self.id}, name='{self.name}', "
            f"course='{self.course}')>"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "dob": self.dob.isoformat() if self.dob is not None else None,
            "address": self.address,
            "course": self.course,
            "batch": self.batch,
            "lastupdateddate": (
                self.lastupdateddate.isoformat() if self.lastupdateddate is not None else None
            ),
        }
