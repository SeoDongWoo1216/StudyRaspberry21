import urllib.request as urq
import urllib.parse as uparse
import datetime
import json

class naverSearch(object):

    # 생성자
    def __init__(self):
        print('Naver Search API 생성')

    # 네이버 API 요청함수
    def getRequestUrl(self, url):
        req = urq.Request(url)

        # 네이버 open API 요청하기위해 반드시 필요한 헤더 작성
        req.add_header('X-Naver-Client-Id', 'LsWz64BYdyM_qAEsYbF_')
        req.add_header('X-Naver-Client-Secret', 'JJCRyGOj9W')

        try:
            res = urq.urlopen(req)
            if res.getcode() == 200:  # ok
                print('[{0}] URL Request succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')

        except Exception as e:
            print(e)
            return None

    # 네이버 검색 API 사용함수
    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode)
        param = '?start={0}&display={1}&query={2}'.format(
            page_start, display, uparse.quote(search_word))
        url = base + node + param 
        # https://openapi.naver.com...nodeval.json?start=1&display=10&query=코로나

        retData = self.getRequestUrl(url)
        if retData == None:
            return None
        else:
            return json.loads(retData)


    # 데이터 처리
    def getPostData(self, post, jsonResult):
        pass

