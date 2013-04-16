""" Python Package Imports """
from datetime import datetime

""" Django Package Imports """
# Not Applicable

""" Internal Package Imports """
from Data_Base.Data.Imports.business_import import BusinessImport
from Data_Base.Data.Imports.school_import import SchoolImport
from Data_Base.Data.Imports.person_import import PersonImport
from Data_Base.Data.Imports.child_import import ChildImport

"""

 Data_Base/Data/Prime.py

 Author:      Matthew J Swann; 
              Yong Kin; 
              Bradon Atkins; and 
              Adam Carter
              
 Version:     1.0
 Last Update: 2013-04-15
 Update By:   Matthew J Swann
 
 Primary data import scheme.

 """

def main():
    
    time_one = datetime.now()
    BusinessImport()
    SchoolImport()
    PersonImport()
    ChildImport()
    time_two = datetime.now()
    print (time_two - time_one)
    
    
if __name__ == '__main__':
    pass
