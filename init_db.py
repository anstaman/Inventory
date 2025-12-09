from app import app, db, Product

def init_database():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if database is already populated
        if Product.query.count() > 0:
            print("Database already contains products. Skipping initialization.")
            return
        
        # Sample products data
        sample_products = [
            {
                'name': 'Wireless Mouse',
                'description': 'Ergonomic wireless mouse with 2.4GHz connectivity',
                'quantity': 45,
                'price': 29.99,
                'category': 'Electronics'
            },
            {
                'name': 'USB-C Cable',
                'description': 'High-speed USB-C to USB-C cable, 6ft length',
                'quantity': 120,
                'price': 12.99,
                'category': 'Electronics'
            },
            {
                'name': 'Office Chair',
                'description': 'Ergonomic office chair with lumbar support',
                'quantity': 15,
                'price': 199.99,
                'category': 'Furniture'
            },
            {
                'name': 'Standing Desk',
                'description': 'Adjustable height standing desk, electric motor',
                'quantity': 8,
                'price': 499.99,
                'category': 'Furniture'
            },
            {
                'name': 'LED Monitor 27"',
                'description': '27-inch LED monitor, 1920x1080 resolution',
                'quantity': 22,
                'price': 249.99,
                'category': 'Electronics'
            },
            {
                'name': 'Mechanical Keyboard',
                'description': 'RGB mechanical keyboard with blue switches',
                'quantity': 35,
                'price': 89.99,
                'category': 'Electronics'
            },
            {
                'name': 'Notebook Set',
                'description': 'Set of 5 lined notebooks, A5 size',
                'quantity': 200,
                'price': 15.99,
                'category': 'Office Supplies'
            },
            {
                'name': 'Blue Pens (Pack of 12)',
                'description': 'Ballpoint pens, blue ink, pack of 12',
                'quantity': 150,
                'price': 5.99,
                'category': 'Office Supplies'
            },
            {
                'name': 'Desk Lamp',
                'description': 'LED desk lamp with adjustable brightness',
                'quantity': 40,
                'price': 34.99,
                'category': 'Electronics'
            },
            {
                'name': 'Whiteboard',
                'description': 'Magnetic whiteboard, 36x24 inches',
                'quantity': 12,
                'price': 45.99,
                'category': 'Office Supplies'
            },
            {
                'name': 'Bluetooth Speaker',
                'description': 'Portable Bluetooth speaker with 10-hour battery',
                'quantity': 55,
                'price': 59.99,
                'category': 'Electronics'
            },
            {
                'name': 'Laptop Stand',
                'description': 'Aluminum laptop stand, adjustable height',
                'quantity': 30,
                'price': 39.99,
                'category': 'Electronics'
            },
            {
                'name': 'File Organizer',
                'description': 'Desktop file organizer with 5 compartments',
                'quantity': 25,
                'price': 24.99,
                'category': 'Office Supplies'
            },
            {
                'name': 'Coffee Mug',
                'description': 'Ceramic coffee mug, 16 oz capacity',
                'quantity': 80,
                'price': 9.99,
                'category': 'Kitchen'
            },
            {
                'name': 'Water Bottle',
                'description': 'Stainless steel water bottle, 32 oz, insulated',
                'quantity': 65,
                'price': 24.99,
                'category': 'Kitchen'
            },
            {
                'name': 'Desk Organizer',
                'description': 'Mesh desk organizer with multiple compartments',
                'quantity': 42,
                'price': 19.99,
                'category': 'Office Supplies'
            },
            {
                'name': 'Webcam HD',
                'description': '1080p HD webcam with built-in microphone',
                'quantity': 28,
                'price': 69.99,
                'category': 'Electronics'
            },
            {
                'name': 'Printer Paper',
                'description': 'A4 printer paper, 500 sheets per ream',
                'quantity': 100,
                'price': 8.99,
                'category': 'Office Supplies'
            },
            {
                'name': 'Stapler',
                'description': 'Heavy-duty stapler, 50-sheet capacity',
                'quantity': 60,
                'price': 14.99,
                'category': 'Office Supplies'
            },
            {
                'name': 'USB Flash Drive 64GB',
                'description': 'USB 3.0 flash drive, 64GB capacity',
                'quantity': 90,
                'price': 18.99,
                'category': 'Electronics'
            }
        ]
        
        # Add all products to the database
        for product_data in sample_products:
            product = Product(**product_data)
            db.session.add(product)
        
        db.session.commit()
        print(f"Database initialized with {len(sample_products)} products!")

if __name__ == '__main__':
    init_database()
