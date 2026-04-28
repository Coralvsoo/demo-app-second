from flask import Flask, jsonify

application = Flask(__name__)

@application.route('/')
def hello():
    return '<h1>Hello from CI/CD, Special demo for group 302 AI and For Dildora because she is sleeping!</h1>', 200

@application.route('/health')
def health():
    return jsonify(status='ok'), 200

if __name__ == '__main__':
    application.run()