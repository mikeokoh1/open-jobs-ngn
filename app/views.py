from flask import Blueprint, render_template

views = Blueprint("views", __name__)

Jobs = [{
    'id': '1',
    'title': 'Settlement Agent',
    'Company': 'Unified Payments',
    'Location': 'Lagos State',
    'Salary': 'N250,000',
    'Work style': 'Onsite'
}, {
    'id': '2',
    'title': 'Operation Agent',
    'Company': 'Globus Bank',
    'Location': 'Niger State',
    'Salary': 'N350,000',
    'Work style': 'Onsite'
}, {
    'id': '3',
    'title': 'Relationship manager',
    'Company': 'E-Transact',
    'Location': 'Lagos State',
    'Salary': 'N280,000',
    'Work style': 'Onsite'
}, {
    'id': '4',
    'title': 'FrontEnd Developer',
    'Company': 'Kuda micro-finance Bank',
    'Location': 'Lagos State',
    'Salary': 'N450,000',
    'Work style': 'Hybrid'
}, {
    'id': '5',
    'title': 'Clearing Agent',
    'Company': 'Interswitch Limited',
    'Location': 'Lagos State',
    'Salary': 'N480,000',
    'Work style': 'Onsite'
}]


@views.route("/")
def home():
  return render_template("home.html")


@views.route("/jobs")
def jobs():
  return render_template("jobs.html", jobs=Jobs)
