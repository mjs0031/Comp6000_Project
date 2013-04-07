""" Python Package Imports """
# Not Applicable

""" Django Package Imports """
from django.test import TestCase
from django.core.exceptions import ValidationError

""" Internal Package Imports """
from Data_Base.models import (Business, School, Person, Child)

"""

 Data_base/tests.py

 Author:      Matthew J Swann; 
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-07
 Update By:   Matthew J Swann
 
 Code for the database unittesting.
 
 Fixtures imported will be included in Control Package.

 """
 
class Test(TestCase):
    fixtures = ['Control/fixtures/json/database_testdata.json']
    
    """
     {
      BUSINESS BLOCK
     }
     """
    def test_busiess_10_01_00_import(self):
        x = Business.objects.get(pk=1)
        self.assertEquals(x.name, 'Medtech Products Inc.')
        self.assertEquals(x.address_line_one, '431 W. End Ave.')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Tarrytown')
        self.assertEquals(x.state, 'NY')
        self.assertEquals(x.zip_code, '10591')
        self.assertEquals(x.phone, '212-357-1250')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'First business in database.')
        
        x = Business.objects.get(pk=2)
        self.assertEquals(x.name, 'Anheuser-Busch')
        self.assertEquals(x.address_line_one, '1 Beer Road')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'St. Louis')
        self.assertEquals(x.state, 'MO')
        self.assertEquals(x.zip_code, '')
        self.assertEquals(x.phone, '')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Second business in database.')
        
        x = Business.objects.get(pk=3)
        self.assertEquals(x.name, 'Jade Garden')
        self.assertEquals(x.address_line_one, '707 King Street')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Seattle')
        self.assertEquals(x.state, 'WA')
        self.assertEquals(x.zip_code, '98144')
        self.assertEquals(x.phone, '')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Third business in database.')
        
        x = Business.objects.get(pk=4)
        self.assertEquals(x.name, 'Knollgrass')
        self.assertEquals(x.address_line_one, '15 W. New York Ave')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Washington')
        self.assertEquals(x.state, 'DC')
        self.assertEquals(x.zip_code, '01002')
        self.assertEquals(x.phone, '')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Fourth business in database.')
        
        x = Business.objects.get(pk=5)
        self.assertEquals(x.name, 'Xmera Core')
        self.assertEquals(x.address_line_one, '345 W. Magnolia Avenue')
        self.assertEquals(x.address_line_two, '3rd Floor, Rm 3139A')
        self.assertEquals(x.city, 'Auburn')
        self.assertEquals(x.state, 'AL')
        self.assertEquals(x.zip_code, '36849')
        self.assertEquals(x.phone, '')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Does not exist.')
        
        x = Business.objects.get(pk=6)
        self.assertEquals(x.name, 'Set Depo')
        self.assertEquals(x.address_line_one, '405 Lexington Ave')
        self.assertEquals(x.address_line_two, '38th Floor')
        self.assertEquals(x.city, 'New York')
        self.assertEquals(x.state, 'NY')
        self.assertEquals(x.zip_code, '10010')
        self.assertEquals(x.phone, '800-451-3376')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Sixth business in database.')

        x = Business.objects.get(pk=7)
        self.assertEquals(x.name, 'Primo Pizza')
        self.assertEquals(x.address_line_one, '1587 Black Rock Turnpike')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Fairfield')
        self.assertEquals(x.state, 'CT')
        self.assertEquals(x.zip_code, '06824')
        self.assertEquals(x.phone, '800-945-5687')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Seventh business in database.')
        
        x = Business.objects.get(pk=8)
        self.assertEquals(x.name, 'Rosenblum Newfield, LLC')
        self.assertEquals(str(x.address_line_one), '405 Lexington Avenue')
        self.assertEquals(x.address_line_two, '39th Floor')
        self.assertEquals(x.city, 'New York')
        self.assertEquals(x.state, 'NY')
        self.assertEquals(x.zip_code, '10010')
        self.assertEquals(x.phone, '212-358-9200')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Eighth business in database.')
        
        x = Business.objects.get(pk=9)
        self.assertEquals(x.name, 'Kraft Foods')
        self.assertEquals(x.address_line_one, '1 Kraft Court')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Glenview')
        self.assertEquals(x.state, 'IL')
        self.assertEquals(x.zip_code, '60025')
        self.assertEquals(x.phone, '877-535-5666')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Ninth business in database.')
        
        x = Business.objects.get(pk=10)
        self.assertEquals(x.name, 'Oskar Blues Brewery')
        self.assertEquals(x.address_line_one, '1800 Pike Road')
        self.assertEquals(x.address_line_two, 'Unit B')
        self.assertEquals(x.city, 'Longmont')
        self.assertEquals(x.state, 'CO')
        self.assertEquals(x.zip_code, '80501')
        self.assertEquals(x.phone, '303-776-1914')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.business_description, 'Tenth business in database.')

    """
     {
      SCHOOL BLOCK
     }
     """
    def test_school_10_01_00_import(self):
        x = School.objects.get(pk=1)
        self.assertEquals(x.name, 'Auburn University')
        self.assertEquals(x.address_line_one, '345 W. Magnolia Ave')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Auburn University')
        self.assertEquals(x.state, 'AL')
        self.assertEquals(x.zip_code, '36849')
        self.assertEquals(x.phone, '334-844-1000')
        self.assertEquals(x.notes, 'Rival :: Bama')
        self.assertEquals(x.education_level, 'C')
        
        x = School.objects.get(pk=2)
        self.assertEquals(x.name, 'Loyola University Chicago')
        self.assertEquals(x.address_line_one, '6122 N. Sheridan Road')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Chicago')
        self.assertEquals(x.state, 'IL')
        self.assertEquals(x.zip_code, '60626')
        self.assertEquals(x.phone, '773-508-2350')
        self.assertEquals(x.notes, 'Jesuit')
        self.assertEquals(x.education_level, 'C')
        
        x = School.objects.get(pk=3)
        self.assertEquals(x.name, 'Auburn Vet School')
        self.assertEquals(x.address_line_one, '1000 Wire Road')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Auburn')
        self.assertEquals(x.state, 'AL')
        self.assertEquals(x.zip_code, '36832')
        self.assertEquals(x.phone, '334-844-2277')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.education_level, 'C')
        
        x = School.objects.get(pk=4)
        self.assertEquals(x.name, 'Auburn High School')
        self.assertEquals(x.address_line_one, '15 Main Street')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Auburn')
        self.assertEquals(x.state, 'AL')
        self.assertEquals(x.zip_code, '36832')
        self.assertEquals(x.phone, '334-844-0001')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.education_level, 'S')
        
        x = School.objects.get(pk=5)
        self.assertEquals(x.name, 'Boston University')
        self.assertEquals(x.address_line_one, 'One Silber Way')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Boston')
        self.assertEquals(x.state, 'MA')
        self.assertEquals(x.zip_code, '02215')
        self.assertEquals(x.phone, '617-353-2000')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.education_level, 'C')
        
        x = School.objects.get(pk=6)
        self.assertEquals(x.name, 'LSU')
        self.assertEquals(x.address_line_one, '3960 West Lakeshore Dr')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Baton Rouge')
        self.assertEquals(x.state, 'LA')
        self.assertEquals(x.zip_code, '70808')
        self.assertEquals(x.phone, '887-670-4521')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.education_level, 'C')
        
        x = School.objects.get(pk=7)
        self.assertEquals(x.name, 'American Military University')
        self.assertEquals(x.address_line_one, '111 West Congress Street')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Charles Town')
        self.assertEquals(x.state, 'WV')
        self.assertEquals(x.zip_code, '25414')
        self.assertEquals(x.phone, '312-263-0456')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.education_level, 'C')
        
        x = School.objects.get(pk=8)
        self.assertEquals(x.name, 'Opelika High School')
        self.assertEquals(x.address_line_one, '1700 Laffayette Pkwy')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Opelika')
        self.assertEquals(x.state, 'AL')
        self.assertEquals(x.zip_code, '36801')
        self.assertEquals(x.phone, '334-844-0002')
        self.assertEquals(x.notes, '')
        self.assertEquals(x.education_level, 'S')
        

    """
     {
      PERSON BLOCK
     }
     """
    def test_person_10_01_00_import(self):
        x = Person.objects.get(pk=1)
        self.assertEquals(x.first_name, 'John')
        self.assertEquals(x.last_name, 'Wayne')
        self.assertEquals(x.business, Business.objects.get(pk=1))
        self.assertEquals(x.address_line_one, '123 Cowboy Street')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Houston')
        self.assertEquals(x.state, 'TX')
        self.assertEquals(x.zip_code, '21568')
        
        x = Person.objects.get(pk=2)
        self.assertEquals(x.first_name, 'Bruce')
        self.assertEquals(x.last_name, 'Wayne')
        self.assertEquals(x.business, Business.objects.get(pk=2))
        self.assertEquals(x.address_line_one, '405 Lexington Ave')
        self.assertEquals(x.address_line_two, '40th Floor')
        self.assertEquals(x.city, 'Gotham')
        self.assertEquals(x.state, 'NY')
        self.assertEquals(x.zip_code, '10010')
        
        x = Person.objects.get(pk=3)
        self.assertEquals(x.first_name, 'Sally')
        self.assertEquals(x.last_name, 'Smith')
        self.assertEquals(x.business, Business.objects.get(pk=3))
        self.assertEquals(x.address_line_one, '345 E. Main')
        self.assertEquals(x.address_line_two, 'Apt. 6')
        self.assertEquals(x.city, 'Chicago')
        self.assertEquals(x.state, 'IL')
        self.assertEquals(x.zip_code, '60625')
        
        x = Person.objects.get(pk=4)
        self.assertEquals(x.first_name, 'Gene')
        self.assertEquals(x.last_name, 'Henderson')
        self.assertEquals(x.business, Business.objects.get(pk=4))
        self.assertEquals(x.address_line_one, '55 Francesca Place')
        self.assertEquals(x.address_line_two, 'Unit 4C')
        self.assertEquals(x.city, 'Queens')
        self.assertEquals(x.state, 'NY')
        self.assertEquals(x.zip_code, '17563')
        
        x = Person.objects.get(pk=5)
        self.assertEquals(x.first_name, 'Melissa')
        self.assertEquals(x.last_name, 'Barcroft')
        self.assertEquals(x.business, Business.objects.get(pk=5))
        self.assertEquals(x.address_line_one, '45 Linda Street')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Pasco')
        self.assertEquals(x.state, 'WA')
        self.assertEquals(x.zip_code, '98235')
        
        x = Person.objects.get(pk=6)
        self.assertEquals(x.first_name, 'Matthew')
        self.assertEquals(x.last_name, 'Swann')
        self.assertEquals(x.business, None)
        self.assertEquals(x.address_line_one, '1877 Bellwood Place')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Auburn')
        self.assertEquals(x.state, 'AL')
        self.assertEquals(x.zip_code, '36832')
        
        x = Person.objects.get(pk=7)
        self.assertEquals(x.first_name, 'Michael')
        self.assertEquals(x.last_name, 'Swann')
        self.assertEquals(x.business, Business.objects.get(pk=7))
        self.assertEquals(x.address_line_one, '14 Charles Street')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Boston')
        self.assertEquals(x.state, 'MA')
        self.assertEquals(x.zip_code, '02238')
        
        x = Person.objects.get(pk=8)
        self.assertEquals(x.first_name, 'Joshua')
        self.assertEquals(x.last_name, 'Kiser')
        self.assertEquals(x.business, Business.objects.get(pk=8))
        self.assertEquals(x.address_line_one, '108 Route 508')
        self.assertEquals(x.address_line_two, '')
        self.assertEquals(x.city, 'Alexandria')
        self.assertEquals(x.state, 'OH')
        self.assertEquals(x.zip_code, '45236')
        
        
    """
     {
      CHILD BLOCK
     }
     """
    def test_child_10_01_00_import(self):
        one   = Person.objects.get(pk=1)
        two   = Person.objects.get(pk=2)
        three = Person.objects.get(pk=3)
        four  = Person.objects.get(pk=4)
        five  = Person.objects.get(pk=5)
        six   = Person.objects.get(pk=6)
        seven = Person.objects.get(pk=7)
        eight = Person.objects.get(pk=8)
        
        x = Child.objects.get(pk=1)
        r = x.family.all()
        self.assertEquals(x.first_name, 'Timmy')
        self.assertEquals(x.last_name, 'Thompson')
        self.assertEquals((one   in r), True)
        self.assertEquals((two   in r), True)
        self.assertEquals((three in r), False)
        self.assertEquals((four  in r), False)
        self.assertEquals((five  in r), False)
        self.assertEquals((six   in r), False)
        self.assertEquals((seven in r), False)
        self.assertEquals((eight in r), False)
        self.assertEquals(x.school, School.objects.get(pk=1))
        
        x = Child.objects.get(pk=2)
        r = x.family.all()
        self.assertEquals(x.first_name, 'Jimmy')
        self.assertEquals(x.last_name, 'Johnson')
        self.assertEquals((one   in r), True)
        self.assertEquals((two   in r), True)
        self.assertEquals((three in r), False)
        self.assertEquals((four  in r), False)
        self.assertEquals((five  in r), False)
        self.assertEquals((six   in r), False)
        self.assertEquals((seven in r), False)
        self.assertEquals((eight in r), False)
        self.assertEquals(x.school, School.objects.get(pk=2))
        
        x = Child.objects.get(pk=3)
        r = x.family.all()
        self.assertEquals(x.first_name, 'Bart')
        self.assertEquals(x.last_name, 'Simpson')
        self.assertEquals((one   in r), False)
        self.assertEquals((two   in r), False)
        self.assertEquals((three in r), True)
        self.assertEquals((four  in r), True)
        self.assertEquals((five  in r), False)
        self.assertEquals((six   in r), False)
        self.assertEquals((seven in r), False)
        self.assertEquals((eight in r), False)
        self.assertEquals(x.school, School.objects.get(pk=3))
        
        x = Child.objects.get(pk=4)
        r = x.family.all()
        self.assertEquals(x.first_name, 'Lisa')
        self.assertEquals(x.last_name, 'Simpson')
        self.assertEquals((one   in r), False)
        self.assertEquals((two   in r), False)
        self.assertEquals((three in r), True)
        self.assertEquals((four  in r), True)
        self.assertEquals((five  in r), False)
        self.assertEquals((six   in r), False)
        self.assertEquals((seven in r), False)
        self.assertEquals((eight in r), False)    
        self.assertEquals(x.school, School.objects.get(pk=4))
        
        x = Child.objects.get(pk=5)
        r = x.family.all()
        self.assertEquals(x.first_name, 'Andrew')
        self.assertEquals(x.last_name, 'Becker')
        self.assertEquals((one   in r), False)
        self.assertEquals((two   in r), False)
        self.assertEquals((three in r), False)
        self.assertEquals((four  in r), False)
        self.assertEquals((five  in r), True)
        self.assertEquals((six   in r), True)
        self.assertEquals((seven in r), False)
        self.assertEquals((eight in r), False)    
        self.assertEquals(x.school, School.objects.get(pk=5))
        
        x = Child.objects.get(pk=6)
        r = x.family.all()
        self.assertEquals(x.first_name, 'Jasmine')
        self.assertEquals(x.last_name, 'Goulette')
        self.assertEquals((one   in r), False)
        self.assertEquals((two   in r), False)
        self.assertEquals((three in r), False)
        self.assertEquals((four  in r), False)
        self.assertEquals((five  in r), True)
        self.assertEquals((six   in r), True)
        self.assertEquals((seven in r), False)
        self.assertEquals((eight in r), False)    
        self.assertEquals(x.school, School.objects.get(pk=6))
        
        x = Child.objects.get(pk=7)
        r = x.family.all()
        self.assertEquals(x.first_name, 'Kristina')
        self.assertEquals(x.last_name, 'Murry')
        self.assertEquals((one   in r), False)
        self.assertEquals((two   in r), False)
        self.assertEquals((three in r), False)
        self.assertEquals((four  in r), False)
        self.assertEquals((five  in r), False)
        self.assertEquals((six   in r), False)
        self.assertEquals((seven in r), True)
        self.assertEquals((eight in r), True)    
        self.assertEquals(x.school, School.objects.get(pk=7))
        
        x = Child.objects.get(pk=8)
        r = x.family.all()
        self.assertEquals(x.first_name, 'Andrew')
        self.assertEquals(x.last_name, 'Scheonster')
        self.assertEquals((one   in r), False)
        self.assertEquals((two   in r), False)
        self.assertEquals((three in r), False)
        self.assertEquals((four  in r), False)
        self.assertEquals((five  in r), False)
        self.assertEquals((six   in r), False)
        self.assertEquals((seven in r), True)
        self.assertEquals((eight in r), True)    
        self.assertEquals(x.school, School.objects.get(pk=8))