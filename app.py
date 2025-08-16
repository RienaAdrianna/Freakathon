from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'





@app.route('/')
def index():
    return render_template('index.html') #master page

if __name__ == "__main__":
    app.run(debug=True) 