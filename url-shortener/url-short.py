from flask import Flask, render_template, request, redirect, url_for, flash
import json, os.path as tap

app = Flask(__name__)
app.secret_key = 'abracadabra'

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
    
        # check if file exists
        if tap.exists('urls.json'):
            with open('urls.json', 'r') as urls_file:
                urls = json.load(urls_file)
        if request.form['_code'] in urls.keys():
            flash('Record already exists!')
            return redirect(url_for('index'))

        urls[request.form["_code"]] = {'url': request.form['_url']}
        # create json file
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)

        return render_template('shortenUrl.html', code=request.form['_code'], url=request.form['_url'])
    else:
        # redirect to (the url for (index function))
        return redirect(url_for('index'))

# route to redirect to code entered
@app.route('/<string:code>')
# function takes in the code entered as argument
def redirectToUrl(code):
    # check if file exists
    if tap.exists('urls.json'):
        # open file
        with open('urls.json', 'r') as urls_file:
            # load file to dictionary
            urls = json.load(urls_file)
            # if argument parsed(code) is a key in the loaded dictionary
            if code in urls.keys():
                # check if the url of the code entered is present
                if 'url' in urls[code].keys():
                    # redirect to the
                    return(redirect(urls[code]['url']))
                        
