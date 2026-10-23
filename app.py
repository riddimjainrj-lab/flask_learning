from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    name = "Riddim"
    course = "Machine Learning"
    accuracy = 92
    risk_score = 25

    if request.method == "POST":
        risk_score = int(request.form.get("risk_score", 25))

    return render_template(
        "dashboard.html",
        name=name,
        course=course,
        accuracy=accuracy,
        risk_score=risk_score
    )

if __name__ == "__main__":
    app.run(debug=True)
