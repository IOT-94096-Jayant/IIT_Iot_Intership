import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="306",
    password="root",
    database="iot_data"
)
cursor = conn.cursor()

# ------------------ CREATE ------------------
def insert_reading(temp, hum):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = "INSERT INTO sensor_readings (temperature, humidity, timestamp) VALUES (%s, %s, %s)"
    cursor.execute(query, (temp, hum, timestamp))
    conn.commit()

# Example insert
insert_reading(22.5, 58.0)

# ------------------ READ ------------------
def fetch_all():
    cursor.execute("SELECT * FROM sensor_readings")
    return cursor.fetchall()

print("All Records:")
for row in fetch_all():
    print(row)

# ------------------ UPDATE ------------------
def update_reading(record_id, new_temp, new_hum):
    query = "UPDATE sensor_readings SET temperature=%s, humidity=%s WHERE id=%s"
    cursor.execute(query, (new_temp, new_hum, record_id))
    conn.commit()

# Example update
update_reading(3, 26.0, 62.0)

# ------------------ DELETE ------------------
def delete_reading(record_id):
    query = "DELETE FROM sensor_readings WHERE id=%s"
    cursor.execute(query, (record_id,))
    conn.commit()

# Example delete
delete_reading(5)

# ------------------ FILTER BELOW THRESHOLD ------------------
def fetch_below_threshold(temp_threshold, hum_threshold):
    query = "SELECT * FROM sensor_readings WHERE temperature < %s OR humidity < %s"
    cursor.execute(query, (temp_threshold, hum_threshold))
    return cursor.fetchall()

print("\nBelow Threshold Records (Temp < 26 or Humidity < 60):")
for row in fetch_below_threshold(26, 60):
    print(row)

# Close connection
cursor.close()
conn.close()