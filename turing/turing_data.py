#-*- coding: utf-8 -*-
import turing_req as Tu

api_url = 'http://openapi.tuling123.com/openapi/api/v2'
json_path = 'turing.json'



if __name__ == "__main__":
    ack = Tu.TuringDome(json_path, api_url)
    ack.talkToTheTuring()
