# fastapi
# PIP installaton:
# pip install db-sqlite3
# pip install ORM-SQLite

#   sqlite3 commands:
sqlite3 address_book.db
SELECT * FROM addresses;
delete from addresses where id=3;
SELECT * FROM addresses;
.exit

##### RUNNING FASTAPI UVICORN SERVER COMMAND:
uvicorn main:app --port 8005 --reload

http://127.0.0.1:8005/docs#/    (FASTAPI SWAGGER)
(POST - Create address,
PUT - Update address,
DELETE - Deleting address with id number,
GET - Getting addresses within address
