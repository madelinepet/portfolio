# portfolio
A django app deployed to AWS with an about me page, my projects, some data visualization, and links to my resume and social media accounts.

## Deployment
Formerly deployed as an EC2 instance, not currently for cost reasons.

## Getting Started
To start locally, 
- Clone the repository using `git clone [repository link]` in your CLI
- Add in .env file like this:
  ```
    SECRET_KEY=
    ALLOWED_HOSTS=
    DEBUG=True
    DB_NAME=portfolio
    DB_USER=
    DB_HOST=localhost
    DB_PASSWORD=
    IAM_APIKEY=
    MAPS_DEFAULT=
    MAPS_URL=
    NASA_URL=
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    ```

- Start a virtual environment by running "pipenv shell"
- Install the app dependencies using `pipenv install` from your CLI
- `brew install postgresql`
- `brew services start postgresql`, 
- `psql postgres`, and if there's an error, you may need to create a db with the same name as your computer using `create database <your computer name>` 
- `create role <DB_USER>`, `alter role <DB_USER> with login;`, `create database portfolio;`, `\q`
- Run `./manage.py makemigrations`, `./manage.py migrate`, `./manage.py collectstatic` `./manage.py runserver`
- Open http://localhost:8000/ in your browser

## Tools
Django, Python3, Jupyter, AWS, Google Domains, HTML5, CSS3, NASA image of the day API


