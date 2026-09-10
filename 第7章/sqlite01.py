#!/usr/bin/env python3.6
# coding: utf-8
import sqlite3
def create_table():
    exist=False
    conn=sqlite3.connect('db/sqlite3.db')
    print("Opened database successfully")
    c=conn.cursor()
    rt=c.execute('SELECT name FROM sqlite_master WHERE type="table"')
    for row in rt:
        if row[0].lower()=='table1':
            exist=True
            break
    if not exist:
        c.execute('CREATE TABLE table1(name TEXT NOT NULL,\
            age INT NOT NULL, height REAL)')
        print("Table created successfully!")
    else:
        print('Table is existed!')
    conn.commit()
    conn.close()
def insert_reacord():
    conn=sqlite3.connect('db/sqlite3.db')
    c=conn.cursor()
    c.execute("INSERT INTO table1(name,age,height) \
      VALUES('Zhao', 16, 1.77 )");
    c.execute("INSERT INTO table1(name,age,height) \
      VALUES('Qian', 17, 1.78 )");
    c.execute("INSERT INTO table1(name,age,height) \
      VALUES('Sun', 18, 1.79 )");
    c.execute("INSERT INTO table1(name,age,height) \
      VALUES ('Li', 19, 1.8 )");
    conn.commit()
    conn.close()
    print("Records created successfully!")
def select_record():
    conn=sqlite3.connect('db/sqlite3.db')
    c=conn.cursor()
    cursors=c.execute("SELECT name, age, height  from table1")
    for row in cursors:
        print("NAME=", row[0],"AGE=", row[1], "HEIGHT=", row[2])
    print("Select operation successfully!")
    conn.close()
def update_record():
    conn=sqlite3.connect('db/sqlite3.db')
    c=conn.cursor()
    c.execute("UPDATE table1 set height=1.82 where name='Zhao'")
    conn.commit()
    conn.close()
    print("Update record successfully!")
def delete_record():
    conn=sqlite3.connect('db/sqlite3.db')
    c=conn.cursor()
    c.execute("DELETE from table1 where name='Sun'")
    conn.commit()
    conn.close()
    print("delete record successfully!")
create_table()
insert_reacord()
select_record()
update_record()
select_record()
delete_record()
select_record()
