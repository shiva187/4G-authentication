import sqlite3

def create_ue_table():
    conn = sqlite3.connect("ue.db")
    cursor = conn.cursor()

    # Creating ue_data table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ue_data (
        imsi TEXT PRIMARY KEY,
        msisdn TEXT NOT NULL,
        opc TEXT NOT NULL,
        k TEXT NOT NULL,
        rand TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Table 'ue_data' created successfully!")

if __name__ == "__main__":
    create_ue_table()
