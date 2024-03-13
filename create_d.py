from app import app, db

# Use the application context
with app.app_context():
    # Create database tables
    db.create_all()
