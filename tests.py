import os
import citatr
import unittest
import tempfile

import flask

test_citation = "903 So. 2d 913\r\nSupreme Court of Florida\r\nCRESCENT MIAMI CENTER, LLC, Petitioner,\r\nv.\r\nFLORIDA DEPARTMENT OF REVENUE, Respondent.\r\nNo. SC03-2063. May 19, 2005."

test_citation_result = "Crescent Miami Ctr., LLC, v. Fla. Dep't of Revenue, 903 So. 2d 913, 914-15 (Fla. 2005)."


class CitatrTestCase(unittest.TestCase):

  def setUp(self):
    citatr.app.config['TESTING'] = True
    self.app = citatr.app.test_client()

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
    query = {'input_citation': citation, 'input_pages': pages}
    return self.app.get('/convert', query_string=dict(
      input_text=citation,
      input_pages=pages))

  def test_login_logout(self):
    rv = self.get_root()
    assert b'Login' in rv.data
    rv = self.login('bigep', 'yankeehotelfoxtrot')
    assert b'Successfully logged in.' in rv.data
    rv = self.get_root()
    assert  b'Initial Westlaw Citation' in rv.data
    rv = self.logout()
    assert b'Successfully logged out.' in rv.data
    rv = self.get_root()
    assert b'Login' in rv.data
    rv = self.login('bad', 'credentials')
    assert b'Invalid credentials.' in rv.data

  def test_conversion(self):
    self.login('bigep', 'yankeehotelfoxtrot')
    rv = self.convert_citation(test_citation, '914-15')
    print(rv.data)

if __name__ == '__main__':
  unittest.main()