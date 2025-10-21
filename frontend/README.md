# BookMarkd Frontend

React-based frontend for BookMarkd application.

## Setup

1. Install dependencies:

```bash
npm install
```

2. Configure environment variables:

```bash
cp .env.example .env
# Edit .env with your API URL
```

3. Run the development server:

```bash
npm start
```

The application will be available at `http://localhost:3000`

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm build` - Builds the app for production
- `npm test` - Runs the test suite

## Configuration

Update the `REACT_APP_API_URL` in `.env` to point to your backend API:

```
REACT_APP_API_URL=http://localhost:5001
```
