import json as js
from packaging import pure_info
def average_salary(i):
    if '千'in i['salary']:
        if '-' in i['salary']:
            first_index = i['salary'].index('-')
            second_index = i['salary'].index('千')
            i['average'] = (float(i['salary'][0:first_index]) + float(i['salary'][first_index + 1:second_index])) / 2
        else:
            first_index = 0
            second_index = i['salary'].index('千')
            i['average'] = float(i['salary'][first_index :second_index])
    else:
        i['average'] = 6
    return i
def salary_revire(i):
    if '万' in i['salary']:
        if ('-') not in i['salary']:
            i2 = i['salary'].index('万')
            n2 = i['salary'][0:int(i2)]
            i['salary'] = '{}{}{}'.format(float(n2) * 10, '千', i['salary'][int(i2) + 1:])
        else:
            i1 = i['salary'].index('-')
            i2 = i['salary'].index('万')
            n1 = i['salary'][0:int(i1)]
            n2 = i['salary'][int(i1) + 1:int(i2)]
            i['salary'] = '{}{}{}{}{}'.format(float(n1) * 10, '-', float(n2) * 10, '千', i['salary'][int(i2) + 1:])
    if '年' in i['salary']:
        if ('-') not in i['salary']:
            i2 = i['salary'].index('千')
            n2 = float(i['salary'][0:int(i2)]) / 12
            i['salary'] = '{}{}'.format(round(n2, 2), '千/月')
        else:
            i1 = i['salary'].index('-')
            i2 = i['salary'].index('千')
            n1 = float(i['salary'][0:int(i1)]) / 12
            n2 = float(i['salary'][int(i1) + 1:int(i2)]) / 12
            i['salary'] = '{}{}{}{}'.format(round(n1, 2), '-', round(n2, 2), '千/月')
    i = average_salary(i)
    return i
total_security = ['股票','证券','证券/期货/外汇经纪人','证券分析师股票/期货操盘手','金融/经济研究员','金融产品经理','金融产品销售','投资/基金项目经理','投资/理财顾问','投资银行业务','投资银行财务分析','融资经理/融资主管','融资专员','风险管理/控制','拍卖/担保/典当业务']
total_insurance = ['保险精算师','保险产品开发/项目策划','保险业务经理/主管','保险经纪人/保险代理','理财顾问/财务规划师','储备经理人','保险电销','保险核保','保险理赔','保险客户服务/续期管理','保险培训师','保险内勤','契约管理']
total_accounting = ['财务经理','财务顾问','首席财务官','CFO','财务总监','财务经理，财务顾问','财务主管/总账主管','会计经历/会计足管','会计','出纳员','财务助理/文员','固定资产会计','财务分析经理/主管','财务分析员','成本经理/成本主管','成本管理员','资金经理/主管','资金专员','审计经理/主管','审计专员/助理','税务经理/税务主管','税务专员/助理','统计员']
total_bank = ['行长/副行长','银行客户总监','个人业务部门经理/主管','个人业务客户经理','公司业务部门经理/主管','公司业务客户经理','综合业务经理/主管','综合业务专员','资产评估/分析','风险控制','信贷管理','信审核查','进出口/信用证结算','外汇交易','清算人员','高级客户经理/客户经理','客户主管/专员','营业部大堂经理','信用卡销售','呼叫中心客服','银行柜员']
total = total_security + total_insurance + total_accounting + total_bank
total_dict = {}
for ind, v in enumerate(total):
    # print(ind + 1, v)
    total_dict[v] = ind
with open('path\\finance.json',encoding='utf-8') as f:
    with open('path\\security.json','w', encoding='utf-8') as f2:
        for i in f:
            i = js.loads(i)
            i = salary_revire(i)
            i['class'] = 1                  #第一类
            for k in total:
                if k in i["job_cat"]:
                    i["cat_num"] = total_dict[k]
            if "证券" in i["com_cat"]:
                i = js.dumps(i,ensure_ascii= False)
                f2.write(i+'\n')
with open('path\\finance.json',encoding='utf-8') as f:
    with open('path\\insurance.json','w', encoding='utf-8') as f2:
        for i in f:
            i = js.loads(i)
            i = salary_revire(i)
            i['class'] = 2
            for k in total:
                if k in i["job_cat"]:
                    i["cat_num"] = total_dict[k]
            if "保险" in i["com_cat"]:
                i = js.dumps(i,ensure_ascii= False)
                f2.write(i+'\n')
with open('path\\finance.json',encoding='utf-8') as f:
    with open('path\\accouting.json','w', encoding='utf-8') as f2:
        for i in f:
            i = js.loads(i)
            i = salary_revire(i)
            i['class'] = 3
            for k in total:
                if k in i["job_cat"]:
                    i["cat_num"] = total_dict[k]
            if "会计" in i["com_cat"]:
                i = js.dumps(i,ensure_ascii= False)
                f2.write(i+'\n')
with open('path\\finance.json',encoding='utf-8') as f:
    with open('path\\credit.json','w', encoding='utf-8') as f2:
        for i in f:
            i = js.loads(i)
            i = salary_revire(i)
            i['class'] = 4
            for k in total:
                if k in i["job_cat"]:
                    i["cat_num"] = total_dict[k]
            if "信托" in i["com_cat"]:
                i = js.dumps(i,ensure_ascii= False)
                f2.write(i+'\n')
with open('path\\finance.json',encoding='utf-8') as f:
    with open('path\\none.json','w', encoding='utf-8') as f2:
        for i in f:
            i = js.loads(i)
            i = salary_revire(i)
            for k in total:
                if k in i["job_cat"]:
                    i["cat_num"] = total_dict[k]
            if  i["com_cat"] == "":
                i = js.dumps(i,ensure_ascii= False)
                f2.write(i+'\n')
with open('path\\finance.json',encoding='utf-8') as f:
    with open('path\\bank.json','w', encoding='utf-8') as f2:
        for i in f:
            i = js.loads(i)
            i = salary_revire(i)
            i['class'] = 5
            for k in total:
                if k in i["job_cat"]:
                    i["cat_num"] = total_dict[k]
            if "银行" in i["com_cat"]:
                i = js.dumps(i,ensure_ascii= False)
                f2.write(i+'\n')
with open('path\\finance.json',encoding='utf-8') as f:
    with open('path\\finance_new.json','w', encoding='utf-8') as f2:
        for i in f:
            i = js.loads(i)
            i = salary_revire(i)
            i = pure_info(i)
            for k in total:
                if k in i["job_cat"]:
                    i["cat_num"] = total_dict[k]
            i = js.dumps(i,ensure_ascii= False)
            f2.write(i+'\n')