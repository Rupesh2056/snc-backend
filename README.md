

### Setup

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

2. Clone the repo:

   ```
   git clone https://github.com/Rupesh2056/snc-backend
   cd snc-backend
   ```

3. Prepare Environment
    ```
    uv sync 
    ```

4. migrate database and create superuser and other data
    ```
    uv run manage.py migrate
    uv run manage.py fill_data
    ```

5. Run Server
    ```
    uv run manage.py runserver 0.0.0.0:8000
    ```

6. Visit [here](http://127.0.0.1:8000) and login with username: "admin" and password "admin"


### For Intermediate Through Table Solution

1. Switch branch
    ```
    git switch feat-through-table
    ```
2. Migrate Database
    ```
    uv run manage.py migrate
    ```
3. Now, an intermediate table StudentMetaData will be used by m2m field (meta_data)of Student Table. This has extra fields added_by and added_at.

4. Visit [student list page](http://127.0.0.1:8000/student/) and view detail page to ensure preservation of old meta data.

5. [Add new Student](http://127.0.0.1:8000/student/create/) and view detail of newly created Student to see the added_by field on newer datas.


##

### Overview

1. Project Structure
    >I used seperate apps to seperate concerns.
    
| App  | Models and Logics |
| ------------- |:-------------:|
| root          | Project root (containing settings.py) |
| user          | Student,Instructor |
| course        | Course,Enrollment     |
| meta          | MetaData      |
| utils          | BaseModel (Contains all Mixins and logics used by all    models)      |


2. Additional Features Covered 
    > 1. Fully SPA using htmx.
    > 2. Realtime Search without wholepage reload
    > 3. Dynamic Filter of MetaData. (Dropdowns are created dynamically.)
    > 4. Feature to add MetaData page within create/update page of Student,Course e.t.c Models. 
    >5. Pagination for all List Pages.
    