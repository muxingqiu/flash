import requests
# get_isbn = 'http://t.yushu.im/v2/book/isbn/{}'
# get_q = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'
class Http:
    def getbook_isbn(self,url,retrun_json = True):
        #这里主要判断两个，返回的是不是200，返回的是不是json
        r = requests.get(url)
        if r.status_code != 200:
            return {} if retrun_json else ""
        return r.json() if retrun_json else r.text