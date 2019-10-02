def duty_sec_clear(i):
    description = ['主要职责：', '岗位职责', '工作内容', '职位描述', '职位简介', 'job description',
                   '工作职责', '职责描述', '工作说明：', '岗位描述', '职位信息', '职责', 'responsib', '岗位说明'
                                                                               'primary objective', '工作职能', '职 位 描 述',
                   'introductio', '职位职能', '深圳专业软件公司急招']
    requirement = ['任职资格', 'job #', 'job post title:', '任职要求', '招聘要求', '必备技能',
                   '基本技能', '职位要求', '岗位要求：', 'requirement', '岗位要求:', '岗位要求 :', '我们希望你有这些能力']
    skip_list = ['其他', '福利', '薪酬', '联系', '工作地点：', '为您提供', '强调：',
                 '公司提供', 'About', '薪资', '具体薪资', '联系人', '即可找到']
    for j in i['job_duty']:
        j = j.replace('二年', '替换两年')
        j = j.replace('一年', '替换医年')
        j = j.replace('四年', '替换四年')
        j = j.replace('五年', '替换五年')
        j = j.replace('三年', '替换三年')
        j = j.lstrip('()（）§ 。:一二三四五')
        j = j.replace('替换三年', '三年')
        j = j.replace('替换两年', '二年')
        j = j.replace('替换医年', '一年')
        j = j.replace('替换三年', '三年')
        j = j.replace('替换四年', '四年')
        for k in requirement:
            if k in j:
                if j not in i['job_duty']:
                    continue
                index_re = i['job_duty'].index(j)
                i['job_duty'] = i['job_duty'][:index_re]
                i['job_skill'] = i['job_duty'][index_re + 1:]
        if '职能类别' in j:
            if j not in i['job_duty']:
                continue
            del_index = i['job_duty'].index(j)
            i['job_duty'] = i['job_duty'][0:del_index]
        for k in description:
            if j not in i['job_duty']:
                continue
            if k in j:
                i['job_duty'].remove(j)
        del_index_1 = 0
        for bonus in skip_list:
            if bonus in i['job_duty']:
                for j in i['job_duty']:
                    if bonus in j:
                        del_index_1 = i['job_duty'].index(j)
        if del_index_1 < 2:
            i['job_duty'] = i['job_duty'][del_index_1:]
        else:
            i['job_duty'] = i['job_duty'][0:del_index_1]
    return i