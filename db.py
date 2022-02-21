import sqlite3
import logging


class DBHelper:
    def __init__(self, dbname="track_table.sqlite"):
        self.dbname = dbname
        try :
            self.conn = sqlite3.connect(dbname, check_same_thread=False)
        except Exception as e:
            print(e)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS track_table (id PRIMARY KEY, code INTEGER UNIQUE)"
        self.conn.execute(stmt)
        self.conn.commit()

    def check(self, code):
        stmt = "SELECT COUNT(1) FROM track_table WHERE code=%d"
        stmt2 = "select * from track_table"
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(1) FROM track_table WHERE code=:code",{'code':code})
        #cursor.execute("SELECT COUNT(1) FROM track_table WHERE code=?",code)
        res = cursor.fetchone()
        return res
if __name__ == 'main':
    db = DBHelper()
    db.setup()
    cnn = db.conn
    cnn.execute("insert into track_table values (54664, 42)")