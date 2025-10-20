from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql://user:password@localhost/bookmarkd')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'BookMarkd API is running'
    })

@app.route('/api/books', methods=['GET'])
def get_books():
    """Get all books endpoint"""
    # TODO: Implement database query
    return jsonify({
        'books': []
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
