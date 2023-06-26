from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title="Home")

@app.route('/shorten-url', methods=['GET', 'POST'])
def shortenUrl():
    if request.method == 'POST':
        return render_template('shortenUrl.html', code=request.form['_code'], url=request.form['_url'])
    else:
        return "<h2>Invalid request. Change form method to POST</h2>"
