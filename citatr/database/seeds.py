class User:
  def __init__(self,username,password):
    self.username = username
    self.password = bytes(password, 'utf-8')

users = [
  User('bigep','yankeehotelfoxtrot')
]