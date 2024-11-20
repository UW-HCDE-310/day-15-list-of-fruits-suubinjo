from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    filtered_fruits = [
        fruit for fruit in fruits
        if fruit["name"].startswith("o") and fruit["quantity"] < 3
    ]
    return render_template("index.html", fruits=filtered_fruits)

if __name__ == "__main__":
    app.run(debug=True)
