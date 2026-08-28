from flask import Flask, render_template, request
from datetime import datetime

from zodiac_data import zodiac_data
from zodiac_logic import get_zodiac

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/zodiac", methods=["POST"])

# create function zodiac in this route to take the date
def zodiac():

    # dob stores the value of the date submitted in the form
    dob = request.form["dob"]

    # birth date refine the date from regular string to actual python TIME
    birth_date = datetime.strptime(dob, "%Y-%m-%d")

    month = birth_date.month
    day = birth_date.day

    zodiac_sign = get_zodiac(month, day)

    zodiac_info = zodiac_data[zodiac_sign]

    print("Zodiac:", zodiac_sign)
    print("Information:", zodiac_info)

    return "Zodiac calculated successfully!"


if __name__ == "__main__":
    app.run(debug=True)