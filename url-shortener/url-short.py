from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title="Home")

@app.route('/shorten-url')
def shortenUrl():
    return render_template('shortenUrl.html', code=request.args['_code'], url=request.args['_url'])