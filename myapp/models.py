from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin




class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


class Jobs(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    job_title: Mapped[str] 
    company: Mapped[str]
    job_role: Mapped[str]
    location: Mapped[str]
    qualification: Mapped[str]
    experience: Mapped[str]
    job_style: Mapped[str]
    salary: Mapped[int]
    
class User(db.Model,UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    industry: Mapped[str]
    address: Mapped[str]
    password: Mapped[str]
    