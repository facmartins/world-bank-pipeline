# IMPORT LIBRARIES
import requests
import pandas as pd
import pyodbc
from config import SERVER, DATABASE

# EXTRACT
countries = ["PT", "ES", "FR", "DE", "IT", "GB", "US", "BR", "CN", "IN"]
indicators = {
    "gdp": "NY.GDP.MKTP.CD",
    "inflation": "FP.CPI.TOTL.ZG",
    "unemployment": "SL.UEM.TOTL.ZS",
    "population": "SP.POP.TOTL"
}

all_data = []

for country in countries:
    print(f"🔄 Extracting {country}...")
    row = {"country_code": country}

    for key, indicator in indicators.items():
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&mrv=1"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if len(data) > 1 and data[1]:
                row[key] = data[1][0]["value"]
                row["year"] = data[1][0]["date"]
                row["country"] = data[1][0]["country"]["value"]
            else:
                row[key] = None
        else:
            row[key] = None

    all_data.append(row)
    print(f"✅ {country} extracted!")

print(f"\n✅ Total records extracted: {len(all_data)}")


# TRANSFORM
df = pd.DataFrame(all_data)

# Reorder columns
df = df[["country", "country_code", "year", "gdp", "inflation", "unemployment", "population"]]

# Clean data
df = df.drop_duplicates()
df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
df["population"] = pd.to_numeric(df["population"], errors="coerce").astype("Int64")
df["gdp"] = pd.to_numeric(df["gdp"], errors="coerce").round(2)
df["inflation"] = pd.to_numeric(df["inflation"], errors="coerce").round(2)
df["unemployment"] = pd.to_numeric(df["unemployment"], errors="coerce").round(2)

print("\n📊 Transformed data:")
print(df)
print(f"\n✅ Total records after transform: {len(df)}")


# LOAD
print("🔄 Starting Load...")

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection=yes;"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO Economics (country, country_code, year, gdp, inflation, unemployment, population)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, row["country"], row["country_code"],
            int(row["year"]) if pd.notna(row["year"]) else None,
            float(row["gdp"]) if pd.notna(row["gdp"]) else None,
            float(row["inflation"]) if pd.notna(row["inflation"]) else None,
            float(row["unemployment"]) if pd.notna(row["unemployment"]) else None,
            int(row["population"]) if pd.notna(row["population"]) else None)
    except Exception as e:
        print(f"❌ Error on {row['country']}: {e}")

conn.commit()
cursor.close()
conn.close()

print("\n✅ Data loaded into SQL Server successfully!")