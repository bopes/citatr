import os
from citatr import app


root_dir = os.path.abspath(os.path.dirname(__file__))

# Debug key
SECRET_KEY='2BBCFA59DC64CB1353FFC2148E634'

# Admin login
USERNAME='bigep'
PASSWORD='yankeehotelfoxtrot'

# DB Config
DATABASE=os.path.join(root_dir, 'db/citatr.db'),