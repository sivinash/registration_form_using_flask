from flask import Flask,render_template,url_for,session
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)