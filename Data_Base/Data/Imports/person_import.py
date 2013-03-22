""" Python Package Support """
# Not applicable

""" Django Package Support """
# Not applicable

""" Internal Package Support """
from Data_Base.models import Business, Person

"""
 Data_Base/Data/Imports/person_import.py
 Author:      Matthew J Swann; Yong Kin; Bradon Atkins; Adam Carter
 Version:     1.0
 Last Update: 2013-03-22
 Update By:   Matthew J Swann
 
 
 Importing data to the person table.

 """
 
class PersonImport(object):
     
    def __init__(self, scriptName=None):
        
        #  1
        Person.objects.create(
            first_name           = 'John',
            last_name            = 'Wayne',
            business             = Business.objects.get(pk=1),            
            address_line_one     = '123 Cowboy Street',
            address_line_two     = '',
            city                 = 'Houston',
            state                = 'TX',
            zip_code             = '21568'          
                )

        #  2
        Person.objects.create(
            first_name           = 'Bruce',
            last_name            = 'Wayne',
            business             = Business.objects.get(pk=2),            
            address_line_one     = '405 Lexington Ave',
            address_line_two     = '40th Floor',
            city                 = 'Gotham',
            state                = 'NY',
            zip_code             = '10010'           
                )
        
        #  3
        Person.objects.create(
            first_name           = 'Sally',
            last_name            = 'Smith',
            business             = Business.objects.get(pk=3),            
            address_line_one     = '345 E. Main',
            address_line_two     = 'Apt. 6',
            city                 = 'Chicago',
            state                = 'IL',
            zip_code             = '60625'          
                )
        
        #  4
        Person.objects.create(
            first_name           = 'Gene',
            last_name            = 'Henderson',
            business             = Business.objects.get(pk=4),            
            address_line_one     = '55 Francesca Place',
            address_line_two     = 'Unit 4C',
            city                 = 'Queens',
            state                = 'NY',
            zip_code             = '17563'           
                )
        
        #  5
        Person.objects.create(
            first_name           = 'Melissa',
            last_name            = 'Barcroft',
            business             = Business.objects.get(pk=5),            
            address_line_one     = '45 Linda Street',
            address_line_two     = '',
            city                 = 'Pasco',
            state                = 'WA',
            zip_code             = '98235'            
                )
        
        #  6
        Person.objects.create(
            first_name           = 'Matthew',
            last_name            = 'Swann',
            business             = None,            
            address_line_one     = '1877 Bellwood Place',
            address_line_two     = '',
            city                 = 'Auburn',
            state                = 'AL',
            zip_code             = '36832'            
                )
        
        #  7
        Person.objects.create(
            first_name           = 'Michael',
            last_name            = 'Swann',
            business             = Business.objects.get(pk=7),            
            address_line_one     = '14 Charles Street',
            address_line_two     = '',
            city                 = 'Boston',
            state                = 'MA',
            zip_code             = '02238'            
                )

        #  8
        Person.objects.create(
            first_name           = 'Joshua',
            last_name            = 'Kiser',
            business             = Business.objects.get(pk=8),            
            address_line_one     = '108 Route 508',
            address_line_two     = '',
            city                 = 'Alexandria',
            state                = 'OH',
            zip_code             = '45236'           
                )
