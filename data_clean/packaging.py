#coding=utf-8
import pymongo
import json as js
from com_package import revise_com
from salary_package import salary_revire
from jd_rum_revise import jd_rum_revise
from sp_jd_rum_revise import sp_jd_rum_revise
from duty_fir_clear import duty_fir_clear
from duty_sec_clear import duty_sec_clear
from duty_thi_clear import duty_thi_clear
from skill_fir_clear import skill_fir_clear
from skill_sec_clear import skill_sec_clear
from skill_thi_clear import skill_thi_clear
from split_str import split_str
def pure_info(i):
    i = revise_com(i)
    i = salary_revire(i)
    if 'job_description' not in str(i):
        i['job_description'] = i['jd']
        del i['jd']
    if type(i['job_description']) == str:
        i = split_str(i)
        if type(i['job_description']) == str:
            z = sp_jd_rum_revise(i)
        else:
            z = jd_rum_revise(i)
    else:
        z = jd_rum_revise(i)
    a = duty_fir_clear(z)
    b = duty_sec_clear(a)
    c = duty_thi_clear(b)
    d = skill_fir_clear(c)
    e = skill_sec_clear(d)
    f = skill_thi_clear(e)
    if f is None:
        return e
    else:
        return f



