import sqlite3

class Database:

    def __init__(self, db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS comic (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn text)")
        conn.commit()
        conn.close()

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect("comicted.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO comic VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("comicted.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM comic")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title = "", author = "", year = "", isbn = ""):
        conn = sqlite3.connect("comicted.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM comic WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        conn = sqlite3.connect("comicted.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM comic WHERE id=?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect("comicted.db")
        cur = conn.cursor()
        cur.execute("UPDATE comic SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()
