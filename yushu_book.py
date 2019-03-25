from httper import httper
import helper



class yushu_book:
    #将url里面的q传到下面方法，就会调用http请求，获取接口返回数据
    get_isbn = 'http://t.yushu.im/v2/book/isbn/{}'
    get_q = 'http://t.yushu.im/v2/web/search?q={}&start={}&count={}'
    @classmethod
    def yushu_book_isbn(cls,q):
        url = cls.get_isbn.format(q)
        isbn_requests = httper.getbook_isbn(url)
        return isbn_requests
    @classmethod
    def yushu_book_key(cls,q):
        url = cls.get_q.format(q,15,0)
        key_requests = httper.getbook_isbn(url)
        return key_requests