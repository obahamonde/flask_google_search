from bs4 import BeautifulSoup
from requests import Session
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/<query>', methods=['POST'])
def search(query:str)->dict:
    url = f'https://www.google.com/search?q={query}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    response = Session().get(url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    els = soup.find_all('div', class_='yuRUbf')
    response = [ {"title": el.find('h3').text, "link": el.find('a')['href']} for el in els]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)