#Initalization Steps
1. move to directory Where you want to Store the repository
2. Clone the repository
    ```git clone <repoLink>```


#Steps to Run

1. Create Virtual Environment
    ```python3 -m venv venv```
2. Activate Virtual Environment
    ```In Linux/ Macos - source venv/bin/activate```
    ```In Windows - venv\Scripts\activate```
3. Install Dependencies
    ```pip install -r requirements.txt```
4. To Run in development 
    ```python3 run.py```
    ```To Run in (WSGI Server) Production```
    ```python wsgi.py```


#Update Requirements File
```pip freeze > requirements.txt```

