from flask import Flask
import logging
import sys
import requests

app = Flask(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async 
src="https://www.googletagmanager.com/gtag/js?id=UA-251004345-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', ' YOUR_GA_CODE');
</script>
 """
 #return prefix_google + "Hello World"

 suffix_google = """
<button onClick="ga('send', 'event', 'button', 'click', 'Label');">Click</button>
"""
 return prefix_google + "Hello World" + suffix_google

@app.route('/LOGGER', methods = ["GET"])
def logger():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async 
src="https://www.googletagmanager.com/gtag/js?id=UA-251004345-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', ' YOUR_GA_CODE');
</script>
 """
 return prefix_google + "logger"



@app.route('/google', methods=["GET"])
def request():
    req =  requests.get("https://www.google.com/")
    return req.cookies.get_dict()

@app.route('/ganalytics', methods=["GET"])
def request_a():
    req = requests.get("https://analytics.google.com/analytics/web/?hl=fr#/report-home/a251004345w345067405p281210810")
    # payload = {'inUserName': 'anhkim.chaloupe@gmail.com', 'inUserPass': 'PASSWORD'}
    # url = 'http://www.locationary.com/home/index2.jsp'
    # requests.post(url, data=payload)
    return req.text