def skill_fir_clear(i):
    skip_list = ['其他', '福利', '薪酬', '联系', '工作地点：', '为您提供', '强调：',
         '公司提供', 'About', '薪资', '具体薪资', '联系人', '即可找到', '职能类别', '你会得到',
                 '招聘人数', '上班时间', '待遇', '工资', '工作地', '企业文化']
    head = ['我们需要您', '提示', 'require', '简历', '能力素质', '公司大概福利']
    for j in i['job_skill']:
        for k in skip_list:
            if k in j:
                if j not in i['job_skill']:
                    continue
                skip_index = i['job_skill'].index(j)
                if skip_index > 2:
                    i['job_skill'] = i['job_skill'][0:skip_index]
        j = j.lstrip('()（）－§ 。:一二三四五')
        for k in head:
            if k in j:
                if j not in i['job_skill']:
                    continue
                head_index = i['job_skill'].index(j)
                if head_index < 2:
                    i['job_skill'] = i['job_skill'][head_index:]
    return i