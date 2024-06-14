import sqlite3

def create_db():
    conn = sqlite3.connect('breast.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS `percobaan` (  `id` tinyint(4) AUTOINCREMENT,  `image` varchar(24) DEFAULT NULL,  `result1` decimal(18,15) DEFAULT NULL,  `result2` decimal(17,15) DEFAULT NULL, `hasil1` varchar(7) DEFAULT NULL,  `hasil2` varchar(7) DEFAULT NULL)''')
    conn.commit()
    conn.close()
def get_db_connection():
    conn = sqlite3.connect('breast.db')
    conn.row_factory = sqlite3.Row
    return conn

def insert_data(data):
    conn = get_db_connection()
    c = conn.cursor()
    print(data)
    c.execute("INSERT INTO percobaan (id, image, result1, result2, hasil1, hasil2) VALUES (?, ?, ?, ?, ?, ?)", ('', data['image'], data['result1'], data['result2'], data['hasil1'], data['hasil2']))
    conn.commit()
    conn.close()
    print(str(c.lastrowid))
    return str(c.lastrowid)

def get_data(id) :
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM percobaan ")
    data = c.fetchone()
    conn.close()
    return data