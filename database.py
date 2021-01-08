import sqlite3


class Data:

    def __init__(self, dbfile):
        self.connection = sqlite3.connect(dbfile)
        self.cursor = self.connection.cursor()

    def create_db(self):
        with self.connection:
            self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS 'users'(
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            phone TEXT);"""
        )
        self.connection.commit()

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users'").fetchall()

    def add_user(self, user_id, first_name, phone):
        with self.connection:
            return self.cursor.execute(
                f"INSERT INTO 'users' ('user_id', 'first_name', 'phone') VALUES(?, ?, ?)", (user_id, first_name, phone)
            )

    def close(self):
        self.connection.close()


db = Data('db.db')
db.create_db()
print(db.get_users())