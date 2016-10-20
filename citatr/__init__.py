# flask imports
from flask import Flask

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='2BBCFA59DC64CB1353FFC2148E634',
    USERNAME='bigep',
    PASSWORD='yankeehotelfoxtrot'
))

from citatr import views