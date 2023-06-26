from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# route to main page
@app.route('/')
def index():
    return render_template('index.html',title="Home")

# route to shortenUrl, on form submission
#                           specify form methods
@app.route('/shorten-url', methods=['GET', 'POST'])
def shortenUrl():
    # check form method and throw error if not POST
    if request.method == 'POST':
        # create dictionary to store urls
        urls = {}
        urls[request.form["_code"]] = {'url': request.form['_url']}

        # create json file
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)

        return render_template('shortenUrl.html', code=request.form['_code'], url=request.form['_url'])
    else:
        # redirect to (the url for (index function))
        return redirect(url_for('index'))
