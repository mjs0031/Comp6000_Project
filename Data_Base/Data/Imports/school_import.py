""" Python Package Support """
# Not applicable

""" Django Package Support """
# Not applicable

""" Internal Package Support """
from Data_Base.models import School

"""
 Data_Base/Data/Imports/school_import.py
 Author:      Matthew J Swann
 Version:     1.0
 Last Update: 2013-03-20
 Update By:   Matthew J Swann
 
 
 Importing data to the school table.

 """
 
class SchoolImport(object):
     
    def __init__(self, scriptName=None):
        
        #  1
        School.objects.create(
            name                 = 'Auburn University',
            address_line_one     = '345 W. Magnolia Ave',
            address_line_two     = '',
            city                 = 'Auburn University',
            state                = 'AL',
            zip_code             = '36849',
            phone                = '334-844-1000',
            notes                = 'Rival :: Bama',     
            education_level      = 'C'              
                )

        #  2
        School.objects.create(
            name                 = 'Loyola University Chicago',
            address_line_one     = '6122 N. Sheridan Road',
            address_line_two     = '',
            city                 = 'Chicago',
            state                = 'IL',
            zip_code             = '60626',
            phone                = '773-508-2350',
            notes                = 'Jesuit',     
            education_level      = 'C'              
                )
        
        #  3
        School.objects.create(
            name                 = 'Auburn Vet School',
            address_line_one     = '1000 Wire Road',
            address_line_two     = '',
            city                 = 'Auburn',
            state                = 'AL',
            zip_code             = '36832',
            phone                = '334-844-2277',
            notes                = '',     
            education_level      = 'C'              
                )
        
        #  4
        School.objects.create(
            name                 = 'Auburn High School',
            address_line_one     = '15 Main Street',
            address_line_two     = '',
            city                 = 'Auburn',
            state                = 'AL',
            zip_code             = '36832',
            phone                = '334-844-0001',
            notes                = '',     
            education_level      = 'S'              
                )
        
        #  5
        School.objects.create(
            name                 = 'Boston University',
            address_line_one     = 'One Silber Way',
            address_line_two     = '',
            city                 = 'Boston',
            state                = 'MA',
            zip_code             = '02215',
            phone                = '617-353-2000',
            notes                = '',     
            education_level      = 'C'              
                )
        
        #  6
        School.objects.create(
            name                 = 'LSU',
            address_line_one     = '3960 West Lakeshore Dr',
            address_line_two     = '',
            city                 = 'Baton Rouge',
            state                = 'LA',
            zip_code             = '70808',
            phone                = '887-670-4521',
            notes                = '',     
            education_level      = 'C'              
                )
        
        #  7
        School.objects.create(
            name                 = 'American Military University',
            address_line_one     = '111 West Congress Street',
            address_line_two     = '',
            city                 = 'Charles Town',
            state                = 'WV',
            zip_code             = '25414',
            phone                = '312-263-0456',
            notes                = '',     
            education_level      = 'C'              
                )

        #  8
        School.objects.create(
            name                 = 'Opelika High School',
            address_line_one     = '1700 Laffayette Pkwy',
            address_line_two     = '',
            city                 = 'Opelika',
            state                = 'AL',
            zip_code             = '36801',
            phone                = '334-844-0002',
            notes                = '',     
            education_level      = 'S'              
                )
