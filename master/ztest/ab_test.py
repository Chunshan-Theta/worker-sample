import subprocess
import requests

while True:
    try:
        reponds = requests.get('http://127.0.0.1:8088/api/query?msgid=test&q=' + "測試",
                               headers={'token': 'gitlabci'})
        print("connect success")
        break
    except:
        pass
out_bytes = subprocess.check_output('ab -n 3000 -c 100 -H "token":"gitlabci" "127.0.0.1:8088/api/query?q=刚存了30块钱玩不了"', shell=True).decode('utf-8')
print(out_bytes.split('Requests per second:')[1].split('[#/sec]')[0].strip())