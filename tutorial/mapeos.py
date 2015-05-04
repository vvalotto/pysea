from tutorial import *
from sqlalchemy.orm import *

class User(object):
    pass

class Group(object):
    pass

class Permission(object):
    pass

mapper(User, user_table)
mapper(Group, group_table)
mapper(Permission, permission_table)

Session = sessionmaker()
session = Session()

query = session.query(User)
print(list(query))

for user in query:
    print(user.user_name)

nuevo_usuario = User()
nuevo_usuario.user_name = 'Mike'
nuevo_usuario.password = 'password'
session.add(nuevo_usuario)

print(query.count())
session.commit()