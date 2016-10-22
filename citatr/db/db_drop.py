import os

current_dir = os.path.dirname(__file__)
db_dir = os.path.join(current_dir, "..")
db_file = os.path.join(db_dir, 'citatr.db')

os.remove(db_file)
print("Existing database deleted...")