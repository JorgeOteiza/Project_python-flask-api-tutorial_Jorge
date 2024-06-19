from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to my portfolio!"

@app.route('/about-me')
def about_me():
    return "This is the about me page."

@app.route('/contact-me')
def contact_me():
    return "This is the contact me page."

if __name__ == '__main__':
    app.run(debug=True)