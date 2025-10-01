Initalization Steps
1. move to directory Where you want to Store the repository
2. Clone the repository
    \n\tgit clone <repoLink>


Steps to Run

1. Create Virtual Environment\n
    \tpyhton3 -m venv venv
2. Activate Virtual Environment
    \n\tIn Linux/ Macos - source venv/bin/activate
    \n\tIn Windows - venv\Scripts\activate
3. Install Dependencies
    \n\tpip install -r rewuirements.txt
4. To Run in development 
    \n\tpython3 run.py
    \nTo Run in (WSGI Server) Production
    \n\t python wsgi.py


Update Requirements File
 n\tpip freeze > requirements.txt

