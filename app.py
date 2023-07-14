from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form['topic']
    # Fetch the summary of the topic from Wikipedia
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}")
    if response.status_code == 200:
        content = response.json()['extract']
    else:
        content = "Failed to generate content. Please try again later."
    return render_template('result.html', content=content)

if __name__ == '__main__':
    app.run()
