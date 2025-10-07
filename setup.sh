#!/bin/bash

# BookMarkd Setup Script
echo "=== BookMarkd Setup Script ==="
echo ""

# Check for required commands
command -v python3 >/dev/null 2>&1 || { echo "Python3 is required but not installed. Aborting." >&2; exit 1; }
command -v node >/dev/null 2>&1 || { echo "Node.js is required but not installed. Aborting." >&2; exit 1; }
command -v npm >/dev/null 2>&1 || { echo "npm is required but not installed. Aborting." >&2; exit 1; }

echo "✓ All prerequisites found"
echo ""

# Setup Backend
echo "=== Setting up Backend ==="
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit backend/.env with your database credentials"
fi

cd ..

# Setup Frontend
echo ""
echo "=== Setting up Frontend ==="
cd frontend

# Install dependencies
echo "Installing npm dependencies..."
npm install

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
fi

cd ..

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "Next steps:"
echo "1. Configure your database in backend/.env"
echo "2. Initialize the database:"
echo "   cd backend && source venv/bin/activate"
echo "   python -c \"from app import app, db; app.app_context().push(); db.create_all()\""
echo "3. Start the backend: cd backend && python app.py"
echo "4. Start the frontend (in a new terminal): cd frontend && npm start"
echo ""
echo "Or use Docker Compose: docker-compose up"
