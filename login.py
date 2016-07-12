# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:56:45 2016

@author: gramener
"""
from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('contact.html', form = form)


if __name__ == '__main__':
   app.run(host="127.0.0.1",port=5001,debug = True)
