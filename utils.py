import sqlite3

def db():
    conn = sqlite3.connect("web.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS poll(id text, choices text, creator text, sname text)")
    conn.commit()
    conn.close()

def insert(id : str, choices : str, creator : str, sname : str):
    conn = sqlite3.connect("web.db")
    c = conn.cursor()
    c.execute("INSERT INTO poll VALUES(?, ?, ?, ?)", (id, choices, creator, sname))
    conn.commit()
    conn.close()

def get_info(id : str):
    conn = sqlite3.connect("web.db")
    c = conn.cursor()
    c.execute("SELECT * FROM poll WHERE id = ?", (id))
    rows = c.fetchall()
    conn.close()
    return rows[0]

insert("1", "Hello##Test", "combo#1190", "poller")