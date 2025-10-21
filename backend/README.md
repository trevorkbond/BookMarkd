# BookMarkd Backend

Flask-based REST API for BookMarkd application.

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. Initialize the database:

```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

5. Run the development server:

```bash
python app.py
```

The API will be available at `http://localhost:5001`

## API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/books` - Get all books

## Database Configuration

The application uses MySQL/RDS. Update the `DATABASE_URL` in `.env`:

```
DATABASE_URL=mysql://username:password@host:port/database
```
