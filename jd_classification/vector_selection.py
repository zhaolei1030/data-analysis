import json as js
with open('path\\total_test_have_position.json',encoding='utf-8')as f:
    with open('vecor_train_text.txt','w',encoding='utf-8')as f2:
        for i in f:
            i = js.loads(i)
            if 'job_position' in i.keys():
                if 'job_duty' in i.keys():
                    a = ','.join(i['job_duty'])
                else:
                    a = ''
                if 'job_skill' in i.keys():
                    b = ','.join(i['job_skill'])
                else:
                    b = ''
                if a+b != '':
                    print(a+b)
                    f2.write(a+b+'\n')