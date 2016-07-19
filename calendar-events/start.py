

#!/usr/bin/python

import datetime
import sqlite3
import calendar
from flask import Flask, render_template, request,session
from flask_bootstrap import Bootstrap
import sqlite3
from flask_mail import Mail, Message

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'Ushasree28%22@9.1993'
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testemailmandrill@gmail.com'
app.config['MAIL_PASSWORD'] = 'mandrill'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def index(msg1):
   msg = Message('Hello', sender = 'testemailmandrill@gmail.com', recipients = ['ushasree.ginne@gramener.com'])
   msg.body = msg1
   mail.send(msg)
   return "Sent"

@app.route('/')
def month():
	session['month']='0'
	session['year']='0'
	ab=presentMonth() 
	month=[present()]
	events=get_events(int(session['month']),int(session['year']))
	return render_template("bootstrap_demo.html",ab=ab,events=events,month=month)

@app.route('/eventsupdates',methods=['POST','GET'])
def eventsupdates():
	result=request.form
	updateEvent(result['date'],result['month'],result['year'],result['eventdetails'])
	ab=presentMonth() 
	month=[present()]
	events=get_events(int(session['month']),int(session['year']))
	return render_template("bootstrap_demo.html",ab=ab,events=events,month=month)

@app.route('/deleteevent',methods=['POST','GET'])
def delete():
	result=request.form
	dit=result['eventdate']
	print dit," dit "
	dt=dit.split(" : ")[0].split("-")
	deleteEvent(int(dt[0]),int(dt[1]),int(dt[2]))
	ab=presentMonth() 
	month=[present()]
	events=get_events(int(session['month']),int(session['year']))
	return render_template("bootstrap_demo.html",ab=ab,events=events,month=month)

@app.route('/monthchange',methods=['POST','GET'])
def monthchange():
	result=request.form
	monthsPandN(int(result['reduce']))
	ab=eventsWithDate(session['month'],session['year'])
	month=[present()]
	events=get_events(int(session['month']),int(session['year']))
	return render_template("bootstrap_demo.html",ab=ab,events=events,month=month)

@app.route('/monthchange2',methods=['POST','GET'])
def monthchange2():
	result=request.form
	monthsPandN(int(result['add']))
	ab=eventsWithDate(session['month'],session['year'])
	month=[present()]
	events=get_events(int(session['month']),int(session['year']))
	return render_template("bootstrap_demo.html",ab=ab,events=events,month=month)

""".. to insert an event by checking whether there was an event already"""
def insertEvent(day,month,year,event):
	conn = sqlite3.connect('calendar.db')
	EDATE = str(day)+'-'+str(month)+'-'+str(year)
	print EDATE
	query1 = "SELECT EVENT from CALENDAR where IDATE="+EDATE
	print query1
	cursor = conn.execute(query1)
	print str(cursor)
	i=0
	for i in cursor:
		print i
	if i == 0:
		conn.execute("INSERT INTO CALENDAR (IDATE,DAY,MONTH,YEAR,EVENT) VALUES (?,?,?,?,?)",(EDATE,day,month,year,event));
		print "Inserted into database successfully"
	else:
		print "insuccessfull"
	conn.commit()
	conn.close()

"""
.. to update an event by checking whether there was an event already"""
def updateEvent(day,month,year,event):
	conn = sqlite3.connect('calendar.db')
	EDATE = str(day)+'-'+str(month)+'-'+str(year)
	print EDATE
	query1 = "SELECT EVENT from CALENDAR where IDATE=\""+EDATE+"\""
	print query1
	cursor = conn.execute(query1)
	i=0
	for a in cursor:
		print a
		i = 1
	if i == 0:
		conn.execute("INSERT INTO CALENDAR (IDATE,DAY,MONTH,YEAR,EVENT) VALUES (?,?,?,?,?)",(EDATE,day,month,year,event));
		print "Inserted into database successfully"
	else:
		query2 = "UPDATE CALENDAR set EVENT = \""+event+"\" where IDATE=\""+EDATE+"\""
		conn.execute(query2);
	conn.commit()
	msg="New event :("+event+") is created on "+EDATE
	index(msg)
	conn.close()

	
""".. to delete an event by checking whether there was an event already"""
def deleteEvent(day,month,year):
	conn = sqlite3.connect('calendar.db')
	EDATE = str(day)+'-'+str(month)+'-'+str(year)
	query1 = "SELECT EVENT  from CALENDAR where IDATE=+\""+EDATE+"\""
	cursor = conn.execute(query1)
	i=0
	ab=""
	for a in cursor:
		ab=str(a[0])
		i=1
	if i == 0:
		print "deletion in database unsuccessfull"
	else:
		query2 = "DELETE from CALENDAR where IDATE=\""+EDATE+"\""
		conn.execute(query2);
	conn.commit()
	msg="Your event :("+ab+") on "+EDATE+" is removed"
	index(msg)
	conn.close()

def presentMonth():
	now = datetime.datetime.now()
	res=eventsWithDate(int(now.month),int(now.year))
	session['month']=now.month
	session['year']=now.year
	return res

def dates(mm,yyyy):
	cal= calendar.Calendar()
	st = []
	st1 = []
	i=0
	for x in cal.itermonthdates(yyyy, mm):
		#print "hi","     :   ",i
		st.append(str(x).split("-")[2])
		#print st
		i += 1
		if i%7==0:
			st1.append(st)
			st=[]
		#print st1
	return st1

def monthsPandN(mon):
	month=session['month']
	year=session['year']
	if month == 1 and mon==-1:
		year = year-1
		month = 12
	elif month == 12 and mon==+1:
		year = year+1
		month = 1
	else:
		month = month + mon
	session['month']=month
	session['year']=year

def get_events(mm,yyyy):
	conn = sqlite3.connect('calendar.db')
	query1 = "SELECT IDATE,EVENT  from CALENDAR where MONTH=+\""+str(mm)+"\" and YEAR=+\""+str(yyyy)+"\""
	#Sprint query1
	cursor = conn.execute(query1)
	events = []
	for a in cursor:
		events.append(a[0]+" : "+a[1])
	return events

def present():
	months=['January','February','March','April','May','June','July','August','September','october','November','December']
	return months[int(session['month'])-1]+","+str(session['year'])


def eventsWithDate(mm,yyyy):
	cal= calendar.Calendar()
	st=[]
	i=0
	for x in cal.itermonthdates(yyyy, mm):
		day = int(str(x).split("-")[2])
		month = int(str(x).split("-")[1])
		year = int(str(x).split("-")[0])
		conn = sqlite3.connect('calendar.db')
		dt = str(day)+"-"+str(month)+"-"+str(year)
		query1 = "SELECT EVENT  from CALENDAR where IDATE=+\""+dt+"\""
		cursor = conn.execute(query1)
		i=0
		for a in cursor:
			st.append(str(x).split("-")[2]+" \n"+a[0])
			i=1
		if i == 0:
			st.append(str(x).split("-")[2])
	result = listOfLists(st)
	return result

def listOfLists(st2):
    st = []
    st1 = []
    i=0
    for x in st2:
        st.append(x)
        i += 1
        if i%7==0:
            st1.append(st)
            st=[]
    return st1


if __name__ == '__main__':
   app.run(debug = True)
