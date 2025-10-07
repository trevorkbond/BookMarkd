"""
Database initialization script for BookMarkd
"""
from app import app, db
from models import User, Book

def init_db():
    """Initialize the database with tables"""
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✓ Database tables created successfully!")
        
        # Optional: Add sample data
        add_sample_data = input("Add sample data? (y/n): ")
        if add_sample_data.lower() == 'y':
            # Check if data already exists
            if User.query.first() is None:
                print("Adding sample data...")
                
                # Add sample user
                user = User(username='demo_user', email='demo@bookmarkd.com')
                db.session.add(user)
                
                # Add sample books
                books = [
                    Book(
                        title='To Kill a Mockingbird',
                        author='Harper Lee',
                        isbn='9780061120084',
                        description='A classic novel about racial injustice in the American South.'
                    ),
                    Book(
                        title='1984',
                        author='George Orwell',
                        isbn='9780451524935',
                        description='A dystopian novel about totalitarianism.'
                    ),
                    Book(
                        title='Pride and Prejudice',
                        author='Jane Austen',
                        isbn='9780141439518',
                        description='A romantic novel of manners.'
                    )
                ]
                
                for book in books:
                    db.session.add(book)
                
                db.session.commit()
                print("✓ Sample data added successfully!")
            else:
                print("Sample data already exists, skipping...")

if __name__ == '__main__':
    init_db()
