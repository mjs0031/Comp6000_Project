""" Python Package Support """
# Not applicable

""" Django Package Support """
# Not applicable

""" Internal Package Support """
from Data_Base.models import Business

"""
 Data_Base/Data/Imports/business_import.py
 Author:      Matthew J Swann; Yong Kin; Bradon Atkins; Adam Carter
 Version:     1.0
 Last Update: 2013-03-22
 Update By:   Matthew J Swann
 
 
 Importing data to the business table.

 """
 
class BusinessImport(object):
     
    def __init__(self, scriptName=None):
        
        #  1
        Business.objects.create(
            name                 = 'Medtech Products Inc.',
            address_line_one     = '431 W. End Ave.',
            address_line_two     = '',
            city                 = 'Tarrytown',
            state                = 'NY',
            zip_code             = '10591',
            phone                = '212-357-1250',
            notes                = '',     
            business_description = 'First business in database.'              
                )

        #  2
        Business.objects.create(
            name                 = 'Anheuser-Busch',
            address_line_one     = '1 Beer Road',
            address_line_two     = '',
            city                 = 'St. Louis',
            state                = 'MO',
            zip_code             = '',
            phone                = '',
            notes                = '',     
            business_description = 'Second business in database.'              
                )
        
        #  3
        Business.objects.create(
            name                 = 'Jade Garden',
            address_line_one     = '707 King Street',
            address_line_two     = '',
            city                 = 'Seattle',
            state                = 'WA', 
            zip_code             = '98144',
            phone                = '',
            notes                = '',     
            business_description = 'Third business in database.'              
                )
        
        #  4
        Business.objects.create(
            name                 = 'Knollgrass',
            address_line_one     = '15 W. New York Ave',
            address_line_two     = '',
            city                 = 'Washington',
            state                = 'DC',
            zip_code             = '01002',
            phone                = '',
            notes                = '',     
            business_description = 'Fourth business in database.'              
                )
        
        #  5
        Business.objects.create(
            name                 = 'Xmera Core',
            address_line_one     = '345 W. Magnolia Avenue',
            address_line_two     = '3rd Floor, Rm 3139A',
            city                 = 'Auburn',
            state                = 'AL',
            zip_code             = '36849',
            phone                = '',
            notes                = '',     
            business_description = 'Does not exist.'              
                )
        
        #  6
        Business.objects.create(
            name                 = 'Set Depo',
            address_line_one     = '405 Lexington Ave',
            address_line_two     = '38th Floor',
            city                 = 'New York',
            state                = 'NY',
            zip_code             = '10010',
            phone                = '800-451-3376',
            notes                = '',     
            business_description = 'Sixth business in database.'              
                )
        
        #  7
        Business.objects.create(
            name                 = 'Primo Pizza',
            address_line_one     = '1587 Black Rock Turnpike',
            address_line_two     = '',
            city                 = 'Fairfield',
            state                = 'CT',
            zip_code             = '06824',
            phone                = '800-945-5687',
            notes                = '',     
            business_description = 'Seventh business in database.'              
                )

        #  8
        Business.objects.create(
            name                 = 'Rosenblum Newfield, LLC',
            address_line_one     = '405 Lexington Avenue',
            address_line_two     = '39th Floor',
            city                 = 'New York',
            state                = 'NY',
            zip_code             = '10010',
            phone                = '212-358-9200',
            notes                = '',     
            business_description = 'Eighth business in database.'              
                )
        
        #  9
        Business.objects.create(
            name                 = 'Kraft Foods',
            address_line_one     = '1 Kraft Court',
            address_line_two     = '',
            city                 = 'Glenview',
            state                = 'IL',
            zip_code             = '60025',
            phone                = '877-535-5666',
            notes                = '',     
            business_description = 'Ninth business in database.'              
                )
        
        # 10
        Business.objects.create(
            name                 = 'Oskar Blues Brewery',
            address_line_one     = '1800 Pike Road',
            address_line_two     = 'Unit B',
            city                 = 'Longmont',
            state                = 'CO',
            zip_code             = '80501',
            phone                = '303-776-1914',
            notes                = '',     
            business_description = 'Tenth business in database.'              
                )