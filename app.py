from flask import Flask, request, redirect
import requests, os
from bs4 import BeautifulSoup as bs
import json, base64
from urllib.parse import *
from lib.wiki import wiki

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("http://github.com/caliph91/textmaker-api", code=302)

@app.route('/api/wikipedia', methods=['GET', 'POST'])
def wikipedia():
   if request.args.get('text')
     wikii = wiki.wikipedia(request.args.get('text'))
     for i in wikii:
     return wikii
  else:
     return { 'success': False, message: 'masukkan parameter text' }


@app.route('/api/nulis', methods=['GET','POST'])
def noolees():
    from lib.nulis import tulis, imageToBase64
    if request.args.get('text'):
            nulis = tulis(unquote(request.args.get('text')))
            for i in nulis:
                i.save('resolt.jpg')
                url = 'https://api.imgbb.com/1/upload'
                par = {
                   'key':'c93b7d1d3f7a145263d4651c46ba55e4',
                   'image': imageToBase64('resolt.jpg')
                      }
                headers = {
                'Accept': 'application/json'
                          }
                req = requests.post(url,data=par, headers=headers)
                p = req.json()['data']['display_url']
                return {
                    'status': 200,
                   'result': p
                }
    else:
        return {
            'status': False,
            'msg': '[!] Masukkan parameter text'
        }


@app.route('/api/textmaker', methods=['GET'])
def makerr():
    from lib.textmaker import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'c93b7d1d3f7a145263d4651c46ba55e4',
         'image':image_64_encode
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
         "results":p
         }
        return js

@app.route('/api/textmaker2', methods=['GET'])
def makerr2():
    from lib.textmaker2 import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'c93b7d1d3f7a145263d4651c46ba55e4',
         'image':image_64_encode
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
         "results":p
         }
        return js

@app.route('/api/textmaker3', methods=['GET'])
def makerr3():
    from lib.textmaker3 import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'c93b7d1d3f7a145263d4651c46ba55e4',
         'image':image_64_encode
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
         "results":p
         }
        return js

@app.route('/api/textmaker4', methods=['GET'])
def makerr4():
    from lib.textmaker4 import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'c93b7d1d3f7a145263d4651c46ba55e4',
         'image':image_64_encode
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
         "results":p
         }
        return js

@app.route('/api/text3d', methods=['GET'])
def tigadimensi():
    from lib.text3d import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'c93b7d1d3f7a145263d4651c46ba55e4',
         'image':image_64_encode
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
         "results":p
         }
        return js

@app.route('/api/text3d-2', methods=['GET'])
def tigadimensi2():
    from lib.text3dke2 import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'c93b7d1d3f7a145263d4651c46ba55e4',
         'image':image_64_encode
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
         "results":p
         }
        return js

@app.route('/api/text3d-3', methods=['GET'])
def tigadimensi3():
    from lib.text3dke3 import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'c93b7d1d3f7a145263d4651c46ba55e4',
         'image':image_64_encode
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
         "results":p
         }
        return js

@app.route('/api/text3d-4', methods=['GET'])
def tigadimensi4():
    from lib.text3dke4 import tulis
    text = request.args.get('text')
    tulis=tulis(text)
    for i in tulis.tulis():
        i.save('gambar.jpg')
        image = open('gambar.jpg', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        url = 'https://api.imgbb.com/1/upload'
        par = {
         'key':'c93b7d1d3f7a145263d4651c46ba55e4',
         'image':image_64_encode
         }
        headers = {
         'Accept': 'application/json'
         }
        req = requests.post(url,data=par, headers=headers)
        p = req.json()['data']['display_url']
        js = {
         "results":p
         }
        return js


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT','80')),debug=True)

