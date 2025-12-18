import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",           # Use your actual MySQL username
    password="root",       # Use your actual password
    database="SmartAgriculture"
)
cursor = conn.cursor()

# ------------------ CREATE ------------------
def insert_reading(sensor_id, moisture):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = "INSERT INTO SoilMoisture (SensorID, MoistureLevel, ReadingTime) VALUES (%s, %s, %s)"
    cursor.execute(query, (sensor_id, moisture, timestamp))
    conn.commit()

# Example insert
insert_reading(4, 19.5)

# ------------------ READ ------------------
def fetch_all():
    cursor.execute("SELECT * FROM SoilMoisture")
    return cursor.fetchall()

print("All Records:")
for row in fetch_all():
    print(row)

# ------------------ UPDATE ------------------
def update_reading(sensor_id, reading_time, new_moisture):
    query = "UPDATE SoilMoisture SET MoistureLevel=%s WHERE SensorID=%s AND ReadingTime=%s"
    cursor.execute(query, (new_moisture, sensor_id, reading_time))
    conn.commit()

# Example update
update_reading(4, '2025-12-18 08:00:00', 21.0)

# ------------------ DELETE ------------------
def delete_reading(sensor_id, reading_time):
    query = "DELETE FROM SoilMoisture WHERE SensorID=%s AND ReadingTime=%s"
    cursor.execute(query, (sensor_id, reading_time))
    conn.commit()

# Example delete
delete_reading(4, '2025-12-18 08:00:00')

# ------------------ FILTER BELOW THRESHOLD ------------------
def fetch_below_threshold(threshold):
    query = "SELECT * FROM SoilMoisture WHERE MoistureLevel < %s"
    cursor.execute(query, (threshold,))
    return cursor.fetchall()

print("\nMoisture Below Threshold (< 20.0):")
for row in fetch_below_threshold(20.0):
    print(row)

# Close connection
cursor.close()
conn.close()