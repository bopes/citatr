import os
import sys
import unittest
import tempfile

root_path = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(root_path)

from citatr import app, db

# Variables

test_citation = "903 So. 2d 913\r\nSupreme Court of Florida\r\nCRESCENT MIAMI CENTER, LLC, Petitioner,\r\nv.\r\nFLORIDA DEPARTMENT OF REVENUE, Respondent.\r\nNo. SC03-2063. May 19, 2005."

test_citation_result = b"Crescent Miami Ctr., LLC, v. Fla. Dep't of Revenue, 903 So. 2d 913, 914-15 (Fla. 2005)."


class CitatrTestCase(unittest.TestCase):

  # Set up methods

  def setUp(self):
    self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    self.app = app.test_client()
    with app.app_context():
      db.init_db()

  def get_root(self):
    return self.app.get('/', follow_redirects=True)

  def get_signup(self):
    return self.app.get('/signup')

  def signup(self, username, password, password_cnf):
    return self.app.post('/signup', data=dict(
      username=username,
      password=password,
      password_cnf=password_cnf
      ), follow_redirects=True)

  def get_login(self):
    return self.app.get('login', follow_redirects=True)

  def login(self, username, password):
    return self.app.post('/login', data=dict(
      username=username,
      password=password
      ), follow_redirects=True)

  def valid_login(self):
    self.signup('test','password','password')
    self.login('test','password')

  def logout(self):
    return self.app.get('/logout', follow_redirects=True)

  def convert_citation(self, citation, pages):
    return self.app.post('/convert', data=dict(
      input_text=citation,
      input_pages=pages
      ), follow_redirects=True)



  # Tests

  def test_signup_login_logout(self):
    # Access root while not logged in
    rv = self.get_root()
    assert b'Login' in rv.data
    # Access signup pafe
    rv = self.get_signup()
    assert b'Create New Account' in rv.data
    # Sign up with blank fields
    rv = self.signup('','','')
    assert b'All values must be filled.' in rv.data
    # Sign up with invalid password
    rv = self.signup('test','invalid','password')
    assert b'Password and password confirmation must match.' in rv.data
    # Sign up with valid password
    rv = self.signup('test','password','password')
    assert b'Account created.' in rv.data
    # Access /index while logged in
    rv = self.login('test', 'password')
    assert b'Initial Westlaw Citation' in rv.data
    # Access root while logged in
    rv = self.get_root()
    assert  b'Initial Westlaw Citation' in rv.data
    # Access /login while logged out
    rv = self.logout()
    assert b'Account logged out.' in rv.data
    # Access root after logging out
    rv = self.get_root()
    assert b'Login' in rv.data
    # Attempt login with invalid credentials
    rv = self.login('bad', 'credentials')
    assert b'Invalid credentials.' in rv.data

  def test_conversion(self):
    # Convert while not logged in
    rv = self.convert_citation(test_citation, '914-15')
    assert b'401 Unauthorized' in rv.data
    assert test_citation_result not in rv.data
    # Convert while logged in
    self.valid_login()
    self.login('bigep', 'yankeehotelfoxtrot')
    rv = self.convert_citation(test_citation, '914-15')
    assert test_citation_result in rv.data

if __name__ == '__main__':
  unittest.main()