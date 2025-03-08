# Web Security Project - Fortnite

## User Manual

### 1. Overview

This application uses Flask to search data indexed in an Apache Solr server. Users can enter query criteria to see matching results.

---

### 2. System Requirements

1. **Operating System:** Tested on Kali. Should also work on other Linux distros.  
2. **Python 3.9+** (with pip)  
3. **Apache Solr** (version 8 or later)

---

### 3. Prerequisites

1. **Install Java**  
   Apache Solr requires Java. Install the default JDK:
   ```bash
   sudo apt-get update
   sudo apt-get install -y default-jdk

2. **Install Apache Solr (Binary Distribution)**

   Download the latest binary (not the source) Solr tarball from solr.apache.org/downloads.html.
    Extract the file:
   ```bash
   tar xvf solr-<version>.tgz

3. **Start Solr**
   Navigate into the extracted Solr folder and start Solr on the default port (8983):
   
       cd solr-<version>
       bin/solr start
   Verify Solr is running by opening your browser to http://127.0.0.1:8983/solr/.

4. **Create the "fortnite" core**
   In the same folder where Solr is extracted:
   ```bash
   bin/solr create -c fortnite
  This creates a new Solr core named fortnite, which the Flask app will query.

## 4. Project Setup

1. **Obtain the Project Files**  
   - Clone this repository (which contains the following files) into a local folder on your machine, for example `WebSecProj`:
     - `main.py`
     - `index.html`
     - `results.html`
     - `requirements.txt`
     - `README.md`

2. **Create a Python Virtual Environment (Recommended)**  
   ```bash
   cd ~/Desktop/WebSecProj-ui
   python3 -m venv venv
   source venv/bin/activate

3. **Install Required Dependencies **
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
  This will install Flask, requests, pandas, and other libraries needed to run the application.

## 5. Configuration

Inside **`main.py`**, ensure the Solr URLs match where you have Solr running. For example:

    ```python
    def fieldnames():
        r = requests.get("http://127.0.0.1:8983/solr/fortnite/select?q=*:*&wt=csv&rows=0&facet")
        return r.content.decode().strip().split(",")
If you’re running Solr on a different port or with a different core name, edit the URLs accordingly.

## 6. Running the Application

1. **Start Solr (if it’s not already running)**
   ```bash
   bin/solr start
   ```
If you installed Solr as a service, you can use:
  ```bash
  sudo service solr start
 ```

2. **Activate the Python Virtual Environment (if used)**
   ```bash
   cd ~/Desktop/WebSecProj-ui
   source venv/bin/activate

3. **Launch the Flask App**
   ```bash
   python main.py
Flask will start on http://127.0.0.1:5000 by default.

## 7. Using the Search Page

1. **Open a Web Browser**  
   Go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

2. **Select a Field and Condition**  
   - You’ll see a dropdown for Solr fields (fetched from Solr).
   - Choose a “match” type (e.g., **is**, **contains**, **starts with**, **ends with**).
   - Enter the text to search for in the input field.

3. **Add or Remove More Queries**  
   Use the **plus (+)** and **minus (–)** buttons to add or remove rows for more query criteria.

4. **Submit Your Search**  
   - Click the **Submit** button.
   - You’ll be taken to a results page showing how many documents matched and details for each matching document.

---

## 8. Troubleshooting

- **Connection Refused (port 7574)**  
  If you see an error like:
```bash
requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=7574)...
```
That means the code is pointing to the wrong port for Solr. Update it to **8983** or run Solr on **7574** by specifying `-p 7574` when starting Solr.

## 9. Stopping the Application

1. **Stop Flask**  
   Press **CTRL + C** in the terminal where `python excelsior.py` is running.

2. **Deactivate Virtual Environment (optional)**  
   ```bash
   deactivate

3. **Stop Solr (if needed)**
    ```bash
    bin/solr stop
    ```
    or
   ```bash
   sudo service solr stop
   ```
