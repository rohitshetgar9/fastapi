# Activating venv
python3 -m venv venv

source venv/bin/activate

# fastapi
pip or pip3 installaton:

pip install db-sqlite3

pip install ORM-SQLite


pip install -r requirements.txt

or

pip3 install -r requirements.txt

#   sqlite3 commands:
sqlite3 address_book.db

SELECT * FROM addresses;

delete from addresses where id=3;

SELECT * FROM addresses;
.exit

# RUNNING FASTAPI UVICORN SERVER COMMAND:
uvicorn main:app --port 8005 --reload

# (FASTAPI SWAGGER)
http://127.0.0.1:8005/docs#/    (FASTAPI SWAGGER)

(POST - Create address,

PUT - Update address,

DELETE - Deleting address with id number,

GET - Getting addresses within address
