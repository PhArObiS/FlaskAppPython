from flask import Flask
from views.user_view import user

app = Flask(__name__)

app.register_blueprint(user)

@app.route("/")
def index():
    return "HOME"

if __name__ == "__main__":
    app.run()