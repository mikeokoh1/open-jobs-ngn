from flask import Blueprint, render_template
from myapp import db
from .models import Jobs, User
from sqlalchemy import select

views = Blueprint("views", __name__)


@views.route("/")
def home():
  result = db.session.execute(select(User).where(User.username))
  user = result.all
  
  return render_template("home.html", user=user)


@views.route("/jobs")
def jobs():
 
  jobs_query = db.session.query(Jobs).order_by(Jobs.job_title).all()
  
  
  return render_template("jobs.html", jobs=jobs_query)


@views.route("/weather")
def weather():
  return render_template("weather.html")
