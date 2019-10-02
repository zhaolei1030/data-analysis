import json as js
import matplotlib.pyplot as plt
import numpy as np
import csv
total_security = ['股票','证券','证券/期货/外汇经纪人','证券分析师股票/期货操盘手','金融/经济研究员','金融产品经理','金融产品销售','投资/基金项目经理','投资/理财顾问','投资银行业务','投资银行财务分析','融资经理/融资主管','融资专员','风险管理/控制','拍卖/担保/典当业务']
total_insurance = ['保险精算师','保险产品开发/项目策划','保险业务经理/主管','保险经纪人/保险代理','理财顾问/财务规划师','储备经理人','保险电销','保险核保','保险理赔','保险客户服务/续期管理','保险培训师','保险内勤','契约管理']
total_accounting = ['财务经理','财务顾问','首席财务官','CFO','财务总监','财务经理，财务顾问','财务主管/总账主管','会计经历/会计足管','会计','出纳员','财务助理/文员','固定资产会计','财务分析经理/主管','财务分析员','成本经理/成本主管','成本管理员','资金经理/主管','资金专员','审计经理/主管','审计专员/助理','税务经理/税务主管','税务专员/助理','统计员']
total_bank = ['行长/副行长','银行客户总监','个人业务部门经理/主管','个人业务客户经理','公司业务部门经理/主管','公司业务客户经理','综合业务经理/主管','综合业务专员','资产评估/分析','风险控制','信贷管理','信审核查','进出口/信用证结算','外汇交易','清算人员','高级客户经理/客户经理','客户主管/专员','营业部大堂经理','信用卡销售','呼叫中心客服','银行柜员']
total = total_security + total_insurance + total_accounting + total_bank
salary_dict = {}
aveage_salary_dict = {}
for k in range(0,72):
    salary_dict[str(k)] = []
count_total = 0
count_sp = 0
with open('path\\finance_new.json', encoding='utf-8') as f2:
    for i in f2:
        i = js.loads(i)
        for k in range(0,72):
            if "cat_num" in i.keys():
                if i["cat_num"] == k:
                    salary_dict[str(k)].append(i['average'])
                    aveage_salary_dict[str(k)] = sum(salary_dict[str(k)])/len(salary_dict[str(k)])
target = []
sample_num = []
x_axis = []
for j in aveage_salary_dict.keys():
    if aveage_salary_dict[j]> 10:
        target.append(total[int(j)])
        sample_num.append(len(salary_dict[j]))
        x_axis.append(total[int(j)]+'({})'.format(len(salary_dict[j])))
        # print(total[int(j)+1])
        # print(str(aveage_salary_dict[j]))
        # print(len(salary_dict[str(j)]))
y = [aveage_salary_dict[str(total.index(j))] for j in target]
for i in total_security:
    if i in target:
        print(i)
        print(len(target))
print(x_axis)
out = open('.Stu_csv.csv','a', newline='')
csv_write = csv.writer(out,dialect='excel')
csv_write.writerow(x_axis)
csv_write.writerow(y)

# for j in total:
#     if j not in target:
#         print(j)
# print(len(target))
        # for j in total:
        #     if j in i["job_cat"]:
        #         i['table'] = 1
        # if i['table'] == 0:
        #     count_sp += 1
            # print(i["job_cat"])
            # print(i['salary'])
        # print(i["com_cat"])