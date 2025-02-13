import sqlite3

def fetch_hss_data():
    conn = sqlite3.connect("hss.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM hss_data")
    records = cursor.fetchall()

    print("\nHSS Data:")
    for record in records:
        print(record)

    conn.close()

if __name__ == "__main__":
    fetch_hss_data()
