# -*- coding: utf-8 -*-
import requests
import json
import sys
# 设置默认解码格式
reload(sys)
sys.setdefaultencoding("utf-8")
r = requests.get("http://www.kuaidi100.com/query?type=yuantong&postid=11111111111")
s1=r.text
print s1
print type(s1)
# (Unicode) json s1->dict
d1 = json.loads(s1)
#dict d1 -> (unicode) json
fps=json.dumps(d1,ensure_ascii=False) 
fp=open('jsonout1.csv','w')
fp.write(fps)