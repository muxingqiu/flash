from flask import Flask
from config import DEBUG
from helper import is_key_or_isbn

app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def hello(q,page):
    is_key_or_isbn(q)
    pass

#这里可以指定host地址，host = 'IP',port = '端口'
#如果没有这一句，那么flash直接导入到其他模块，那么就会被执行
if __name__ == "__main__":
    app.run(debug=DEBUG)