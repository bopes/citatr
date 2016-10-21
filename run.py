import os
from citatr import app, init_db

db_loc = os.path.join(app.root_path, 'citatr.db')
if not os.path.isfile(db_loc):
  init_db()

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)