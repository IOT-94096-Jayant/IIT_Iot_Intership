from flask import Flask, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="306",
        password="root",
        database="iot_data"
    )

@app.route('/temperture/<float:temp>')
def temperature(temp):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO sensor_readings (temperature, humidity, timestamp) VALUES (%s, %s, %s)"
        cursor.execute(query, (temp, 0.0, timestamp))  # Assuming humidity 0 for now
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"Temperature {temp} recorded at {timestamp}", "temperature": temp, "timestamp": timestamp})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/readings')
def get_readings():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sensor_readings")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        readings = [{"id": row[0], "temperature": row[1], "humidity": row[2], "timestamp": row[3]} for row in rows]
        return jsonify(readings)
    except Exception as e:
        return jsonify({"error": str(e)}), 500