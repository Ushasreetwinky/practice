# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:37:51 2016

@author: gramener
"""

from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators

class ContactForm(Form):
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   name = TextField("Password",[validators.Required("Please enter your password.")])
   submit = SubmitField("Send")