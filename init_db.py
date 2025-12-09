from app import app, db, Product, Category

def init_database():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if database is already populated
        if Product.query.count() > 0:
            print("Database already contains products. Skipping initialization.")
            return
        
        # Initialize categories
        categories = [
            'DEMOLAITTEET',
            'VALMIIT',
            'KOTELOT',
            'IT TAVARAT',
            'TARVIKKEET',
            'LAITEOSAT'
        ]
        
        for cat_name in categories:
            category = Category(name=cat_name)
            db.session.add(category)
        
        db.session.commit()
        print(f"Initialized {len(categories)} categories")
        
        # Warehouse locations
        internal_warehouses = ['Vantaa', 'Tampere', 'Hollola']
        external_warehouses = ['Ulkovarasto 1', 'Ulkovarasto 2', 'Ulkovarasto 3']
        all_locations = internal_warehouses + external_warehouses
        
        # Sample products data with Finnish context
        sample_products = [
            {
                'name': 'Demokotelo A1',
                'description': 'Demokäyttöön tarkoitettu esittelykotelo',
                'quantity': 15,
                'price': 450.00,
                'category': 'DEMOLAITTEET',
                'location': 'Vantaa'
            },
            {
                'name': 'Demokotelo B2',
                'description': 'Asiakasesittelyyn soveltuva demokotelo',
                'quantity': 8,
                'price': 520.00,
                'category': 'DEMOLAITTEET',
                'location': 'Tampere'
            },
            {
                'name': 'Valmis tuote X100',
                'description': 'Täysin kasattu ja testattu tuote',
                'quantity': 45,
                'price': 1200.00,
                'category': 'VALMIIT',
                'location': 'Vantaa'
            },
            {
                'name': 'Valmis tuote X200',
                'description': 'Premium-versio valmiista tuotteesta',
                'quantity': 22,
                'price': 1850.00,
                'category': 'VALMIIT',
                'location': 'Hollola'
            },
            {
                'name': 'Alumiinikotelo 300x200x150',
                'description': 'Alumiininen suojakotelo',
                'quantity': 120,
                'price': 85.00,
                'category': 'KOTELOT',
                'location': 'Ulkovarasto 1'
            },
            {
                'name': 'Muovikotelo 250x150x100',
                'description': 'Muovinen kevyt kotelo',
                'quantity': 200,
                'price': 35.00,
                'category': 'KOTELOT',
                'location': 'Ulkovarasto 1'
            },
            {
                'name': 'Teräskotelo 400x300x200',
                'description': 'Vahva teräskotelo',
                'quantity': 55,
                'price': 145.00,
                'category': 'KOTELOT',
                'location': 'Vantaa'
            },
            {
                'name': 'Kannettava tietokone',
                'description': 'Työasema-kannettava, Intel i7',
                'quantity': 12,
                'price': 1200.00,
                'category': 'IT TAVARAT',
                'location': 'Tampere'
            },
            {
                'name': 'Näyttö 24"',
                'description': 'Full HD -näyttö',
                'quantity': 28,
                'price': 180.00,
                'category': 'IT TAVARAT',
                'location': 'Tampere'
            },
            {
                'name': 'Verkkokaapeli Cat6 (100m)',
                'description': 'Verkkokaapelirulla',
                'quantity': 45,
                'price': 65.00,
                'category': 'IT TAVARAT',
                'location': 'Ulkovarasto 2'
            },
            {
                'name': 'USB-muistitikku 32GB',
                'description': 'USB 3.0 muistitikku',
                'quantity': 150,
                'price': 12.00,
                'category': 'IT TAVARAT',
                'location': 'Vantaa'
            },
            {
                'name': 'Ruuvit M4x20 (100kpl)',
                'description': 'Ruuvipakkaus',
                'quantity': 300,
                'price': 8.50,
                'category': 'TARVIKKEET',
                'location': 'Ulkovarasto 3'
            },
            {
                'name': 'Mutterit M4 (100kpl)',
                'description': 'Mutteripakkaus',
                'quantity': 280,
                'price': 6.50,
                'category': 'TARVIKKEET',
                'location': 'Ulkovarasto 3'
            },
            {
                'name': 'Kaapelinipat (50kpl)',
                'description': 'Muoviset kaapelinipat',
                'quantity': 500,
                'price': 4.00,
                'category': 'TARVIKKEET',
                'location': 'Hollola'
            },
            {
                'name': 'Teippi 50mm (50m)',
                'description': 'Pakkausteipin rulla',
                'quantity': 180,
                'price': 5.50,
                'category': 'TARVIKKEET',
                'location': 'Hollola'
            },
            {
                'name': 'Emolevy ATX',
                'description': 'Vaihto-osa: ATX-emolevy',
                'quantity': 8,
                'price': 145.00,
                'category': 'LAITEOSAT',
                'location': 'Vantaa'
            },
            {
                'name': 'Virtalähde 500W',
                'description': 'Modulaarinen virtalähde',
                'quantity': 18,
                'price': 89.00,
                'category': 'LAITEOSAT',
                'location': 'Vantaa'
            },
            {
                'name': 'Tuuletin 120mm',
                'description': 'Kotelo- tai jäähdytystuuletin',
                'quantity': 95,
                'price': 12.00,
                'category': 'LAITEOSAT',
                'location': 'Ulkovarasto 2'
            },
            {
                'name': 'Näppäimistö',
                'description': 'Langallinen näppäimistö',
                'quantity': 35,
                'price': 25.00,
                'category': 'LAITEOSAT',
                'location': 'Tampere'
            },
            {
                'name': 'Hiiri',
                'description': 'Optinen hiiri USB',
                'quantity': 42,
                'price': 15.00,
                'category': 'LAITEOSAT',
                'location': 'Tampere'
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
