import sqlite3
import hashlib
import random

def generate_rand():
    return hex(random.randint(0, 2**128 - 1))

def compute_xres(k, rand):
    data = k + rand
    return hashlib.sha256(data.encode()).hexdigest()[:16]

def ue_initiate_auth(ue_imsi):
    print(f"\nUE: Initiating authentication request for IMSI {ue_imsi}...")
    enb_receive_request(ue_imsi)

def enb_receive_request(ue_imsi):
    print(f"eNB: Received authentication request from UE with IMSI {ue_imsi}. Forwarding to MME...")
    mme_receive_request(ue_imsi)

def mme_receive_request(ue_imsi):
    print(f"MME: Received authentication request for IMSI {ue_imsi}. Querying HSS...")
    hss_process_auth(ue_imsi)

def hss_process_auth(ue_imsi):
    try:
        hss_conn = sqlite3.connect("hss.db")
        hss_cursor = hss_conn.cursor()
        hss_cursor.execute("SELECT k, opc FROM hss_data WHERE imsi = ?", (ue_imsi,))
        hss_record = hss_cursor.fetchone()

        if hss_record:
            k, opc = hss_record
            print(f"HSS: IMSI {ue_imsi} found. Fetching data...")
            rand = generate_rand()
            xres = compute_xres(k, rand)
            print(f"HSS: Generated RAND: {rand} and XRES: {xres}. Sending to MME...")
            mme_receive_auth_data(ue_imsi, rand, xres, k)
        else:
            print(f"HSS: IMSI {ue_imsi} not found. Authentication failed.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        hss_conn.close()

def mme_receive_auth_data(ue_imsi, rand, xres, k):
    print(f"MME: Received authentication data from HSS. Forwarding RAND to UE via eNB...")
    enb_forward_rand(ue_imsi, rand, xres, k)

def enb_forward_rand(ue_imsi, rand, xres, k):
    print(f"eNB: Forwarding RAND to UE for computation...")
    ue_compute_res(ue_imsi, rand, xres, k)

def ue_compute_res(ue_imsi, rand, xres, k):
    print(f"UE: Computing RES using received RAND: {rand}")
    res = compute_xres(k, rand)
    print(f"UE: Computed RES: {res}. Sending to MME via eNB...")
    enb_forward_res(ue_imsi, res, xres)

def enb_forward_res(ue_imsi, res, xres):
    print(f"eNB: Forwarding RES to MME...")
    mme_validate_res(ue_imsi, res, xres)

def mme_validate_res(ue_imsi, res, xres):
    if res == xres:
        print(f"MME: Authentication Successful for IMSI {ue_imsi}!")
    else:
        print(f"MME: Authentication Failed for IMSI {ue_imsi}. RES does not match XRES.")

def main():
    try:
        ue_conn = sqlite3.connect("ue.db")
        ue_cursor = ue_conn.cursor()
        ue_cursor.execute("SELECT imsi FROM ue_data")
        ue_records = ue_cursor.fetchall()
        for ue in ue_records:
            ue_initiate_auth(ue[0])
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        ue_conn.close()

if __name__ == "__main__":
    main()
