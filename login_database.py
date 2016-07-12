# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:09:45 2016

@author: gramener
"""

import sqlite3
from flask import Flask
app = Flask(__name__)

    
@app.route('/enter_login_details')
def enter_login_details():
    conn=sqlite3.connect("Twitter.db")
    print "Connected to database"
    conn.execute("insert into login_details(ID,username,password) values(?,?,?)",(78011,"usha","An"))
    print "inserted"
    ab=""
    for row in conn.execute('SELECT * FROM login_details'):
        ab+str(row)
    conn.commit()
    conn.close()
    print ab
    return ab;

if __name__ == '__main__':
   app.run(host="127.0.0.1",port=5003,debug=True)