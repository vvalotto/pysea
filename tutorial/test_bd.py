from tutorial import *

stmt = user_table.select()

#stmt.execute(user_name='rick1', password='secret', display_name='Rick Copeland Clone')

result = stmt.execute()
for registro in result:
    print(registro)

result1 = stmt.execute()
row = result1.fetchone()
print(row['user_name'])
print(row.password)
print(row.items())