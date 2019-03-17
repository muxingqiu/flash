from flask import blueprints, Blueprint
from helper import is_key_or_isbn
from yushu_book import yushu_book
from flask import jsonify

web = Blueprint('web',__name__)

@web.route('/book/search/<q>/')
def hello(q):
    if is_key_or_isbn(q) == "isbn":
        request = yushu_book.yushu_book_isbn(q)
    else:
        request = yushu_book.yushu_book_key(q)
    return jsonify(request)
    #return json.dumps(request),200,{'content-type':"application/json"}
#这里可以指定host地址，host = 'IP',port = '端口'
#如果没有这一句，那么flash直接导入到其他模块，那么就会被执行