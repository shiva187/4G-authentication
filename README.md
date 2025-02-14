# 4G Core Network UE Authentication Simulation

This project simulates UE (User Equipment) authentication in a "4G Core Network" by using databases for "UE and HSS (Home Subscriber Server)". It includes multiple scripts for database creation, data storage, and verification of UEs based on HSS records.

 📌 Project Overview

This project implements the **Authentication and Key Agreement (AKA) process in a 4G Core Network. The main functionalities include:

- Managing UE and HSS databases
- Storing and retrieving subscriber authentication data
- Verifying UEs by checking their credentials against the HSS
- Using different programs for database management and authentication simulation

 🏛 Database Structure

The project uses two SQLite databases:

 1️⃣ UE Database

Stores information about the UEs trying to authenticate.

| Column | Type | Description                              |
| ------ | ---- | ---------------------------------------- |
| imsi   | TEXT | International Mobile Subscriber Identity |
| msisdn | TEXT | Mobile Station ISDN Number               |
| opc    | TEXT | Operator Configuration Parameter         |
| k      | TEXT | Authentication Key                       |
| rand   | TEXT | Random Challenge                         |

 2️⃣ HSS Database

Stores authentication parameters used for verifying UEs.

| Column | Type | Description                      |
| ------ | ---- | -------------------------------- |
| imsi   | TEXT | UE IMSI (Primary Key)            |
| msisdn | TEXT | Mobile Number                    |
| opc    | TEXT | Operator Configuration Parameter |
| k      | TEXT | Authentication Key               |
| rand   | TEXT | Random Challenge                 |
| xres   | TEXT | Expected Response                |
| ck     | TEXT | Cipher Key                       |
| ik     | TEXT | Integrity Key                    |
| autn   | TEXT | Authentication Token             |

 ⚙️ Features and Functionalities

- UE initiates authentication request to eNB (Base Station)
- eNB forwards request to MME (Mobility Management Entity)
- MME queries HSS to validate UE credentials
- HSS verifies UE and sends authentication response
- UE authentication success/failure determination

## 📂 Project Files

| File Name              | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| create_db_hss.py     | Creates the `hss.db` database and table                 |
| hss_data.py            | Inserts predefined authentication records into `hss.db` |
| HSS_disp.py            | Retrieves and displays stored HSS data                  |
| create_db_ue.py         | Creates the `ue.db` database and table                  |
| ue_data.py             | Inserts predefined UE records into `ue.db`              |
| authenticate_ue.py     | Simulates UE authentication by verifying against HSS    |

 🚀 How to Use

 1️⃣ Set Up the Database

Run the following commands to create the databases:


python create_db_hss.py
python create_db_ue.py


2️⃣ Insert Data into Databases


python insert_hss_data.py
python insert_ue_data.py


3️⃣ Run UE Authentication Process


python authenticate_ue.py


📜 License

This project is open-source and free to use under the **MIT License**.

💡 Future Enhancements

- Implement MILENAGE algorithm for secure authentication
- Extend support for **5G Security Functions (SEAF, AUSF, UDM)
- Introduce real-time communication simulation between nodes


