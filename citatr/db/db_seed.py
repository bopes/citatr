import os
import sys
citatr_dir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(citatr_dir)
from citatr import app, get_db
import bcrypt
import seeds

db = get_db()
with app.open_resource('db/schema.sql', mode='r') as f:
  db.cursor().executescript(f.read())

# Add seeds
for user in seeds.users:
  u = user[0]
  pw = bcrypt.hashpw(bytes(user[1], 'utf-8'), bcrypt.gensalt())
  db.execute('INSERT INTO users (username, password) values (?, ?)', [u,pw])
db.commit()
# Display seed counts
user_count = db.execute("SELECT COUNT(*) FROM users;").fetchone()[0]
print("%i seed user(s) added." % user_count)

print("Seed complete.")