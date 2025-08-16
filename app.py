from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:grocery123@localhost/grocery'


@app.route('/')
@app.route('/dashboard')

def dashboard():
    return render_template('dashboard.html')

def index():
    return render_template('layout.html')  

if __name__ == "__main__":
    app.run(debug=True) 