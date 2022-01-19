from connectproduct import *
import sqlite3
conn1=sqlite3.connect("products.db")
status=1
while(status):
    ch=int(input("1.insert\n2.delete\n3.show table's details\n4.update\n5.exit\nplease choose opration:"))
    if ch==1:
        i=insertq()
        i.show1()
    if ch==2:
        d=deleteq()
    if ch==3:
        s=selectq()
    if ch==4:
        u=updateq()
    if ch==5:
        status = 0
