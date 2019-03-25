import requests

class httper:

    @staticmethod
    def getbook_isbn(url,retrun_json = True):
        #这里主要判断两个，返回的是不是200，返回的是不是json
        r = requests.get(url)
        if r.status_code != 200:
            return {""} if retrun_json else ""
        return r.json() if retrun_json else r.text