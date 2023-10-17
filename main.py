# Create an address book application where API users can create, update and delete
# addresses.
# The address should:
# - contain the coordinates of the address.
# - be saved to an SQLite database.
# - be validated
# API Users should also be able to retrieve the addresses that are within a given distance and
# location coordinates.
# Important: The application does not need a GUI. (Built-in FastAPI’s Swagger Doc is sufficient)


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from math import radians, sin, cos, sqrt, atan2


app = FastAPI()


# Define your data model
class Address(BaseModel):
    id: int
    street: str
    city: str
    latitude: float
    longitude: float


class Addressnew(BaseModel):
    street: str
    city: str
    latitude: float
    longitude: float

class Addressdel(BaseModel):
    id:int



db = 'address_book.db'
# Create the SQLite database and table
conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS addresses
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  street TEXT, city TEXT, 
                  latitude REAL, longitude REAL, UNIQUE(street, city))''')
conn.commit()
conn.close()


@app.post("/addresses/", response_model=Addressnew)
def create_address(address: Addressnew):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO addresses (street, city, latitude, longitude) VALUES (?, ?, ?, ?)",
                   (address.street, address.city, address.latitude, address.longitude))
    conn.commit()
    conn.close()
    return address


@app.put("/addresses/", response_model=Address)
def update_address(address: Address):
    # Implement the update logic
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE addresses SET street=?, city=?, latitude=?, longitude=? WHERE id=?",
                       (address.street, address.city, address.latitude, address.longitude, address.id))
        conn.commit()
        conn.close()
        return address
    except sqlite3.IntegrityError as e:
        conn.rollback()  # Roll back the transaction, if any errors occurred and get back to previous state
        conn.close()
        print(e)
        raise HTTPException(status_code=400, detail="Update failed: Duplicate street and city values.")


@app.delete("/addresses/")
def delete_address(id:int):
    # Implement the delete logic
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(f"Delete from addresses where id={id}")
    conn.commit()
    conn.close()
    return id


# Haversine distance function
    def haversine_distance(lat1, lon1, lat2, lon2):
        # Radius of the Earth in kilometers
        R = 6371.0

        # Convert latitude and longitude from degrees to radians
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance

    try:
        # Execute the SQL query to select addresses within the specified distance
        cursor.execute("SELECT street, city, latitude, longitude FROM addresses")

        addresses = cursor.fetchall()

        # Filter addresses based on the distance
        valid_addresses = []
        for addr in addresses:
            addr_lat, addr_lon = addr[3], addr[2]  # Swap latitude and longitude
            distance = haversine_distance(latitude, longitude, addr_lat, addr_lon)
            if distance <= max_distance_km:
                valid_addresses.append(addr)

        # Close the database connection
        conn.close()

        return valid_addresses

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

