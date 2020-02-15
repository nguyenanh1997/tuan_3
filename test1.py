from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from OpenSSL import SSL
import os

context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(os.path.dirname(__file__), 'udara.com.crt')
key = os.path.join(os.path.dirname(__file__), 'udara.com.key')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "test1"


    
if __name__ == "__main__":
    context = (cer, key)
    app.run(host='0.0.0.0',port=5001, debug = True, ssl_context=context)
    