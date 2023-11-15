# import requests
# import json
# import psycopg2
# from datetime import datetime

# # Define your PostgreSQL database connection parameters
# DB_NAME = "alqurancloudapi"
# DB_USER = "postgres"
# DB_PASS = "zxcv"

# # Define the API URL
# API_URL = "http://api.alquran.cloud/v1/edition"

# # Send a GET request to the API URL to fetch the data
# response = requests.get(API_URL)

# # Check if the request was successful (HTTP status code 200)
# if response.status_code == 200:
#     data = response.json()

#     # Save the JSON data to a file
#     with open("api_data.json", "w") as file:
#         json.dump(data, file, indent=4)

#     # Establish a connection to the PostgreSQL database
#     conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS)
#     cur = conn.cursor()

#     for edition_data in data["data"]:
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         # Set a default direction if 'direction' is missing or null
#         direction = edition_data.get("direction", "rtl")

#         cur.execute(
#             """
#             INSERT INTO qurancloud_edition (created_at, updated_at, identifier, language, name, "englishName", format, type, direction)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
#         """,
#             (
#                 current_time,  # created_at
#                 current_time,  # updated_at
#                 edition_data["identifier"],
#                 edition_data["language"],
#                 edition_data["name"],
#                 edition_data["englishName"],
#                 edition_data["format"],
#                 edition_data["type"],
#                 direction,  # Set the 'direction' value
#             ),
#         )

#     conn.commit()
#     print("Data imported successfully.")

#     # Close the database connection
#     cur.close()
#     conn.close()

# else:
#     print(f"Failed to fetch data from the API. Status code: {response.status_code}")

import requests
import json
import psycopg2
from datetime import datetime

# Define your PostgreSQL database connection parameters
DB_NAME = "alqurancloudapi"
DB_USER = "postgres"
DB_PASS = "zxcv"

# Define the API URL
API_URL = "https://api.alquran.cloud/v1/surah"

# Send a GET request to the API URL to fetch the data
response = requests.get(API_URL)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    data = response.json()

    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS)
    cur = conn.cursor()

    for surah_data in data["data"]:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cur.execute(
            """
            INSERT INTO qurancloud_surah (created_at, updated_at, number, name, english_name, english_name_translation, revelation_type, "numberOfAyahs")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (
                current_time,  # created_at
                current_time,  # updated_at
                surah_data["number"],
                surah_data["name"],
                surah_data["englishName"],
                surah_data["englishNameTranslation"],
                surah_data["revelationType"],
                surah_data["numberOfAyahs"],
            ),
        )

    conn.commit()
    print("Data imported successfully.")

    # Close the database connection
    cur.close()
    conn.close()

else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")
