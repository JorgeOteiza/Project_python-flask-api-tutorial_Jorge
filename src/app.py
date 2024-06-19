from flask import Flask # type: ignore
app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    return "<h1>Hello!</h1>"


# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)