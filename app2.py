from flask import Flask,request
app = Flask("Alan_WebSerber")
@app.route("/")
def homepage():
    return "歡迎光臨"
if __name__ == "__main__":
    app.run(host = "0.0.0.0")
