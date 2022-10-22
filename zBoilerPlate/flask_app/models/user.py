from flask_app.config.mysqlDB import connect
from pprint import pprint
mydb = 'flaskposts'

class User:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']


  @classmethod
  def getAll(cls):
    query = '''
      SELECT * 
      FROM users;'''
    things = connect(mydb).query_db(query)
    print(things)
    output = []
    for stuff in things:
      output.append(cls(stuff))
    pprint(output)
    return output