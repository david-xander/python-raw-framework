# app.py

from raw.api import API


app = API()


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page 4"


@app.route("/about/{cosa}")
def about(request, response, cosa):
    response.text = f"Hello from the ABOUT page {cosa}"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"
