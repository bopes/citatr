import os
import sys
import bcrypt
import seeds
citatr_dir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(citatr_dir)
from citatr import get_db

db = get_db()

# Add seeds
users_added = 0
for user in seeds.users:
  u = user[0]
  pw = bcrypt.hashpw(bytes(user[1], 'utf-8'), bcrypt.gensalt())
  db.execute('INSERT INTO users (username, password) values (?, ?)', [u,pw])
  users_added += 1
db.commit()
# Display seed counts
user_count = db.execute("SELECT COUNT(*) FROM users;").fetchone()[0]
print("%i seed user(s) added. %i user(s) total." % (users_added, user_count))

print("Seed complete.")