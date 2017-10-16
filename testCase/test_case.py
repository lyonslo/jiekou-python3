# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  : lileilei
# @File    : test_case.py
from  Interface.testFengzhuang import TestApi
from  Public.get_excel import datacel
from  Public.log import LOG,logger
listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel()
from Public.panduan import assert_in
@logger('测试')
def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust=[]
    for i in range(len(listurl)):
        api=TestApi(url=listurl[i],key=listkey[i],connent=listconeent[i],fangshi=listfangshi[i])
        apicode=api.getcode()
        apijson=api.getJson()
        LOG.info('inputdata> 参数:%s, url:%s ,返回:%s,预期:%s'%(listconeent[i],listurl[i],apijson,listqiwang[i]))
        assert_re=assert_in(asserqiwang=listqiwang[i],fanhuijson=apijson)
        if assert_re=='pass':
            list_json.append(apijson)
            listrelust.append('pass')
            list_pass += 1
        else:
            list_fail+=1
            listrelust.append('fail')
            list_json.append(apijson)
    return  listrelust,list_fail,list_pass,list_json