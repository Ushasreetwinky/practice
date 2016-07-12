# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:02:34 2016

@author: gramener
"""

import sqlite3

def retrieve():
    conn = sqlite3.connect('Twitter.db')
    ab=""
    for row in conn.execute('SELECT * FROM login_details'):
        ab=ab+"\n"+str(row)
    conn.close()
    return ab

def insert(user_id,name,password):
     conn = sqlite3.connect('Twitter.db')
     conn.execute("insert into login_details(ID,username,password) values(?,?,?)",(user_id,name,password))
     conn.commit()
     conn.close()

def delete_row(user_id):
    conn = sqlite3.connect('Twitter.db')
    query="delete from login_details where ID="+str(user_id)
    conn.execute(query)
    conn.commit()
    conn.close()
     
     
print(retrieve())
delete_row(78006)
print(retrieve())