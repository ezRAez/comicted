import sqlite3

def connect():
    conn = sqlite3.connect("comicted.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS comic (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn text)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("comicted.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO comic VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("comicted.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM comic")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("comicted.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM comic WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("comicted.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM comic WHERE id=?", (id,))
    conn.commit()
    conn.close()
