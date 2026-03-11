
import requests
import pandas as pd
import mysql.connector
import time
from datetime import datetime

# API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

# Database connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ifdxrmf4j9#123",
    database="crypto_project"
)

cursor = conn.cursor()

print("Crypto data collector started...")

while True:

    # Fetch API data
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data)

    df = df[[
        "name",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume"
    ]]

    df["timestamp"] = datetime.now()

    # Insert into database
    for index, row in df.iterrows():

        query = """
        INSERT INTO crypto_prices
        (coin_name, symbol, price, market_cap, volume, timestamp)
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (
            row["name"],
            row["symbol"],
            row["current_price"],
            row["market_cap"],
            row["total_volume"],
            row["timestamp"]
        )

        cursor.execute(query, values)

    conn.commit()

    print("Data inserted at:", datetime.now())

    # Wait 5 minutes
=======
import requests
import pandas as pd
import mysql.connector
import time
from datetime import datetime

# API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

# Database connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ifdxrmf4j9#123",
    database="crypto_project"
)

cursor = conn.cursor()

print("Crypto data collector started...")

while True:

    # Fetch API data
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data)

    df = df[[
        "name",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume"
    ]]

    df["timestamp"] = datetime.now()

    # Insert into database
    for index, row in df.iterrows():

        query = """
        INSERT INTO crypto_prices
        (coin_name, symbol, price, market_cap, volume, timestamp)
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (
            row["name"],
            row["symbol"],
            row["current_price"],
            row["market_cap"],
            row["total_volume"],
            row["timestamp"]
        )

        cursor.execute(query, values)

    conn.commit()

    print("Data inserted at:", datetime.now())

    # Wait 5 minutes
