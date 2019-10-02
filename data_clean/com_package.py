import re
def revise_com(i):
    if 'com_scale' in str(i):
        com_ = re.sub('[，]', '/', i['com_scale'])
    else:
        com_ = re.sub('[，]', '/', i['comsca'])
    com_ = com_.split('|')
    if len(com_) == 1:
        com_.append('11')
        com_.append('11')
    elif len(com_) == 2:
        com_.append(com_[1])
        com_[1] = '22'
    i['com_type'] = com_[0]
    i['com_scale'] = com_[1]
    i['com_cat'] = com_[2]
    if i.__contains__('jobcat'):
        i['job_cat'] = i['jobcat']
        del i['jobcat']
    if i.__contains__('exp'):
        i['experience'] = i['exp']
        del i['exp']
    if i.__contains__('city'):
        i['company_exp'] = i['city']
        del i['city']
    if i.__contains__('job'):
        i['job_name'] = i['job']
        del i['job']
    if i.__contains__('com'):
        i['company_name'] = i['com']
        del i['com']
    if i.__contains__('num'):
        i['num_want'] = i['num']
        del i['num']
    if i.__contains__('contact'):
        i['JD_url'] = i['contact']
        del i['contact']
    if i.__contains__('time'):
        i['pub_time'] = i['time']
        del i['time']
    if i.__contains__('edu'):
        i['degree'] = i['edu']
        del i['edu']
    if i.__contains__('curtime'):
        i['crawl_time'] = i['curtime']
        del i['curtime']
    if i.__contains__('loc'):
        i['job_location'] = i['loc']
        del i['loc']
    if 'comsca' in str(i):
        del i['comsca']
        del i['comtype']
        del i['comind']
    return i