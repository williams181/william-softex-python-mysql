from connection import DBconnect
from create import Create

class Database:
    def __init__(self):
        conn = DBconnect()
        c = Create(conn)
        # c.drop_db()
        c.create_db()
        c.use_db()
        c.create_tables()
        c.populate_tables()
