# Inventory Management System

A modern web application for managing retail store inventory. Built with Flask and SQLite, featuring a clean and intuitive user interface.

## Features

- 📦 **Browse Products**: View all products in a responsive grid layout
- ➕ **Add Products**: Easily add new products with details like name, description, price, quantity, and category
- ✏️ **Edit Products**: Update product information and quantities
- 🗑️ **Delete Products**: Remove products from inventory
- 🔍 **Search**: Search products by name or description
- 🏷️ **Filter**: Filter products by category
- 📊 **Statistics**: View key metrics like total products, stock levels, and inventory value
- 🎨 **Modern UI**: Beautiful gradient design with responsive cards and smooth animations

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anstaman/Inventory.git
cd Inventory
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database with sample products:
```bash
python init_db.py
```

This will create a SQLite database with 20 pre-populated sample products.

## Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

### Browsing Products
- The main page displays all products in a grid layout
- Each product card shows the name, description, price, quantity, and category
- Products are color-coded by stock level (low, medium, high)

### Adding a Product
1. Click the "Add Product" button
2. Fill in the product details in the modal form
3. Click "Save Product"

### Editing a Product
1. Click the "Edit" button on any product card
2. Modify the product details in the modal form
3. Click "Save Product"

### Deleting a Product
1. Click the "Delete" button on any product card
2. Confirm the deletion

### Searching and Filtering
- Use the search box to find products by name or description
- Use the category dropdown to filter by category
- Both filters can be used together

## Database Schema

The application uses a simple SQLite database with a single `Product` table:

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key |
| name | String(100) | Product name |
| description | String(500) | Product description |
| quantity | Integer | Stock quantity |
| price | Float | Product price |
| category | String(50) | Product category |
| created_at | DateTime | Creation timestamp |

## API Endpoints

- `GET /` - Main application page
- `GET /api/products` - Get all products
- `GET /api/products/<id>` - Get a specific product
- `POST /api/products` - Create a new product
- `PUT /api/products/<id>` - Update a product
- `DELETE /api/products/<id>` - Delete a product

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with Flask-SQLAlchemy ORM
- **Frontend**: HTML5, CSS3 (vanilla), JavaScript (vanilla)
- **Design**: Modern gradient UI with responsive grid layout

## Project Structure

```
Inventory/
├── app.py              # Main Flask application
├── init_db.py          # Database initialization script
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend application
└── inventory.db        # SQLite database (created after init_db.py)
```

## License

This project is open source and available under the MIT License.
