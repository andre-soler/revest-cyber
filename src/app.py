import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # ✅ Seguro: consulta parametrizada
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()
