from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leaks (id INTEGER PRIMARY KEY, data TEXT)''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    for _, row in df.iterrows():
        c.execute('INSERT INTO leaks (data) VALUES (?)', (str(row.to_dict()),))
    conn.commit()
    conn.close()

    return jsonify({'success': 'File uploaded and processed'})


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT data FROM leaks WHERE data LIKE ?", (f'%{query}%',))
    results = [row[0] for row in c.fetchall()]
    conn.close()
    return jsonify(results)


@app.route('/delete', methods=['POST'])
def delete_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM leaks")
    conn.commit()
    conn.close()
    return jsonify({'success': 'All data deleted from the database'})


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
