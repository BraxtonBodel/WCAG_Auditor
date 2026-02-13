from sqlalchemy import Column, Integer, String, Text
from pgvector.sqlalchemy import Vector
from .database import Base

class WCAGGuideline(Base):
    __tablename__ = "wcag_guidelines"

    id = Column(Integer, primary_key=True, index=True)
    success_criterion = Column(String, index=True)
    description = Column(Text)
    level = Column(String)

    embedding = Column(Vector(768))