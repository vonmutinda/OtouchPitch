# [minute-pitch](https://minuteone.herokuapp.com/)

## About OtouchPitch 
It's a web app that allows user to share incredible lines of pitches for various categories that anyone could use in just one minute to make a difference .

## Description & User Specifications
The minute-Pitch is web application  that enable users to:

    1. Post pitches
    2. View pitches posted by other user
    3. Downvote a pitch
    4. Upvote a pitch
    5. Comment on  pitches posted by othe users

## Specifications
Get the specs [here](https://github.com/vonmutinda/OtouchPitch/blob/master/specs.md)


## Set-up and Installation

### Software Requirements
    - Python 3.6 *
    - PostgreSQL DMS
    - Text Editor ( preferably vscode / pyCharm )

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/vonmutinda/OtouchPitch && cd OtouchPitch`

Install [Postgres](https://www.postgresql.org/download/)
Install [Python](https://www.python.org/downloads/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv --without-pip virtual`
`curl https://bootstrap.pypa.io/get-pip.py | python`
`source virtual/bin/activate`

### Database
Quickly create a database where your data is going to be persistent .
`psql`
`you=#  CREATE DATABASE pitches;`
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3 manage.py server` 

Open your browser on `http://localhost:5000/`, `http://127.0.0.1:5000`

## Technologies used
    - Python 3.7
    - HTML
    - Bootstrap 4 
    - CSS 
    - Heroku
    - Postgresql

## Support and contact details
Contact me [von MUTINDA](maxwellmutinda@outlook.com) for any comments, reviews or insights .

### License
Copyright (c) [von MUTINDA](LICENSE)