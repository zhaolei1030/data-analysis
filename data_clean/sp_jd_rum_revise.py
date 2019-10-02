import re
def clear_info(j):
    j = j.lower()
    if len(j) ==1 and j.isnumeric():
        return j
    else:
        j = j.replace('20-40', '替换年龄')
        j = j.replace('.net', '替换网络')
        j = j.replace('4000-7000', '替换收入')
        j = j.replace('2-3', '替换编程经验')
        j = j.replace('30-40', '替换岁数')
        j = j.replace('4-10', '替换单休')
        j = j.replace('6-15', '替换工资')
        j = j.replace('1-2', '替换工作经验')
        j = j.replace('二年', '替换两年')
        j = j.replace('一年', '替换医年')
        for o in range(10):
            j = j.replace('{}年'.format(o), '替换工作{}year'.format(english_num[o]))
        j = j.lstrip(',、．；?、 123456×7890*()&lt;1&gt;（），【一■二◆！～：》·"●①②③④⑤⑥⑦⑧⑨')
        j = j.rstrip(',、．；?1234×567890、。 &lt;1&gt;(（，一.】;■二◆！"')
        j = j.strip('.？- ~')
        j = j.replace('替换年龄', '20-40')
        j = j.replace('替换网络', '.net', )
        j = j.replace('替换收入', '4000-7000', )
        j = j.replace('替换编程经验', '2-3', )
        j = j.replace('替换单休', '4-10', )
        j = j.replace('替换工资', '6-15', )
        j = j.replace('替换岁数', '30-40')
        j = j.replace('替换工作经验', '1-2')
        j = j.replace('替换两年', '二年')
        j = j.replace('替换医年', '一年')
        for o in range(10):
            j = j.replace('替换工作{}year'.format(english_num[o]), '{}年'.format(o))
        return j
description = ['主要职责：', '岗位职责', '工作内容', '职位描述', '职位简介', 'job description',
                   '工作职责', 'responsibility', '请了解我们', '我们需要你', '工作经历或技术背景要求',
                   '岗位说明', '职位职责', '岗位责任', '职责', '具体要求', '工作描述',
                   '职责描述']
requirement = ['任职资格', '任职要求', '招聘要求', '必备技能', '岗位要求', '工作责任', '任职要求'
                 '职位要求', '任职资格', 'requirement', '我们希望你有这些能力',
                 '岗位及要求' , '专业知识和技能要求', '技术能力']
skip_list = ['其他', '福利', '薪酬', '联系', '您将得到', '为您提供', '强调：'
        , '公司提供', 'About', '薪资', '具体薪资', '联系人', '工作地点', '即可找到']
judge_list = ['熟悉', '熟练', '掌握', '辅助', '相关专业', '学历', '专业']
english_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def sp_jd_rum_revise(i):
    index_des, index_req, index_znlb, index_kword, index_skip = 7777, 7777, 7777, 7777, 7777
    skill_judgement = 7777
    print(i['job_description'])
    for k in description:
        if k in i['job_description']:
            index_des = i['job_description'].index(k)
            index_des_1 = index_des + len(k) + 1
    for k in requirement:
        if k in i['job_description']:
            index_req = i['job_description'].index(k)
            index_req_1 = index_req + len(k) + 1
    if '职能类别' in i['job_description']:
        index_znlb = i['job_description'].index('职能类别')
        index_znlb_1 = index_znlb + 5
    if '关键字' in i['job_description']:
        index_kword = i['job_description'].index('关键字')
        index_kword_1 = index_kword + 4
    for k in skip_list:
        if k in i['job_description']:
            if '日本' not in i['job_description']:
                if index_skip == 7777:
                    index_skip = i['job_description'].index(k) + len(k)
                    if (index_skip < index_req) or (index_skip < index_des):
                        index_skip = 7777
    for k in judge_list:
        if k in i['job_description']:
            if skill_judgement == 7777:
                skill_judgement = 9999
    new_description = i['job_description']
    if index_kword != 7777:
        i['key_word'] = new_description[index_kword_1:]
        i['job_cat'] = new_description[index_znlb_1:int(index_kword)]
    else:
        i['job_cat'] = new_description[index_znlb_1:]
        i['key_word'] = ''
    if index_skip != 7777:
        index_znlb = index_skip
    if index_des != 7777:
        if index_req != 7777:  # 能找到des和request的的索引
            if int(index_des) < int(index_req):
                i['job_duty'] = new_description[index_des_1:int(index_req)]
                i['job_skill'] = new_description[index_req_1:int(index_znlb)]
            else:
                i['job_duty'] = new_description[index_des_1:int(index_znlb)]
                i['job_skill'] = new_description[index_req_1:int(index_des)]
        else:
            i['job_duty'] = new_description[index_des_1:int(index_znlb)]
            i['job_skill'] = ''
    elif index_des == 7777:
        if index_req != 7777:  # 能找到request的的索引
            i['job_skill'] = new_description[index_req_1:int(index_znlb)]
            i['job_duty'] = new_description[0:int(index_req)]
        elif skill_judgement == 7777:
            i['job_duty'] = new_description[0:int(index_znlb)]
            i['job_skill'] = ''
        else:
            i['job_duty'] = ''
            i['job_skill'] = new_description[0:int(index_znlb)]
    else:
        if index_des != 7777:
            if index_req != 7777:  # 能找到des和request的的索引
                if int(index_des) < int(index_req):
                    i['job_duty'] = new_description[index_des_1:int(index_req)]
                    i['job_skill'] = new_description[index_req_1:int(index_skip)]
                else:
                    i['job_duty'] = new_description[index_des_1:int(index_skip)]
                    i['job_skill'] = new_description[index_req_1:int(index_des)]
            else:
                i['job_duty'] = new_description[index_des_1:int(index_skip)]
                i['job_skill'] = ''
        else:
            if index_req != 7777:  # 能找到request的的索引
                i['job_skill'] = new_description[index_req_1:int(index_skip)]
                i['job_duty'] = new_description[0:int(index_req)]
            elif skill_judgement == 7777:
                i['job_duty'] = new_description[0:int(index_skip)]
                i['job_skill'] = ''
            else:
                i['job_duty'] = ''
                i['job_skill'] = new_description[0:int(index_skip)]
    i['job_duty'] = re.split("[；。\-]", i['job_duty'])
    new_duty = []
    for j in i['job_duty']:
        j = clear_info(j)
        if j == '':
            continue
        else:
            new_duty.append(j)
    new_skill = []
    i['job_duty'] = new_duty
    i['job_skill'] = re.split("[。；\-;]", i['job_skill'])
    for j in i['job_skill']:
        j = clear_info(j)
        if j == '':
            continue
        else:
            new_skill.append(j)
    i['job_skill'] = new_skill
    del i['job_description']
    return i