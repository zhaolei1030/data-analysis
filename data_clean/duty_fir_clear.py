def duty_fir_clear(i):
    description = ['主要职责：', '岗位职责', '工作内容', '职位描述', '职位简介', 'job description',
                   '工作职责', 'responsibility', '请了解我们', '我们需要你', '工作经历或技术背景要求',
                   '岗位说明', '职位职责', '岗位责任', '职责', '具体要求', '工作描述', '岗位要求', '职责描述']
    requirement = ['任职资格', '任职要求', '招聘要求', '必备技能', '岗位要求', '工作责任', '任职要求'
                                                                   '职位要求', '岗位要求', '任职资格', 'requirement', '我们希望你有这些能力',
                   '岗位及要求'
        , '岗位及要求', '专业知识和技能要求']
    skip_list = ['其他', '福利', '薪酬', '联系', '您将得到', '为您提供', '强调：'
        , '公司提供', 'About', '薪资', '具体薪资', '联系人', '工作地点', '即可找到']
    judge_list = ['熟悉', '熟练', '掌握', '辅助', '相关专业', '学历', '专业']
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
        for k in judge_list:
            if k in j:
                i['job_skill'] = i['job_duty']
                i['job_duty'] = []
    return i