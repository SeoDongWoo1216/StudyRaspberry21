from flask import Flask

app = Flask(__name__)

@app.route('/')  # controller부분, /로 시작하는 값들은 여기서 처리함.
def hello_world():
    return 'Hello Flask'

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

