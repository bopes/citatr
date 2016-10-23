# flask imports
import os
from flask import Flask

# create our little application :)
app = Flask(__name__)
ctx = app.app_context()
ctx.push()
with ctx:
    pass

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'citatr.db'),
    DEBUG=True,
    SECRET_KEY='2BBCFA59DC64CB1353FFC2148E634',
    USERNAME='bigep',
    PASSWORD='yankeehotelfoxtrot'
))

from citatr import views