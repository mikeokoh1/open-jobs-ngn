from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from myapp import db
from .models import User, Jobs
from sqlalchemy import select
from flask_login import login_required, login_user, logout_user, current_user


auth = Blueprint("auth", __name__)

@auth.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        
        result = db.session.execute(select(User).where(User.email == email))
        user = result.first()

        
        if email:
            if check_password_hash(User.password, password):
                flash("logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("/admin"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")
            
            
    return render_template("admin_login.html")


@auth.route("/admin_signup", methods=["GET", "POST"])
def admin_signup():
    if request.method == "POST":
        username = request.form.get("name")
        email = request.form.get("email")
        industry = request.form.get("industry")
        address = request.form.get("address")
        password = request.form.get("password")
        
        
        result = db.session.execute(select(User).where(User.email == email))
        user = result.first()
        
        if email:
            flash("Admin with email already exist.", category="error")
        if username:
            flash("Admin with company name already exist.", category="error")
        else:
            
            user = User(
                username=username,
                email=email,
                industry=industry,
                address=address,
                password=generate_password_hash(password)
            )
            db.session.add(user)
            db.session.commit()
            flash("Admin account succesfully created.", category="success")
            login_user(User, remember=True)
            return redirect(url_for("/admin"))

    return render_template("admin_signup.html")

@auth.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if request.method == "POST":
        # Check if the form was submitted
        job_title = request.form.get("job_title")
        
        # Perform validation to ensure job_title is not empty
        if job_title:
            company = request.form.get("company")
            job_role = request.form.get("job_role")
            location = request.form.get("location")
            qualification = request.form.get("qualification")
            experience = request.form.get("experience")
            job_style = request.form.get("job_style")
            salary = request.form.get("salary")
            
            new_job = Jobs(
                job_title=job_title,
                company=company,
                job_role=job_role,
                location=location,
                qualification=qualification,
                experience=experience,
                job_style=job_style,
                salary=salary
            )
            db.session.add(new_job)
            db.session.commit()
            flash("Job added successfully!", "success")
            return redirect(url_for("auth.admin"))  # Redirect back to the admin page after adding the job
        else:
            # Handle case where job_title is empty
            flash("Job title cannot be empty!", "error")
            return render_template("admin.html", user=current_user)
    
    return render_template("/admin")
    
@auth.route("/admin_logout")
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for("/admin_login"))