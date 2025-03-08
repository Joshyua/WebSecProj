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
       bin/solr start -e cloud
---

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

## 5. Running the Application

1. **Start Solr (if it’s not already running)**
   ```bash
   bin/solr start -e cloud
   ```
   
2. **Activate the Python Virtual Environment (if used)**
   ```bash
   cd ~/Desktop/WebSecProj-ui
   source venv/bin/activate

3. **Launch the Flask App**
   ```bash
   python main.py
Flask will start on http://127.0.0.1:5000 by default.

## 6. Using the Search Page

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

## 7. Stopping the Application

1. **Stop Flask**  
   Press **CTRL + C** in the terminal where `python main.py` is running.

2. **Stop Solr (if needed)**
    ```bash
    bin/solr stop
    ```
