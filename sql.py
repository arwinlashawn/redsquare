import sqlite3

# connect to sqlite database
conn = sqlite3.connect("School.db")
c = conn.cursor()

# define variables

# table names
table1 = "Class" # parent table
table2 = "Teacher"
table3 = "Student"

# column names
col1 = "id"
col2 = "name"
col3 = "no_of_students"
col4 = "teacher"
col5 = "salary"
col6 = "class"


### TABLE CREATION ###

# Class table creation
c.execute(f"""CREATE TABLE IF NOT EXISTS {table1}
	({col1} INTEGER PRIMARY KEY NOT NULL,
	{col2} TEXT, 
	{col3} INTEGER,
	{col4} TEXT)""")

# Teacher table creation
c.execute(f"""CREATE TABLE IF NOT EXISTS {table2}
	({col1} INTEGER PRIMARY KEY NOT NULL,
	{col2} TEXT, 
	{col5} INTEGER,
	FOREIGN KEY (id) REFERENCES Class (teacher))""")

# Student table creation
c.execute(f"""CREATE TABLE IF NOT EXISTS {table3}
	({col1} INTEGER PRIMARY KEY NOT NULL,
	{col2} TEXT, 
	{col6} INTEGER,
	FOREIGN KEY (class) REFERENCES Class (id))""")


# NOW POPULATE THE DATABASE ###

# define some variables
# ended up not using these
class_names = ["Physics", "Mathematics", "English", "History"]
student_names = ["Sean", "Mary", "John", "David", "Jane", 
"Tim", "Kim", "Angel", "Khan", "Ling"]
teacher_names = ["Voon", "Awang"]

# say Physics has 4 students, Math 3, English, 2, History 1
# say Voon teaches Physics and Mathematics, salary 5000
# say Awang teaches History and English, salary 6000

# insertion into Class table
class_sql = f"""INSERT OR IGNORE INTO {table1}
({col2}, {col3}, {col4})
VALUES(?, ?, ?)"""

class_rows = [("Physics", 4, "Voon"), ("Mathematics", 3, "Voon"),
 ("English", 2, "Awang"), ("History", 1, "Awang")]

for i in class_rows:
	#print(i)
	c.execute(class_sql, i)


# insertion into Teacher table
teacher_sql = f"""INSERT OR IGNORE INTO {table2}
({col2}, {col5})
VALUES(?, ?)"""

teacher_rows = [("Voon", 5000), ("Awang", 6000)]

for i in teacher_rows:
	#print(i)
	c.execute(teacher_sql, i)


#  insertion into Student table
student_sql = f"""INSERT OR IGNORE INTO {table3}
({col2}, {col6})
VALUES(?, ?)"""

student_rows = [("Sean", "Physics"), ("Mary", "Physics"), ("John", "Physics"), ("David", "Physics"),
("Jane", "Mathematics"), ("Time", "Mathematics"), ("Kim", "Mathematics"), ("Angel", "History"),
 ("Khan", "History"), ("Ling", "English")]

for i in student_rows:
	#print(i)
	c.execute(student_sql, i)


### select statement to know the class with the most students and who
### their teacher(s) are

c.execute(f"""SELECT name, teacher FROM Class
ORDER BY no_of_students DESC
LIMIT 1""")

# just to be sure it selected one class and one teacher
rows = c.fetchall()
for i in rows:
	print(i)



conn.commit()


conn.close()




