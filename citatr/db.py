import os
import sqlite3
import bcrypt
from flask import g
from citatr import app
from citatr.database import seeds

# Create database connection
def connect_db():
  rv = sqlite3.connect(app.config['DATABASE'])
  rv.row_factory = sqlite3.Row
  return rv

# Open database connection
def get_db():
  if not hasattr(g, 'sqlite_db'):
    g.sqlite_db = connect_db()
  return g.sqlite_db

# Initialize database
def init_db():
  db = get_db()
  if not os.path.isfile(app.config['DATABASE']) or app.config['TESTING']:
    with app.open_resource('database/schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()
  if not app.config['TESTING']:
    print(" * Database initialized.")

# Close database connection
@app.teardown_appcontext
def close_db(error):
  if hasattr(g, 'sqlite_db'):
    g.sqlite_db.close()

# Seed database
def seed_db():
  db = get_db()
  # Add seeds
  users_added = 0
  for user in seeds.users:
    u = user.username
    pw = bcrypt.hashpw(user.password, bcrypt.gensalt())
    db.execute('INSERT INTO users (username, password) values (?, ?)', [u,pw])
    users_added += 1
  db.commit()
  # Display seed counts
  user_count = db.execute("SELECT COUNT(*) FROM users;").fetchone()[0]
  print("%i seed user(s) added. %i user(s) total." % (users_added, user_count))
  # Complete seed
  print("Seed complete.")

# Drop database
def drop_db():
  if os.path.isfile(app.config['DATABASE']):
    os.remove(app.config['DATABASE'])
    print("Existing database deleted...")
  else:
    print("No existing database found.")

# Reset database
def reset_db():
  # if os.path.isfile(app.config['DATABASE']):
  #   confirmation = input("Database already exists. Overwrite? (Y/N)\n --> ")
  #   if confirmation not in ['Y','YES",Yes','y','yes']:
  #     print("Database initialization aborted.")
  #     return
  #   else:
  drop_db()
  init_db()
  seed_db()
