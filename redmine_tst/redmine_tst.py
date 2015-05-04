from redmine import Redmine

redmine = Redmine('http://leycem.fi.uner.edu.ar/redmine', key='93bf3a7ef6f2af8acfcdedb2f036adbb74775853')

proyecto = redmine.project.get('proyint-003')

print(proyecto.id)

print(proyecto.identifier)
