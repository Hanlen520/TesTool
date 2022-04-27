import requests
import json as complexjson
from common.logger import logger


class HttpClient(object):

    def __init__(self, root_url: str):
        self.root_url = root_url if root_url.endswith('/') else root_url + "/"
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        self.show_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

    @staticmethod
    def show_log(url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info("request url --> {}".format(url))
        logger.info("request method --> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("request header --> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("request params --> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("request data --> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("request body --> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("upload files --> {}".format(files))
        logger.info("request cookies --> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))


if __name__ == '__main__':
    rc = HttpClient("http://127.0.0.1:8000/")
    json_data = {
        "size": 8,
        "current": 1,
        "content": "",
        "condition": "",
        "table_name": "Student"
    }
    rsp = rc.post("student_manage/info/", json=json_data)
    print(rsp.json())
