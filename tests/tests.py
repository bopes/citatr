import os
import sys
import unittest
import tempfile

root_path = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(root_path)

from citatr import app

# Variables

test_citation = "903 So. 2d 913\r\nSupreme Court of Florida\r\nCRESCENT MIAMI CENTER, LLC, Petitioner,\r\nv.\r\nFLORIDA DEPARTMENT OF REVENUE, Respondent.\r\nNo. SC03-2063. May 19, 2005."

test_citation_result = b"Crescent Miami Ctr., LLC, v. Fla. Dep't of Revenue, 903 So. 2d 913, 914-15 (Fla. 2005)."


class CitatrTestCase(unittest.TestCase):

  # Set up methods



  def setUp(self):
    app.config['TESTING'] = True
    self.app = app.test_client()

  def get_root(self):
    return self.app.get('/', follow_redirects=True)

  def login(self, username, password):
    return self.app.post('/login', data=dict(
      username=username,
      password=password
      ), follow_redirects=True)

  def logout(self):
    return self.app.get('/logout', follow_redirects=True)

  def convert_citation(self, citation, pages):
    return self.app.post('/convert', data=dict(
      input_text=citation,
      input_pages=pages
      ), follow_redirects=True)


  # Tests

  def test_login_logout(self):
    # Access root while not logged in
    rv = self.get_root()
    assert b'Login' in rv.data
    # Access /index while logged in
    rv = self.login('bigep', 'yankeehotelfoxtrot')
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
    self.login('bigep', 'yankeehotelfoxtrot')
    rv = self.convert_citation(test_citation, '914-15')
    assert test_citation_result in rv.data

if __name__ == '__main__':
  unittest.main()