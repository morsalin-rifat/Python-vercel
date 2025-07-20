from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "হ্যালো ভাই! এটা আমার Python ওয়েব অ্যাপ ❤️"

if __name__ == "__main__":
    app.run()
