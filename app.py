from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:grocery123@localhost/grocery'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('dashboard.html') #master page

if __name__ == "__main__":
    app.run(debug=True) 