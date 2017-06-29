import sqlite3

class Database():

    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.conn = sqlite3.connect(self.dbfile)
        self.check_table()

    def check_table(self):
        c = self.conn.cursor()

        # create table for remember.py
        c.execute('CREATE TABLE IF NOT EXISTS remember_tbl (id INTEGER PRIMARY KEY, key text NOT NULL, value text NOT NULL)')

        self.conn.commit()

