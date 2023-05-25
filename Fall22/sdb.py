import sqlite3
  
# create/connect database
conn = sqlite3.connect('student.db') 
  
# create a cursor object from the cursor class
cur = conn.cursor()

# create a table to hold data
# cur.execute('''
    # CREATE TABLE student_data(
    # name TEXT,
    # lang TEXT,
    # date TEXT,
    # time TEXT,
    # inst TEXT
    # )
# ''')
  
# creating a list of items  
multiple_columns = [('ADEYEMI JOHNSON', 'python', '9/1/22', '10am', 'Chantal Muhumure'),
                    ('MYA TAYLOR', 'java', '9/13/22', '1030am', 'Guadalupe Torres'),
                    ('SEBASTIAN ELLISON', 'python', '9/20/22', '1230pm', '???'),
                    ('GEORGE MARTINEZ', 'python', '9/21/22', '930am', 'Paul Clark'),
                    ('GEORGE MARTINEZ', 'python', '10/4/22', '10am', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '9/13/22', '1230pm', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '9/20/22', '1230pm', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '9/27/22', '930am', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '9/29/22', '1030am', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '10/6/22', '1030am', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '10/18/22', '130pm', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '10/31/22', '1030am', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '11/8/22', '930am', 'Paul Clark'),
                    ('DIEGO GARCIA', 'python', '11/15/22', '10am', 'Paul Clark'),
                    ('TIFFANY BRAZIL', 'python', '9/15/22', '1030am', 'Chantal Muhumure'),
                    ('TIFFANY BRAZIL', 'python', '10/3/22', '9am', 'Chantal Muhumure'),
                    ('RICARDO GONZALES', 'python', '9/22/22', '3pm', 'Robert Garner'),
                    ('RICARDO GONZALES', 'python', '9/27/22', '10am', 'Robert Garner'),
                    ('PATRICK BLOCK', 'C++', '10/3/22', '3pm', 'Chantal Muhumure'),
                    ('GEORGE GABOR', 'C++', '9/28/22', '12pm', 'Chantal Muhumure'),
                    ('DUKE VELAZCO', 'java', '10/20/22', '230pm', 'Guadalupe Torres'),
                    ('DUKE VELAZCO', 'java', '11/3/22', '430pm', 'Guadalupe Torres'),
                    ('DEBRA TRUJILLO', 'web', '10/3/22', '230pm', 'Laura Arguelles'),
                    ('DEBRA TRUJILLO', 'web', '10/3/22', '630pm', 'Laura Arguelles'),
                    ('MONIQUE CANDELARIA', 'python', '10/6/22', '530pm', 'Thomas Gutierrez'),
                    ('MONIQUE CANDELARIA', 'python', '10/13/22', '6pm', 'Thomas Gutierrez'),
                    ('MONIQUE CANDELARIA', 'python', '11/9/22', '1pm', 'Thomas Gutierrez'),
                    ('MARIAH MEDIAN', 'python', '9/13/22', '530pm', 'Paul Clark'),
                    ('MARIAH MEDIAN', 'python', '9/20/22', '230pm', 'Paul Clark'),
                    ('MARIAH MEDIAN', 'python', '10/4/22', '430pm', 'Paul Clark'),
                    ('MARIAH MEDIAN', 'python', '10/11/22', '430pm', 'Paul Clark'),
                    ('MARIAH MEDIAN', 'python', '10/19/22', '3pm', 'Paul Clark'),
                    ('MARIAH MEDIAN', 'python', '11/10/22', '6pm', 'Paul Clark'),
                    ('MARIAH MEDIAN', 'python', '11/15/22', '430pm', 'Paul Clark'),
                    ('HUNG TRAN', 'c', '11/22/22', '5pm', '???'),
                    ('WILLIAM PEACOCK', 'python', '12/1/22', '5pm', 'Chantal Muhumure'),
                    ('PAUL PACHECO', 'python', '8/31/22', '6pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '9/1/22', '6pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '9/13/22', '6pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'sql', '9/20/22', '330pm', 'Hye Clark'),
                    ('PAUL PACHECO', 'python', '9/27/22', '430pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '10/4/22', '6pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '10/11/22', '6pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '10/17/22', '530pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '10/18/22', '3pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '10/31/22', '530pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'sql', '11/1/22', '6pm', 'Hye Clark'),
                    ('PAUL PACHECO', 'sql', '11/2/22', '3pm', 'Hye Clark'),
                    ('PAUL PACHECO', 'python', '11/7/22', '6pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '11/10/22', '4pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '11/15/22', '1pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'sql', '11/21/22', '6pm', 'Hye Clark'),
                    ('PAUL PACHECO', 'sql', '11/23/22', '12pm', 'Hye Clark'),
                    ('PAUL PACHECO', 'sql', '11/28/22', '6pm', 'Hye Clark'),
                    ('PAUL PACHECO', 'python', '11/29/22', '6pm', 'Paul Clark'),
                    ('PAUL PACHECO', 'python', '12/1/22', '630pm', 'Paul Clark'),
                    ('DANIEL ARCHULETA', 'sql', '11/30/22', '1230pm', 'Hye Clark'),
                    ('DANIEL ARCHULETA', 'sql', '11/30/22', '6pm', 'Hye Clark'),
                    ('DANIEL ARCHULETA', 'sql', '12/5/22', '6pm', 'Hye Clark'),
                    ('JESSE GARCIA', 'java', '10/19/22', '12pm', 'Guadalupe Torres'),
                    ('JESSE GARCIA', 'java', '10/20/22', '12pm', 'Guadalupe Torres'),
                    ('JESSE GARCIA', 'java', '11/7/22', '12pm', 'Guadalupe Torres'),
                    ('JESSE GARCIA', 'java', '11/17/22', '1pm', 'Guadalupe Torres'),
                    ('JESSE GARCIA', 'java', '11/22/22', '12pm', 'Guadalupe Torres'),
                    ('JESSE GARCIA', 'java', '10/29/22', '12pm', 'Guadalupe Torres'),
                    ('TRISTAN GUTIERREZ', 'python', '12/1/22', '10am', 'Chantal Muhumure'),
                    ('TRISTAN GUTIERREZ', 'python', '12/1/22', '2pm', 'Chantal Muhumure'),
                    ('TRISTAN GUTIERREZ', 'python', '12/6/22', '130pm', 'Chantal Muhumure'),
                    ('TRISTAN GUTIERREZ', 'python', '12/6/22', '5pm', 'Chantal Muhumure')]
  
#cur.executemany("INSERT INTO student_data VALUES (?,?,?,?,?)", multiple_columns)
 
cur.execute("SELECT * FROM student_data")
results = cur.fetchall()
for i in results:
    print(i)
 
 
# committing our connection
conn.commit()
  
# close our connection
conn.close()
