import sqlite3

def create_db():
    conn = sqlite3.connect('alzheimer.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS `percobaan` (  `id` INTEGER PRIMARY KEY AUTOINCREMENT,  `image` varchar(24) DEFAULT NULL,  `result1` decimal(18,15) DEFAULT NULL,  `result2` decimal(17,15) DEFAULT NULL, `hasil1` varchar(7) DEFAULT NULL,  `hasil2` varchar(7) DEFAULT NULL)''')
    conn.commit()
    conn.close()
def get_db_connection():
    conn = sqlite3.connect('alzheimer.db')
    # conn.row_factory = sqlite3.Row
    return conn

def insert_data(data):
    conn = get_db_connection()
    c = conn.cursor()
    print(data)
    c.execute("INSERT INTO percobaan (image, result1, result2, hasil1, hasil2) VALUES (?, ?, ?, ?, ?)", ( data['image'], data['result1'], data['result2'], data['hasil1'], data['hasil2']))
    conn.commit()
    conn.close()
    # print(str(c.lastrowid))
    return str(c.lastrowid)

def get_data(id) :
    conn = get_db_connection()
    c = conn.cursor()
    c.execute(f"SELECT * FROM percobaan where id ={id}")
    rows = c.fetchall()
    column_names = [desc[0] for desc in c.description]
# Convert the rows into dictionaries
    data = [{column_names[i]: value for i, value in enumerate(row)} for row in rows]
    conn.close()
    return data

def get_all() : 
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM percobaan")
    rows = c.fetchall()
    column_names = [desc[0] for desc in c.description]
    data = [{column_names[i]: value for i, value in enumerate(row)} for row in rows]
    conn.close()
    return data

def delete_data() :
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM percobaan")
    conn.commit()
    conn.close()
# create_db()
# data = {}
# data["image"] = "/testing/asda"
# data['result1'] = 3.141592653589793
# data['result2'] = 2.718281828459045
# data['hasil1'] = "tes1"
# data['hasil2']  = "tes2"
# delete_data()

# res = get_all()
# print(res)

