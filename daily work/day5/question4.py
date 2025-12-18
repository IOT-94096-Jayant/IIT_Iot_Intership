import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="306",              # your MySQL username
    password="root",         # your MySQL password
    database
)

cursor = conn.cursor()

# -----------------------------
# 1. CREATE - Insert new record
# -----------------------------
insert_query = """
INSERT INTO SoilMoisture (SensorID, MoistureLevel, ReadingTime)
VALUES (%s, %s, %s)
"""
data = (5, 17.8, "2025-12-18 11:00:00")
cursor.execute(insert_query, data)
conn.commit()
print("✅ Record inserted successfully!")

# -----------------------------
# 2. READ - Retrieve records below threshold
# -----------------------------
threshold = 20.0
select_query = """
SELECT SensorID, MoistureLevel, ReadingTime
FROM SoilMoisture
WHERE MoistureLevel < %s
"""
cursor.execute(select_query, (threshold,))
results = cursor.fetchall()

print(f"\n🌱 Records with MoistureLevel below {threshold}:")
for row in results:
    print(row)

# -----------------------------
# 3. UPDATE - Modify a record
# -----------------------------
update_query = """
UPDATE SoilMoisture
SET MoistureLevel = %s
WHERE SensorID = %s AND ReadingTime = %s
"""
cursor.execute(update_query, (25.0, 2, "2025-12-18 08:05:00"))
conn.commit()
print("\n🔄 Record updated successfully!")

# -----------------------------
# 4. DELETE - Remove a record
# -----------------------------
delete_query = """
DELETE FROM SoilMoisture
WHERE SensorID = %s AND ReadingTime = %s
"""
cursor.execute(delete_query, (3, "2025-12-18 08:15:00"))
conn.commit()
print("\n🗑️ Record deleted successfully!")

# Close connection
cursor.close()
conn.close()

