import sqlite3

def fetch_ue_data():
    conn = sqlite3.connect("ue.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ue_data")
    records = cursor.fetchall()

    for record in records:
        print(record)

    conn.close()

if __name__ == "__main__":
    fetch_ue_data()
