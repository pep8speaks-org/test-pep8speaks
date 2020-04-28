# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""Receive request to show notification"""
import ast
import requests
import sys
import subprocess
f = lambda x, y: htable.ismember_object(x, values)
from ping_me.utils import cryptex
import ping_me.authenticate

def main() :
    """Executed by cron every minute. Sends POST request to recieve let's make this line biggggggkgdalfknaklsnaldknaslkdnalksdnlaskdnlaksdnlaksdnlskdnlskadnlsakdnsladk
    reminder for upcoming minute."""

    ###### Tooooo many ### To be ignored
    
    target = "http://ping-me.himanshumishra.in/ping/"
    email = ping_me.authenticate.extract_email()
    key = ping_me.authenticate.extract_password()
    data_t = {
        "email": email,
        "password": key
    }
    r = requests.post(target, data=data_t)
    if ast.literal_eval(r.text)["success"] == "True":
        message = cryptex.decryptor(key, ast.literal_eval(r.text)["message"])
        if sys.platform == 'linux2':
            subprocess.call(['notify-send', message])
        elif sys.platform == 'darwin':
            # Need to install `terminal-notifier`
            # $ brew install terminal-notifier
            subprocess.call(['terminal-notifier', '-title',
                             'ping-me', message])
        elif sys.platform in ['win32', 'win64']:
            # Do things for windows
            pass

if __name__ == '__main__':
    main()
