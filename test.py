from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from OpenSSL import SSL
import os

context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(os.path.dirname(__file__), 'udara.com.crt')
key = os.path.join(os.path.dirname(__file__), 'udara.com.key')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    resp = make_response("Setting a cookie")
    resp.set_cookie('foo','bar', httponly=True, secure=True )
    return resp

@app.route('/test', methods=['GET'])
def test():
    resp = make_response(redirect("https://0.0.0.0:5001"))
    return resp

@app.route('/t', methods=['GET'])
def t():
    return 's'
    
if __name__ == "__main__":
    context = (cer, key)
    app.run(host='0.0.0.0',port=5000, debug = True,ssl_context=context)
    