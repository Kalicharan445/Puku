
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        birthday = request.form["birthday"]
        
        today = datetime.date.today().strftime("%Y-%m-%d")
        
        if birthday == today:
            message = f"Happy Birthday, {name}!"
        else:
            message = f"Thanks for submitting, {name}!"
        
        return render_template("index.html", message=message)
    
    return render_template("index.html", message="")

if __name__ == "__main__":
    app.run(debug=True)
