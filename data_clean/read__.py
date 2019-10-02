import json as js
with open('D:\Work(jd)\封装\jd_1_rum_revisied_sp.json'.format(33), encoding='utf-8') as f2:
    for i in f2:
        i = js.loads(i)
        print(i)