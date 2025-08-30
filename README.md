### Setup

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

2. Clone the repo:

   '''
   git clone https://github.com/Rupesh2056/snc-backend
   cd snc-backend
   '''

3. Prepare Environment
    '''
    uv sync 
    '''

4. migrate database and create superuser and other data
    '''
    uv run manage.py migrate
    uv run manage.py fill_data
    '''

5. Run Server
    '''
    uv run manage.py runserver 0.0.0.0:8000
    '''

6. Visit 127.0.0.1:8000 and login with username: "admin" and password "admin"
