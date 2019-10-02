import json as js
zero = ['财务总监','财务经理','财务顾问','财务主管/总账主管','金融产品经理','金融产品销售','投资/理财顾问',
        '投资银行业务','融资经理/融资主管','融资专员','拍卖/担保/典当业务','银行客户总监','个人业务部门经理/主管',
        '个人业务客户经理','公司业务部门经理/主管','公司业务客户经理','综合业务经理/主管','信贷管理','进出口/信用证结算',
        '高级客户经理/客户经理','信用卡销售','保险业务经理/主管','理财顾问/财务规划师','保险经纪人/保险代理','储备经理人']
one = ['首席财务官','CFO','财务分析经理/主管','成本经理/成本主管','资金经理/主管','审计经理/主管','税务经理/税务主管',
       '金融/经济研究员','证券分析师股票/期货操盘手','投资/基金项目经理','投资银行财务分析','风险管理/控制',
       '行长/副行长','保险精算师','保险产品开发/项目策划']
print(len(zero))
print(len(one))
with open('path\\total_test.json',encoding='utf-8')as f:
    with open('path\\total_test_have_position.json','w', encoding='utf-8')as f2:
        for i in f:
            i = js.loads(i)
            for j in zero:
                if j in i['job_cat']:
                    i['job_position'] = 0
            for j in one:
                if j in i['job_cat']:
                    i['job_position'] = 1
            i = js.dumps(i,ensure_ascii=False)
            f2.write(i+'\n')