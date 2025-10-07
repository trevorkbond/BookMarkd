# BookMarkd
BookMarkd is an all-in-one book enjoyer's website. This app is much like Letterboxd but for books. Rate books, share books with friends, receive book recommendations, join online book clubs, or set personal reading goals are some of BookMarkd's features.

## Project Structure

```
BookMarkd/
├── backend/          # Flask REST API
├── frontend/         # React application
└── README.md         # This file
```

## Tech Stack

- **Frontend**: React
- **Backend**: Flask (Python)
- **Database**: MySQL/RDS

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js 14+
- MySQL

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

5. Initialize the database:
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

6. Start the backend server:
```bash
python app.py
```

The API will be running at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env if needed (default points to http://localhost:5000)
```

4. Start the development server:
```bash
npm start
```

The application will be running at `http://localhost:3000`

## API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/books` - Get all books

## Database Configuration

The application uses MySQL. Update the `DATABASE_URL` in `backend/.env`:

```
DATABASE_URL=mysql://username:password@host:port/database
```

For AWS RDS, use the RDS endpoint:
```
DATABASE_URL=mysql://username:password@your-rds-endpoint.region.rds.amazonaws.com:3306/database
```

## Development

- Backend runs on port 5000
- Frontend runs on port 3000
- CORS is enabled for local development

## License

MIT License - see LICENSE file for details

