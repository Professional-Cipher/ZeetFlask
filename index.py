from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>ZeetFlask</h1>"


if __name__ == "__main__":
    app.run(debug=False)