# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="students"
)

# create cursor
cursor = connection.cursor()

# take user input
rollno = int(input("Enter rollno: "))
name = input("Enter name: ")
email = input("Enter email: ")
course = input("Enter course: ")

# parameterized query (SAFE)
query = "INSERT INTO students (rollno, name, email, course) VALUES (%s, %s, %s, %s)"

values = (rollno, name, email, course)

# execute query
cursor.execute(query, values)

# commit changes
connection.commit()

print("Record inserted successfully!")

# close cursor and connection
cursor.close()
connection.close()