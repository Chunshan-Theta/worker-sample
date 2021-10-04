import subprocess
import requests
import json
import copy
while True:
    try:
        reponds = requests.get('http://127.0.0.1:8088/api/query?msgid=test&q=' + "測試",
                               headers={'token': 'ner_api'})
        print("connect success")
        break
    except:
        pass
CONNECTION_NUMBER = 1
TOTAL_CONNECTION_NUMBER = 10
# test mul connection
out_bytes = subprocess.check_output('ab -n 100 -c 50 -H "token":"ner_api" -T "application/json" -p ./test_sample/ner_request.json http://127.0.0.1:8088/api/ner', shell=True).decode('utf-8')
print(out_bytes.split('Requests per second:')[1].split('[#/sec]')[0].strip())
# test lots request in sentence
# 5 10 15 50
# total 100
# out_bytes = subprocess.check_output('ab -n 10 -c 1 -H "token":"ner_api" -T "application/json" -p ./test_sample/ner_request_5.json http://127.0.0.1:8088/api/ner', shell=True).decode('utf-8')
# print(out_bytes.split('Requests per second:')[1].split('[#/sec]')[0].strip())


# def make_test():
#     sent = {
# 			"id" : "1",
# 			"text" : "二十位陳家豪 銀行家"
# 		}
#
#     docs = list()
#     for i in range(1000):
#         sent["id"] = str(i)
#         temp = copy.deepcopy(sent)
#         docs.append(temp)
#     with open("./test_sample/ner_request_much.json" , "w", encoding="utf-8") as file:
#         file.write(json.dumps({"docs" : docs}))
# make_test()