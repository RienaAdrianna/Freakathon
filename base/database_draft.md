**open:

Grocery_Items (Main Table)

1. Grocery_ID (Int) [primary_key, auto_increment]
2. Grocey_name (Varchar) [Not null]
3. Category_ID (int) [Foreign Key to categories table(Category_Id)]
4. Purchase Date (Date) [Null]
5. Expiry Data (Date) [Null]
6. Quantity (Decimal(10,2)) [Not Null, DEFAULT 1.00]
7. Unit_ID (Int) [Foreign key]

#Create Model
class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Category {self.category_name}>'
