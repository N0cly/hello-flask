from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
 return 'Hello, World!'

@app.route('/test')
def test():
 return 'On est là, et c/'est déjà bien'
