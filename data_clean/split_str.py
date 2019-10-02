import re
def split_str(i):
    i['job_description'] = i['job_description'].replace('211、985', '替换学历')
    i['job_description'] = re.sub('\d+、', '7788', i['job_description'])
    i['job_description'] = re.sub('\d+\.', '7788', i['job_description'])
    i['job_description'] = re.sub('（+\d+）', '7788', i['job_description'])
    i['job_description'] = re.sub('\(+\d+\)', '7788', i['job_description'])
    i['job_description'] = re.sub('-', '7788', i['job_description'])
    i['job_description'] = i['job_description'].split('7788')
    for j in i['job_description']:
        if '替换学历' in j:
            j.replace('替换学历', '211、985')
    return i
