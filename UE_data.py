import sqlite3

def insert_ue_data():
    conn = sqlite3.connect("ue.db")
    cursor = conn.cursor()

    # Data to insert
    ue_entries = [
        ('208920000000001', '+919876543210', '1234', '0x1234567890ABCDEF', '0x12345678'),
        ('208908000000007', '+919876543216', '7654', '0x1234567890ABCDEF', '0x12345678'),
        ('208920000000006', '+919876543215', '3210', '0x90ABCDEF1234567890', '0x90ABCDEF'),
        ('208020000070010', '+919876543219', '1098', '0x1234567890ABCDEF', '0x12345678')
    ]

    cursor.executemany("INSERT INTO ue_data (imsi, msisdn, opc, k, rand) VALUES (?, ?, ?, ?, ?)", ue_entries)

    conn.commit()
    conn.close()
    print("UE data inserted successfully!")

if __name__ == "__main__":
    insert_ue_data()
