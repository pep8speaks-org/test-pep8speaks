# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""Receive request to show notification"""
import ast
import requests
import sys
import subprocess

from ping_me.utils import cryptex
import ping_me.authenticate
iteral_eval(r.text)["success"] == "True":
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

if __name__ == '__main__' :
    main()
