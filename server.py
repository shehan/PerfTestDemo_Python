from flask import Flask
import time
import random

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return "Hello World!"


def about():
    delay = random.randint(2,6)
    time.sleep(delay)
    return "This is the About Us page...<br>delay: %s seconds" %str(delay)

# This is another way to add a route
app.add_url_rule(rule="/about", endpoint='about', view_func=about, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)  # setting debug=True will auto-reload the server when a file is changed