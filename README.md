# twofg

# How to do when pull a new changes.

## Optional.

If the db was changed, run the following command.

- python manage.py inspectdb
  And for apply this changes on the models run the next command.
- python manage.py inspectdb > models.py

---

1. Run the migrations with following commands.

   - python manage.py makemigrations
   - python manage.py migrate

2. Run the requirements file with the next command.

   - pip install -r requirements.txt

3. Check the .env.example file and add and modify the new vars to your .env file with them.

4. Generate a new SECRET_KEY and modify only in .env file for the project can work correctly use the next command on the terminal for generate a SECRET KEY.
   - python -c "import secrets; print(secrets.token_urlsafe(50))"

# Before you push new changes do the nexts steps.

1. Update the requirements file with the following command.

   - pip freeze > requirements.txt

2. Update the .env.example file with the new vars added on the .env file
