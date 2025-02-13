import sqlite3

def create_hss_table():
    conn = sqlite3.connect("hss.db")  # Creates the database file
    cursor = conn.cursor()

    # Creating hss_data table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hss_data (
        imsi TEXT PRIMARY KEY,
        msisdn TEXT NOT NULL,
        opc TEXT NOT NULL,
        k TEXT NOT NULL,
        rand TEXT NOT NULL,
        xres TEXT NOT NULL,
        ck TEXT NOT NULL,
        ik TEXT NOT NULL,
        autn TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Table 'hss_data' created successfully!")

if __name__ == "__main__":
    create_hss_table()
