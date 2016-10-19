# flask imports
from flask import Flask

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='bigep',
    PASSWORD='yankeehotelfoxtrot'
))

from citatr import views