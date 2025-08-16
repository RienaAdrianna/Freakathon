**open:

Grocery_Items (Main Table)

1. Grocery_ID (Int) [primary_key, auto_increment]
2. Grocey_name (Varchar) [Not null]
3. Category_ID (int) [Foreign Key to categories table(Category_Id)]
4. Purchase Date (Date) [Null]
5. Expiry Data (Date) [Null]
6. Quantity (Decimal(10,2)) [Not Null, DEFAULT 1.00]
7. Unit_ID (Int) [Foreign key]

# Grocery Database Schema

## Table Structure

### 1. categories
| Column | Type | Constraints |
|--------|------|-------------|
| category_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| category_name | VARCHAR(50) | NOT NULL, UNIQUE |
| description | TEXT | NULL |

**Sample Data:**
- fruits, vegetables, dairy, meat, seafood, grains, pantry, frozen, beverages, snacks, herbs_spices, other

### 2. units
| Column | Type | Constraints |
|--------|------|-------------|
| unit_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| unit_name | VARCHAR(20) | NOT NULL, UNIQUE |
| unit_type | VARCHAR(20) | NOT NULL (weight, volume, count, etc.) |

**Sample Data:**
- piece, kg, g, lb, oz, liter, ml, cup, tbsp, tsp, package, bunch, bag

### 3. storage_locations
| Column | Type | Constraints |
|--------|------|-------------|
| location_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| location_name | VARCHAR(50) | NOT NULL, UNIQUE |
| temperature_range | VARCHAR(50) | NULL |

**Sample Data:**
- fridge, freezer, pantry, counter, other

### 4. grocery_items (Main Table)
| Column | Type | Constraints |
|--------|------|-------------|
| item_id | INT | PRIMARY KEY, AUTO_INCREMENT |
| name | VARCHAR(255) | NOT NULL |
| category_id | INT | FOREIGN KEY → categories(category_id), DEFAULT to 'other' category |
| purchase_date | DATE | NULL |
| expiry_date | DATE | NOT NULL |
| quantity | DECIMAL(10,2) | NOT NULL, DEFAULT 1.00 |
| unit_id | INT | FOREIGN KEY → units(unit_id), DEFAULT to 'piece' |
| location_id | INT | FOREIGN KEY → storage_locations(location_id), DEFAULT to 'fridge' |
| notes | TEXT | NULL |
| is_consumed | BOOLEAN | NOT NULL, DEFAULT FALSE |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP |

## Primary Keys
- **categories.category_id** - Primary key for categories table
- **units.unit_id** - Primary key for units table  
- **storage_locations.location_id** - Primary key for storage locations table
- **grocery_items.item_id** - Primary key for main grocery items table

## Foreign Key Relationships

### grocery_items table foreign keys:
1. **category_id** → **categories(category_id)**
   - Ensures each grocery item has a valid category
   - ON DELETE SET DEFAULT (sets to 'other' category if category is deleted)
   - ON UPDATE CASCADE

2. **unit_id** → **units(unit_id)**
   - Ensures each grocery item has a valid unit of measurement
   - ON DELETE SET DEFAULT (sets to 'piece' if unit is deleted)
   - ON UPDATE CASCADE

3. **location_id** → **storage_locations(location_id)**
   - Ensures each grocery item has a valid storage location
   - ON DELETE SET DEFAULT (sets to 'fridge' if location is deleted)
   - ON UPDATE CASCADE

## Indexes (Recommended)
- `idx_grocery_category` on grocery_items(category_id)
- `idx_grocery_location` on grocery_items(location_id)
- `idx_grocery_expiry` on grocery_items(expiry_date)
- `idx_grocery_consumed` on grocery_items(is_consumed)

## Benefits of This Design
1. **Normalization** - Reduces data redundancy by storing categories, units, and locations in separate tables
2. **Data Integrity** - Foreign key constraints ensure referential integrity
3. **Flexibility** - Easy to add new categories, units, or storage locations
4. **Performance** - Indexed columns for faster queries
5. **Scalability** - Can easily extend with additional tables (e.g., suppliers, brands, nutritional info)

Citation: Claude.ai