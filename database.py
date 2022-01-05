import sqlite3

class Database:
    def __init__(self):
        self.db = sqlite3.connect('database.db')
        self.cursor = self.db.cursor()

    # GETS
    def get_beatmaps(self):
        return self.cursor.execute(
            "SELECT * FROM beatmaps"
        ).fetchall()

    def get_matchups(self):
        return self.cursor.execute(
            "SELECT * FROM comparisons"
        ).fetchall()
