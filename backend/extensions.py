from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Declaring here avoids circular imports
db = SQLAlchemy()
jwt = JWTManager()
