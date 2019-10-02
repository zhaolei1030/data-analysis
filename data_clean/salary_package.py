import re
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
    return i