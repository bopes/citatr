import os
from citatr import app, db

db.reset_db()
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)