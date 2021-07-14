from flask import Flask

app = Flask(__name__)

@app.route('/')  # controller부분, /로 시작하는 값들은 여기서 처리함.
def hello_world():         

    # HTML을 return 해줄수도 있음(''' ''') 안에 넣어야함.
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>플라스크 페이지</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
    </head>
    <body>
        <h1>Hello Flask </h1>
        <h3>제목줄입니다</h3>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

