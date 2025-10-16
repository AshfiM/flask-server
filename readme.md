#Initalization Steps
1. move to directory Where you want to Store the repository
2. Clone the repository
    - ``git clone <repoLink>``
3. Create .env file and .env.production file in your repo folder
4. Store follwing values in both env files 
5. Create database
```
FLASK_ENV=development
FLASK_SECRET_KEY=dev_secret_key
JWT_SECRET_KEY=dev_jwt_secret
SQLALCHEMY_DATABASE_URL=dataabse
```
#Steps to Run

1. Create Virtual Environment
    - ``python3 -m venv venv``
2. Activate Virtual Environment
    - In Linux/ Macos 
        - ``source venv/bin/activate``
    - In Windows 
        - ``venv\Scripts\activate``
3. Install Dependencies
    - ``pip install -r requirements.txt``
4. To Run 
    - To run in development
        - In Mac 
            - ``python3 run.py``
        - In Windows
            - ``python run.py``
    - To Run in (nginx web sever -> gunicorn -> Flask) Production
        - In windows
            - Install nginx server
            - Run
                - ``python runServer.py``
        - In Mac
            - Install nginx through homebrew
                - ``brew install nginx``
            - Run
                - ``python3 runServer.py``


#Update Requirements File
- ``pip freeze > requirements.txt``

