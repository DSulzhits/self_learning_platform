Self Learning Platform service, including Sections (in this example different kind of animals) and Content (animal
species).
Virtual environment in this project: venv

1) After starting virtual environment, install dependencies from file requirements.txt

```bash
pip install - r requirements.txt
```

2) Fill .env file according to file .env.sample


3) Create database with command

```bash
python manage.py ccdb
```

4) Create migrations with command

```bash
python manage.py makemigrations
```

5) Apply migrations with command

```bash
python manage.py migrate
```

6) Run command, to create Users

```bash
python manage.py ccsu
```

7) Run command, to fill the database, with fixture

```bash
python manage.py loaddata sections.json
```

8) Run command, to start application
```bash
python manage.py runserver 
```

Project Models

Section with fields:

- title - section title
- description - section description (may be empty)


Content with fields:

- section - related to section
- title - content title
- content - content

User with fields:

- email - user email
- role - user role (MEMBER or MODERATOR)
- first_name - user first name (may be empty)
- last_name - user last name (may be empty)
- phone - user phone (may be empty)
- is_active - boolean field default=True



Permissions 
- Realized custom permission for User.role = MODERATOR
- See the sections list and the content list can all authorised users
- See detail info about sections or content can all authorised users
- Create, Update, Delete section or content items can AdminUser or Moderator
- See the users list can AdminUser or Moderator
- Create new users can all users
- See detail info about user all authorised users
- Update user can AdminUser or Moderator or User (only his own account)
- Delete user can only the AdminUser


Pagination
- Realised pagination for list of sections (3 item per page) and for list of content (10 items per page)


Endpoints for model Section
- List of Sections
- Create a new Section
- Detail info about Section
- Update the Section
- Delete the Section

Endpoints for model Сontent
- List of Сontent
- Create a new Сontent
- Detail info about Сontent
- Update the Сontent
- Delete the Сontent

Endpoints for model User
- List of Users
- Create a new User
- Detail info about User
- Update the User
- Delete the User

Documentation
- Documentation you can see here:
```bash
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```