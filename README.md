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

# CREATE ADDRESS API:
{
  "street": "Kolkata rolls",
  "city": "Kolkata",
  "latitude": -87.629798,
  "longitude": 41.878114
},

{
  "street": "Am schwantentich 8",
  "city": "Mumbai",
  "latitude": -97.629798,
  "longitude": 31.878114
},

{
  "street": "adad",
  "city": "adddadada",
  "latitude": -101.556,
  "longitude": 46.6768
},

{
  "street": "fgfh",
  "city": "Delhi",
  "latitude": -20.7899,
  "longitude": 10.8967
}

# For distance calculation:

The use of the Haversine formula in this code is appropriate for calculating distances between geographical coordinates on the Earth's surface. Addresses that are within the specified max_distance_km are added to the valid_addresses list.
get_addresses_within_distance that retrieves addresses from an SQLite database and filters them based on their distance from a specified latitude and longitude using the Haversine formula. The Haversine formula is commonly used to calculate the distance between two points on the Earth's surface with respect to its radius.

# Sample coordinates for the reference
**i/p:**
latitude = -20.678

longitude = 10.9887

distance = 4940

**O/p / response body:**
[
  [
    "fgfh",
    "Delhi",
    -20.7899,
    10.8967
  ]
]

**i/p:**
latitude = -20.678

longitude = 10.9887

distance = 20000

**O/p / response body:**
[
  [
    "Kolkata rolls",
    "Kolkata",
    -87.629798,
    41.878114
  ],
  [
    "Am schwantentich 8",
    "Mumbai",
    -97.629798,
    31.878114
  ],
  [
    "adad",
    "adddadada",
    -101.556,
    46.6768
  ],
  [
    "fgfh",
    "Delhi",
    -20.7899,
    10.8967
  ]
]


# (FASTAPI SWAGGER)
http://127.0.0.1:8005/docs#/    (FASTAPI SWAGGER)

(POST - Create address,

PUT - Update address,

DELETE - Deleting address with id number,

GET - Getting addresses within the address
