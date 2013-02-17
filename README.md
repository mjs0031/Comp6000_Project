Comp6000_Project
================

 """

 Comp6000/readme.md
 Author(s)    : Matthew J Swann; Yong Kin; Bradon Atkins
 Version      : 1.0
 Last Revised : 2013-02-17
 Update By    : Matthew J Swann
 
 The HTLM docs will be linked to the views in "Data_Base/views.py". 
 The views will interact with the data itself. The schemas and 
 functionality for the data will exist within "Data_Base/models.py".
 
 Files in "Comp600" ::
 
    "/manage.py"   -- control script. Any command line interaction
 	 		uses this script :
 				'$ python manage.py shell'
 					- opens a shell to the DB
 					
 				'$ python manage.py syncdb'
 					- syncs the DB, must DELETE DB if model changes
 						have been made
 						
 				'$ python manage.py runserver 8000'
 					- runs the server on port 8000
 					- open browser, go to 'localhost:8000' for homepage
 				
 				'$ python manage.py test <Package Name>'
 					- runs specific package unittests
 				
 				'$ python manage.py test'
 					- runs entire battery of unittests, all packages
 				
 				'$ python manage.py dumpdata <Package Name> --indent=4 > Control/fixtures/<Package Name>_testdata.json'
 					- dumps the DB tables from that package into JSON for unit testing;
 						won't dump anything for an empty package
 						
 Fiels in "Comp6000/#Documents" ::
 	"Comp6000 - Proposal.doc" -- the proposal
 	
 	{Other files to be added including, but not limited to, project specs.}
 
 Files in "Comp600/Comp6000" ::
 	"/settings.py" -- I'll make the 3-4 changes here. It's a delicate
 			file and we don't need to do much with. Autorun basically.
 			
 	"/urls.py"     -- This is where our URL schemes go. This'll be
 			light-weight. It'll tie the views, URL's and HTML together.
 			
 	"/wsgi.py"     -- Better not to touch it. I generally leave it be.
 	
 	
 Files in "Comp600/Control" ::
 	"/fixtures"    -- {includes readme.txt}; storage for *.json files
 	
 	"/templates"   -- {inclused readme.txt}; storage for HTML docs
 	
 	"/admin.py"    -- admin site setup; visited by running the server;
 						'localhost:8000/admin'
 						
 						
 Files in "Comp6000/Data_Base" ::
 	"/models.py"   -- Database tables; setup via Object Relational Mapping;
 						think of the tables as class outlines in OOP, that
 						analogy helped me
 						
 	"/test.py"     -- Unittesting framework for verification and validation;
 						cause I'm lazy; set it up and run her.
 						
 	"/views.py"    -- control for queries. basically this is the glue between
 						the HTLM and the tables declared in 'models.py'
 """
