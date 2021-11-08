from datetime import datetime

from sqlmodel import SQLModel, Field


class UpdateTime(SQLModel, table=True):
    __tablename__ = "updates"
    id: int = Field(default=None, primary_key=True)
    table: str
    timestamp: datetime
