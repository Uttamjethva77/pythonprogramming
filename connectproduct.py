import sqlite3
conn1=sqlite3.connect("products.db")
conn1.execute('''create table if not exists product(id number(10),pname varchar(20),cost int(10))''')
class insertq:
    def __init__(s):
        a=str(input("enter product id :"))
        b=str(input('enter product name:'))
        c=str(input('enter product cost:'))
        insert="insert into product values(" +a+ ",'"+b+"','"+c+"')"
        conn1.execute(insert)
        conn1.commit()
    def show1(s):
        print("record inserted Successfully")
class selectq:
    def __init__(s):
        show=conn1.execute("select * from product")
        for r in show:
            print("id={}".format(r[0]))
            print("product name={}".format(r[1]))
            print("product cost={}".format(r[2]))
            print("*****************")
class deleteq:
    def __init__(s):
        id=input("enter Id:")
        q='delete from product where id='+id
        conn1.execute(q)
        conn1.commit()
class updateq:
    def __init__(s):
        id=(input("enter id:"))
        w=str(input("enter product name"))
        q="update product set pname ='"+w+"' where id="+id
        print(q)
        conn1.execute(q)
        conn1.commit()
