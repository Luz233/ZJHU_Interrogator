#coding:utf-8

import requests
from selenium import webdriver
import base64
import re
from selenium import webdriver
driver=webdriver.PhantomJS(executable_path='/jkxx/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
url="http://jwxt.zjhu.edu.cn?XXXXXXX"#jwc01任意登录接口

def GetMiddleStr(content,startStr,endStr):
  startIndex = content.index(startStr)
  #print(startIndex)
  if startIndex>=0:
    startIndex += len(startStr)
  endIndex = content.index(endStr,startIndex)
  return content[startIndex:endIndex]
def len_zh(data):
    temp = re.findall('[^a-zA-Z0-9.]+', data)
    count = 0
    for i in temp:
        count += len(i)
    return(count)
def strB2Q(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code > 32 and inside_code <= 126:        
            inside_code += 65248

        rstring += chr(inside_code)
    return rstring

view="t<-1280608021;t<p<l<dybyscj;zxcjcxxs;>;l<\e;0;>>;l<i<1>;>;l<t<;l<i<1>;i<5>;i<15>;i<22>;i<23>;i<25>;i<29>;i<38>;i<40>;>;l<t<t<p<p<l<DataTextField;DataValueField;>;l<xymc;xydm;>>;>;t<i<27>;@<--\>请选择学院\<--;经济管理学院;教师教育学院;体育学院;人文学院;外国语学院;艺术学院;理学院;信息工程学院;生命科学学院;医学院;社会发展学院;图书馆;湖州学院;马克思主义学院;工学院;安定书院;音乐学院;经济管理学院(湖院);人文学院(湖院);理工学院(湖院);马克思主义学院(湖院);公共教学部(湖院);图书馆(湖院);行政(湖院);学生处;教务处;>;@<--\>请选择学院\<--;01;02;03;04;05;06;07;08;09;10;11;12;13;14;16;17;18;61;62;63;64;65;88;89;98;99;>>;>;;>;t<t<p<p<l<DataTextField;DataValueField;>;l<xmxh;xh;>>;>;t<i<1>;@<2018042101||王杰;>;@<"
view2=";>>;>;;>;t<t<;p<l<i<0>;i<1>;i<2>;i<3>;i<4>;i<5>;i<6>;i<7>;i<8>;i<9>;i<10>;i<11>;i<12>;i<13>;i<14>;i<15>;i<16>;i<17>;i<18>;i<19>;i<20>;i<21>;>;l<p<2000-2001;2000-2001>;p<2001-2002;2001-2002>;p<2002-2003;2002-2003>;p<2003-2004;2003-2004>;p<2004-2005;2004-2005>;p<2005-2006;2005-2006>;p<2006-2007;2006-2007>;p<2007-2008;2007-2008>;p<2008-2009;2008-2009>;p<2009-2010;2009-2010>;p<2010-2011;2010-2011>;p<2011-2012;2011-2012>;p<2012-2013;2012-2013>;p<2013-2014;2013-2014>;p<2014-2015;2014-2015>;p<2015-2016;2015-2016>;p<2016-2017;2016-2017>;p<2017-2018;2017-2018>;p<2018-2019;2018-2019>;p<2019-2020;2019-2020>;p<2020-2021;2020-2021>;p<2021-2022;2021-2022>;>>;>;;>;t<;l<i<13>;>;l<t<@0<;;;;;;;;;;>;;>;>>;t<p<p<l<Visible;>;l<o<f>;>>;>;l<i<1>;>;l<t<@0<;;;;;;;;;;>;;>;>>;t<@0<;;;;;;;;;;>;;>;t<@0<;;;;;;;;;;>;;>;t<p<;p<l<onclick;>;l<preview()\;;>>>;;>;t<p<;p<l<onclick;>;l<window.close()\;;>>>;;>;>>;>>;>"
def chaxun(xuehao):
	flag0=0
	cookie_list=[]
	while(flag0==0):
		try:
			driver.get(url)
# 获取cookie列表
			cookie_list=driver.get_cookies()
			print(cookie_list)
			if(cookie_list[0]['value']):
				flag0=1
		except:
			print("try")

	header={
	'Host':'jwxt.zjhu.edu.cn',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Referer':'http://jwxt.zjhu.edu.cn/cjcx.aspx?xh=jwc01&xm=&gnmkdm=N120305',
	'Content-Type':'application/x-www-form-urlencoded',
	'Content-Length':'4060',
	'Connection':'close',
	'Cookie':'ASP.NET_SessionId='+cookie_list[0]['value'],
	'Upgrade-Insecure-Requests':'1'
	}

	datas={
	'__VIEWSTATE':base64.b64encode((view+xuehao+view2).encode()),
	'Dropdownlist5':'--%3E%C7%EB%D1%A1%D4%F1%D1%A7%D4%BA%3C--',
	'Dropdownlist3':'a.xh',
	'Dropdownlist4':'2018082101',
	'Button1':'%B0%B4%D1%A7%C4%EA%D1%A7%C6%DA%B2%E9%D1%AF',
	'DropDownList1':'2020-2021',
	'DropDownList2':'2'}
	flag1=0
	a=[]
	while(flag1==0):
		try:
			a=requests.post(url="http://jwxt.zjhu.edu.cn/cjcx.aspx?xh=jwc01&xm=&gnmkdm=N120305",data=datas,headers=header)
			flag1=1
		except:
			print("try2")
	#print(a)
	#print(a.text)
	output=''
	output=output+'<table border="1">'
	output=output+'<tr>'+'<td>'+GetMiddleStr(a.text,'Label3">','</span>')+'</td>'+'</tr>'
	output=output+'<tr>'+'<td>'+GetMiddleStr(a.text,'<span id="Label5">','</span>')+'</td>'+'</tr>'
	output=output+'<tr>'+'<td>'+GetMiddleStr(a.text,'<span id="Label6">','</span>')+'</td>'+'</tr>'
	output=output+'<tr>'+'<td>'+GetMiddleStr(a.text,'<span id="Label7">','</span>')+'</td>'+'</tr>'
	output=output+'<tr>'+'<td>'+GetMiddleStr(a.text,'<span id="Label8">','</span>')+'</td>'+'</tr>'
	b=a.text.split('<td>')[2:]
	c=1
	prin=''
	#print(b[1])
	a=0
	for i in range(len(b)):
		#print(b[i])
		b[i].replace('</tr><tr>','')
		b[i].replace('</td>','')
		b[i].replace('</tr><tr class="alt">','')
		b[i].replace(' ','')
		if('未通过' in b[i]):
			a=i
			break
		#print(i)
	#print(a)
	i=0
	
	while(i<a+1):
		output=output+'<tr>'+'<td>'+str(b[i+3])+'</td>'+'<td>'+str(b[i+4])+'</td>'+'<td>'+str(b[i+6])+'</td>'+'<td>'+str(b[i+7])+'</td>'+'<td>'+str(b[i+8])+'</td>'+'<td>'+str(b[i+10])+'</td>'+'<td>'+str(b[i+11])+'</td>'+'</tr>'
		i=i+15
		#print(a.text)
	output=output+'</table>'
	#output=output.replace(' ','&nbsp;')
	return output.replace('\n','<br>')
#    except:
 #       return "error"
