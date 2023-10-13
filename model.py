import orm_sqlite

class Address_book(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True) # auto-increment
    name = orm_sqlite.StringField()
    location = orm_sqlite()


