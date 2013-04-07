""" Python Package Support """
# Not applicable

""" Django Package Support """
# Not applicable

""" Internal Package Support """
from Data_Base.models import School, Person, Child

"""
 Data_Base/Data/Imports/child_import.py
 
 Author:      Matthew J Swann; 
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-07
 Update By:   Matthew J Swann
 
 Importing data to the person table.

 """
 
class ChildImport(object):
     
    def __init__(self, scriptName=None):
        
        #  1
        x = Child.objects.create(
            first_name           = 'Timmy',
            last_name            = 'Thompson',
            school               = School.objects.get(pk=1),                    
                )
        x.family.add(Person.objects.get(pk=1))
        x.family.add(Person.objects.get(pk=2))
        x.save()

        #  2
        x = Child.objects.create(
            first_name           = 'Jimmy',
            last_name            = 'Johnson',
            school               = School.objects.get(pk=2),                    
                )
        x.family.add(Person.objects.get(pk=2))
        x.family.add(Person.objects.get(pk=1))
        x.save()
        
        #  3
        x = Child.objects.create(
            first_name           = 'Bart',
            last_name            = 'Simpson',
            school               = School.objects.get(pk=3),                    
                )
        x.family.add(Person.objects.get(pk=3))
        x.family.add(Person.objects.get(pk=4))
        x.save()
        
        #  4
        x = Child.objects.create(
            first_name           = 'Lisa',
            last_name            = 'Simpson',
            school               = School.objects.get(pk=4),                    
                )
        x.family.add(Person.objects.get(pk=4))
        x.family.add(Person.objects.get(pk=3))
        x.save()
        
        #  5
        x = Child.objects.create(
            first_name           = 'Andrew',
            last_name            = 'Becker',
            school               = School.objects.get(pk=5),                    
                )
        x.family.add(Person.objects.get(pk=5))
        x.family.add(Person.objects.get(pk=6))
        x.save()
        
        #  6
        x = Child.objects.create(
            first_name           = 'Jasmine',
            last_name            = 'Goulette',
            school               = School.objects.get(pk=6),                    
                )
        x.family.add(Person.objects.get(pk=6))
        x.family.add(Person.objects.get(pk=5))
        x.save()
        
        #  7
        x = Child.objects.create(
            first_name           = 'Kristina',
            last_name            = 'Murry',
            school               = School.objects.get(pk=7),                    
                )
        x.family.add(Person.objects.get(pk=7))
        x.family.add(Person.objects.get(pk=8))
        x.save()

        #  8
        x = Child.objects.create(
            first_name           = 'Andrew',
            last_name            = 'Scheonster',
            school               = School.objects.get(pk=8),                    
                )
        x.family.add(Person.objects.get(pk=8))
        x.family.add(Person.objects.get(pk=7))
        x.save()
