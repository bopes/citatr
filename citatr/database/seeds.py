class User:
  def __init__(self,username,password):
    self.username = username
    self.password = password.encode('UTF-8','strict')

users = [
  User('bigep','yankeehotelfoxtrot')
]