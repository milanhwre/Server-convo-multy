from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Facebook Login</h1>
    <p>Login to Facebook and your cookies will be captured to extract the Access Token.</p>
    <p>To proceed, please use your browser's developer tools to copy cookies and send a POST request to <b>/get_token</b>.</p>
    '''

@app.route('/get_token', methods=['POST'])
def get_token():
    cookies = request.form.get('cookies')
    if not cookies:
        return jsonify({"error": "Cookies not provided!"}), 400

    # Setting up headers with the provided cookies
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": cookies,
    }

    # Facebook Graph API request to fetch Access Token
    url = "https://graph.facebook.com/me?fields=id,name"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return jsonify({
            "message": "Access Token successfully extracted!",
            "response": response.json(),
        })
    else:
        return jsonify({
            "error": "Failed to fetch Access Token",
            "details": response.text,
        }), 400

if __name__ == "__main__":
    app.run(port=5000)
