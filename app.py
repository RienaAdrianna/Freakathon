from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocery.db'
db = SQLAlchemy(app)

# Create Category Model
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Category {self.category_name}>'


@app.route('/')
def index():
    return render_template('index.html') #master page

if __name__ == "__main__":
    app.run(debug=True) 