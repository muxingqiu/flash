from flask import blueprints, Blueprint,jsonify,request

from app.cms.book import SearchForm
from helper import is_key_or_isbn
from yushu_book import yushu_book
from . import web
from app.cms import book


@web.route('/book/search/')
def hello():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()    #接收form中的q
        isbn_or_key = is_key_or_isbn(q)
        if isbn_or_key == "isbn":
            requestf = yushu_book.yushu_book_isbn(q)
        else:
            requestf = yushu_book.yushu_book_key(q)
        return jsonify(requestf)
    else:
        return jsonify(form.errors)
    #return json.dumps(request),200,{'content-type':"application/json"}
#这里可以指定host地址，host = 'IP',port = '端口'
#如果没有这一句，那么flash直接导入到其他模块，那么就会被执行