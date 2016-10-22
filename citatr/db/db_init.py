import os

current_dir = os.path.dirname(__file__)
db_dir = os.path.join(current_dir, "..")
db_file = os.path.join(db_dir, 'citatr.db')

def run_init_db():
  import sys
  citatr_dir = os.path.join(current_dir, "../..")
  sys.path.append(citatr_dir)
  from citatr import init_db
  init_db()

if os.path.isfile(db_file):
  confirmation = input("Database already exists. Overwrite? (Y/N)\n --> ")
  if confirmation in ['Y','YES",Yes','y','yes']:
    os.remove(db_file)
    print("Existing database deleted...")
    run_init_db()
    print("Database initialized.")
  else:
    print("Database initialization aborted.")
else:
  run_init_db()