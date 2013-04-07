""" Python Package Imports """
# Not Applicable

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
 Last Update: 2013-04-07
 Update By:   Matthew J Swann
 
 Primary data import scheme.

 """

def main():
    
    BusinessImport()
    SchoolImport()
    PersonImport()
    ChildImport()
    
    
    
if __name__ == '__main__':
    pass
