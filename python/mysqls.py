import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="aju"
)
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(20)NOT NULL,
               age INT,
               gender VARCHAR(10),
               email VARCHAR(50)UNIQUE,
               phone_no VARCHAR(15)UNIQUE,
               address TEXT)
               """)



cursor.execute("""  
INSERT INTO student(name,age,gender,email,phone_no,address)VALUES
               
               ("Anjal",25,"male","anjal@gmail.com","7994413795","koranath(H)karkkidamkunnu po")
                  
 """)

# cursor.execute(""" 
#                 UPDATE student 
#                 SET email="adarsh@gmail.com",name="adarsh"WHERE name="Anjal"      
               
#                """)


# cursor.execute("SELECT * FROM student")
# rows=cursor.fetchall()
# for row  in rows:
#     print(row)



# cursor.execute("""
# DELETE FROM student WHERE name="An"
#  """)

connection.commit()
connection.close()


