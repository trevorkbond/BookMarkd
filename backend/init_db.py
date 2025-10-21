"""This isn't useful yet, ignore for now"""

"""Database initialization script for BookMarkd."""
from backend.app import create_app, db  # Ensures configured app context loads bindings
from models import *  # noqa: F403,F401 makes SQLAlchemy aware of models

def init_db():
    """Create all registered database tables."""
    app = create_app()
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✓ Database tables created successfully!")

if __name__ == '__main__':
    init_db()
