# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:01:30 2016

@author: gramener
"""
import sqlite3 

db=sqlite3.connect('Twitter.db')

def login_check(username,password):
    cursor = db.cursor() 
    query="select password from login_details where username=\""+username+"\""
    query2="select id from login_details where username=\""+username+"\""
    pswrd=cursor.execute(query)
    db.commit()
    ab=""
    for i in pswrd:
       ab=str(i[0])
    if password==ab:
        for i in cursor.execute(query2):
            return str(i[0])
    return password==ab

def follow(following_id,follower_id):
    cursor=db.cursor()
    query="select count(*) from login_details where ID in ("+str(following_id)+","+str(follower_id)+")"
    for row in cursor.execute(query):
        if str(row[0])=="2":
            query2="insert into followers(id,follower) select "+str(following_id)+","+str(follower_id)+" where not exists (select 1 from followers where id="+str(following_id)+" and "+"follower="+str(follower_id)+")"       
            cursor.execute(query2)
    db.commit()
    
def retrieve_followers(ID):
    cursor=db.cursor()
    query="select follower from followers where id="+str(ID)
    followers=[]
    for row in cursor.execute(query):
        followers.append(row[0])
    return followers
    
def retrieve_following(ID):
    cursor=db.cursor()
    query="select id from followers where follower="+str(ID)
    following=[]
    for row in cursor.execute(query):
        following.append(row[0])
    if not following:
        return
    return following

def get_my_tweets(ID):
    cursor=db.cursor()
    query="select tweet from tweets where id="+str(ID)
    tweets=[]
    for row in cursor.execute(query):
        tweets.append(str(row[0]))
    return tweets

def insert_tweet(ID,tweet):
    cursor=db.cursor()
    cursor.execute("insert into tweets(id,tweet) values(?,?)",(ID,tweet))
    
def get_tweets(ID):
    tweets=[]
    following=retrieve_following(ID)
    following.append(ID)
    for ids in following:
        tweet=get_my_tweets(ids)
        if tweet:
            for twet in tweet:
                tweets.append(twet)
    return tweets

def unfollowing(ID):
    cursor=db.cursor()
    following=retrieve_following(ID)
    str_follow=""
    unfollow=[]
    for i in following:
        if str_follow=="":
            str_follow+=str(i)
        else:
            str_follow+=","+str(i)
    query="select id from login_details where id not in ("+str_follow+")"
    for a in cursor.execute(query):
        unfollow.append(int(a[0]))
    print unfollow
#insert_tweet(78011,"hi tweet")
#print(get_my_tweets(78004))
#print(retrieve_followers(78004))
follow(78011,78004)
#print(login_check("usha","An"))
print(retrieve_following(78004))
unfollowing(78004)
print(get_tweets(78004))