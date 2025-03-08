from flask import Flask, render_template, request, jsonify
import requests
import os
from flask_dropzone import Dropzone

app = Flask(__name__)
dropzone = Dropzone(app)

@app.route('/')
def index():
    headers = fieldnames()
    return render_template('index.html', headers=headers)


@app.route('/search', methods=['POST'])
def search():
    fullvarstring = ""
    for i in range(1, int(len(request.form)/3)+1):
        header = request.form.get(f"header{i}")
        match = request.form.get(f"match{i}")
        string = request.form.get(f'string{i}')
        
        #handle request prob through dedicated def
        q = handle_query(header,match,string)
        if (i == 1):
            fullvarstring += f"q={q}"
        else:
            fullvarstring += f"&fq={q}"
        if request.form.get("start"):
            start = request.form.get("start")
            fullvarstring+= f"&start={start}"
        fullvarstring+= "&q.op=AND"
    print(f"lol:{fullvarstring}")
    r = requests.get(f"http://127.0.0.1:8983/solr/fortnite/select?{fullvarstring}").json()
    start = r['response']['start']
    numFound = r['response']['numFound']
    docs = r['response']['docs']
    
    blur = False if (request.form.get("blur") is None) else True
    return render_template('results.html',numFound=numFound, docs=docs, blur=blur,start=start, fullvarstring=fullvarstring)

@app.route('/api/fieldnames')
def fieldnames():
    r = requests.get(f"http://127.0.0.1:8983/solr/fortnite/select?q=*:*&wt=csv&rows=0&facet")
    return r.content.decode().strip().split(",")


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == "POST":
        try:
            file = request.files['file']
            file.save(os.path.join('/tmp',file.filename))
            #upload to solr
            return render_template('upload.html', status="Success")
        except:
            return render_template('upload.html', status="Failed")
    else:
        return render_template('upload.html')

def get_url():
    try:
        with open("url.txt", "r") as f:
            line = f.readline()
        return line
    except:
        return None

def handle_query(header, match, string): #TO MOVE TO A SEPERATE PY FILE LATER
    if (header == "email"):
        header = "email_str" #fix for text vs str search
    if (match == "is"):
        return f"{header}:{string}"
    elif (match == "contains"):
        return f"{header}:*{string}*"
    elif (match == "starts with"):
        return f"{header}:{string}*"
    elif (match == "ends with"):
        return f"{header}:*{string}"
    elif (match == "regex"):
        return f"{header}:/{string}/"

if __name__ == '__main__':
    app.run(debug=True)
