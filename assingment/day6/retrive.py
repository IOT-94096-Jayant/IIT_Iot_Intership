query = "select * from students";

# create cursor to execute query
cursor = connection.cursor()

# execute qeury with cursor
cursor.execute(query)

# get required data from cursor
students = cursor.fetchall()

# print students data
#print(students)

for student in students:
    print(student)
    
# close the cursor
cursor.close()

# close connection with mysql server
connection.close()