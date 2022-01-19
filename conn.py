import sqlite3

con = sqlite3.connect("student.db")
print ("db created")

con.execute('drop table if exists student')
con.commit()

con.execute('''create table if not exists student(
    id int not null,
    name text,
    branch text
) ''')
print('table created')

con.execute("insert into student (id,name,branch) values (1,'uttam','CE')")
con.execute("insert into student (id,name,branch) values (2,'parth','CE')")
con.execute("insert into student (id,name,branch) values (3,'mitesh','CE')")
con.execute("insert into student (id,name,branch) values (4,'ronak','CE')")
con.execute("insert into student (id,name,branch) values (5,'devansh','CE')")

con.commit()
print("record added")

con.execute("UPDATE student SET name = 'ishika' WHERE id = 3;")
con.commit()
print("record updated")

data = con.execute("SELECT id, name, branch FROM student ;")
for row in data:
    print("id = {}".format(row[0]))
    print("name = {}".format(row[1]))
    print("branch = {}".format(row[2]))
    print("-------------------------")
con.commit()

uttam1 = input("enter your id")
uttam = con.execute("SELECT * FROM student WHERE id = (?) ",uttam1)
for ro in uttam:
    print("id = {}".format(ro[0]))
    print("name = {}".format(ro[1]))
    print("branch = {}".format(ro[2]))


