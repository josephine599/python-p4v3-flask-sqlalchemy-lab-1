#!/usr/bin/env python3
# server/seed.py
#!/usr/bin/env python3
from app import app
from models import db, Earthquake

with app.app_context():
    # Clear existing data
    Earthquake.query.delete()

    # Add earthquakes exactly matching the tests
    db.session.add(Earthquake(magnitude=9.5, location="Chile", year=1960))  # id 1
    db.session.add(Earthquake(magnitude=9.2, location="Alaska", year=1964)) # id 2
    db.session.add(Earthquake(magnitude=8.6, location="Alaska", year=1946)) # id 3
    db.session.add(Earthquake(magnitude=8.5, location="Banda Sea", year=1934)) # id 4
    db.session.add(Earthquake(magnitude=8.4, location="Chile", year=1922)) # id 5

    db.session.commit()
