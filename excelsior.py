from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    headers = fieldnames()
    return render_template('drain.html', headers=headers)


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
        print(fullvarstring)
    r = requests.get(f"http://127.0.0.1:8983/solr/test3/select?{fullvarstring}").json()
    
    numFound = r['response']['numFound']
    
    docs = r['response']['docs']
    
    #print(r.response.docs)
    return render_template('results.html', numFound=numFound, docs=docs)
    
@app.route('/api/fieldnames')
def fieldnames():
    r = requests.get(f"http://127.0.0.1:7574/solr/test3/select?q=*:*&wt=csv&rows=0&facet")
    return r.content.decode().strip().split(",")



def handle_query(header, match, string): #TO MOVE TO A SEPERATE PY FILE LATER
    if (match == "is"):
        return f"{header}:{string}"
    elif (match == "contains"):
        return f"{header}:*{string}*"
    elif (match == "starts with"):
        return f"{header}:{string}*"
    elif (match == "ends with"):
        return f"{header}:*{string}"

if __name__ == '__main__':
    app.run(debug=True)
