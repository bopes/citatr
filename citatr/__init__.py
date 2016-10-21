# flask imports
from flask import Flask, g
import os
import sqlite3

# create our little application :)
app = Flask(__name__)
# ctx = app.app_context()
# ctx.push()

# with ctx:
#     pass

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'citatr.db'),
    DEBUG=True,
    SECRET_KEY='2BBCFA59DC64CB1353FFC2148E634',
    USERNAME='bigep',
    PASSWORD='yankeehotelfoxtrot'
))

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
  with app.open_resource('db/schema.sql', mode='r') as f:
    db.cursor().executescript(f.read())
  db.commit()
  print('* Initialized database')

@app.cli.command('initdb')
def initdb_command():
  init_db()
  print("Database initialized")

# Close database connection
@app.teardown_appcontext
def close_db(error):
  if hasattr(g, 'sqlite_db'):
    g.sqlite_db.close()

from citatr import views