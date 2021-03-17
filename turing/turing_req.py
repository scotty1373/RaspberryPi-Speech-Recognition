#-*- coding: utf-8 -*-
import json
import urllib.request

# api_url = "http://openapi.tuling123.com/openapi/api/v2"
# json_path = 'turing.json'

class TuringDome():
    def __init__(self,json_path="",api_url=""):
        self.json_path = json_path
        self.api_url = api_url
        # self.text_input = input('请输入我的问话\n我：')
        self.text_input = input('User：')

    def readJson(self):
        '''获取json文件'''
        with open(self.json_path,'r',encoding='utf-8') as f_json:
            json_data = json.load(f_json)
        return json_data

    def textInput(self):
        '''用变量text_input替换text的value值'''
        req = self.readJson()
        req['perception']['inputText']['text'] = self.text_input
        return req

    def dumpsJson(self):
        '''将json字符串转化成dict格式'''
        req = self.textInput()
        req = json.dumps(req,sort_keys=True,indent=4,).encode('utf8') #必须encode成utf8，否则http post无法识别，报错TypeError
        return req  

    def urllibRequestResponse(self):
        req = self.dumpsJson()
        http_post = urllib.request.Request(self.api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)# 在urlopen()方法中传入字符串格式的url地址，则此方法会访问目标网址，然后返回访问的结果。
        response_str = response.read().decode('utf8')  #传回的数据为byte类型，decode成utf8格式
        response_dict = json.loads(response_str) # 将字符串response_str转成字典
        return response_dict

    def getTuringResponse(self):
        '''取得机器人返回的语句并输出'''
        response_dict = self.urllibRequestResponse()
        intent_code = response_dict.get('intent')['code']
        results_text = response_dict.get('results')[0]['values']['text']
        if results_text == None:
            print('code：' + str(intent_code))
            print('请查阅api文档检查报错信息')
        # print('Turing的回答：')
        print('Turing_Scotty：' + results_text)

    def talkToTheTuring(self):
        #self.text_input = input('请输入我的问话\n我：')
        while True:
            if self.text_input != "exit":
                self.getTuringResponse()
                # self.text_input = input('请输入我的问话\n我：')
                self.text_input = input('User：')
            else:
                print("*****结束对话！*****")
                break

# if __name__ == '__main__':
#     #pass
#     td = TuringDome(json_path=json_path,api_url=api_url)
#     td.talkToTheTuring()
