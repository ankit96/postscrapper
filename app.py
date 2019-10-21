__author__ = 'ankit'

import os
from flask import Flask,request, redirect, Response
from postreader import main
import requests
import json
import re
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/post', methods=['post'])
def posting():
    
    text = request.values.get('text')
    #user_name = request.values.get('user_name')
    #user_id = request.values.get('user_id')
    data = main(str(text))
    
    #data = "<@"+str(user_id)+'|'+str(user_name)+'>'+':Top 10 recent post of '+text+' page'+'\n'+str(data)
    return Response(str(data),content_type="text/plain; charset=utf-8" )


@app.route('/')
def hello():
    return redirect('https://github.com/ankit96/postscrapper')


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)

