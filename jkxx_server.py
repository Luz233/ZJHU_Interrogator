#coding:utf-8
import requests
import base64
import ccj
import os
from flask import Flask, render_template, request, current_app
from flask_cors import *
import hashlib
server = Flask(__name__)
CORS(server,supports_credentials=True)
import json
def check(xh,jhm):
    xhli=open('xh.txt','r+')
    xhlist=xhli.read()
    print(xhlist)
    if(xh in xhlist):
        xhli.close()
        return True
    else:
        if(jhm is not None):
            jhmli=open('3.txt','r+')
            jhmlist=jhmli.read()
            jhmli.close()
            print(jhmlist)
            if(len(jhm)>30 and jhm in jhmlist):
                jhmlist=jhmlist.replace(jhm,'')
                jhmli=open('3.txt','w')
                jhmli.write(jhmlist)
                xhli.write(xh)
                jhmli.close()
                xhli.close()
                return True
            return False
        return False
@server.route('/cjcx',methods=['get','post'])
def cjcx():
    xm=""
    if request.method == 'GET':
        xh=request.values.get("xh")
        jhm=request.values.get("jhm")
        print(xh,jhm)
        if(check(xh,jhm)):
            return ccj.chaxun(xh)
        else:
            return "学号未激活或激活码错误"

@server.route('/ea4e5208bedeb088d69ca90b445b8570',methods=['get','post'])
def ea4e5208bedeb088d69ca90b445b8570():
    xm=""
    if request.method == 'GET':
        xh=request.values.get("xh")
        return ccj.chaxun(xh)




indexx="""
 <html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<head>
    <title>成绩提前查询（免密）</title>
    <meta name="copyright"   content="仅供测试使用，请勿用作违法用途">

  <style type="text/css">
*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
} 

a{
    text-decoration: none;
    color: black;
}

body{
    background: url("https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=4286836258,2371376262&fm=26&gp=0.jpg") no-repeat;
    background-size: cover;
    /*text-align: center;*/
}

.div1{
    width:500px;
    height:200px;
    opacity:0.5;
    /*background:#F00;*/
    padding: 30px;
    float:left;
}
.div1 h2{color:white;}
.div1 a{color:white;}
.dbglog-header{
    width:100%;
    height:500px;
    border-radius: 5px 5px 0 0;
    line-height: 30px;
    color:gray;
    text-align: center;
    margin-top: 200px;
    cursor:default;
}
.div2{
    width:500px;
    height:200px;
    opacity:0.9;
    /*background:#F00;*/
    padding: 100px;
    float:left;
}
#panel{
    width:400px;
    height: 630px;
    background-color: white;
    text-align: left;
    border-radius: 5px;
    box-shadow: -10px 20px 100px black;
    position: absolute;
    top:50%;
    left:50%;
    margin-left: -200px;
    margin-top: -300px;
}

.panel-header{
    width:100%;
    height:64px;
    background-color: RoyalBlue;
    border-radius: 5px 5px 0 0;
    line-height: 64px;
    color:white;
    text-align: center;
    margin-bottom: 10px;
    cursor:default;
}

.panel-content{
    padding: 20px;
}

.panel-content .user-pwd{
   margin-bottom: 15px;
   height: 40px;
   position: relative;
}

.panel-content .user-pwd img{
   position: absolute;
   top: 7px;
   left: 6px;
}

.panel-content .user-pwd input{
   width: 100%;
   height: 100%;
   box-sizing: border-box;
   padding-left: 38px;
   border-radius: 5px;
   border:1px solid #dddddd;

}

.panel-content .user-pwd input:focus{
    outline: none;
    border: 1px solid orange;
    panel-header: 0 0 10px orange;
}

.setting a{
    color: darkgray;
    font-size: 13px;
}

.setting a.pull-right{
    float: right;
}

.login-btn{
  margin: 15px 0;
  width: 100%;
  height: 35px;
  background-color: CornflowerBlue;
  border: 0;
  font-size: 20px;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.login-btn:focus{
    outline: none;
}
.del-btn{
  margin: 15px 15px;
  width: 40%;
  height: 35px;
  background-color: CornflowerBlue;
  border: 0;
  font-size: 20px;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.del-btn:focus{
    outline: none;
}
.reg{
    text-align: center;
    margin-bottom: 15px;
    color: darkgray;
    font-size: 13px;
}

.reg a{
    color: orangered;
}


.panel-footer{
    padding:0 20px;
    height: 44px;
    line-height: 44px;
}

.panel-footer img{
    width: 30px;
    vertical-align: middle;
}
  </style>
  
<html>
<script src="/clipboard.js"></script>
<script src="/jquery-2.1.3.min.js"></script>
  </head>

    <!--
    <marquee behavior="scroll" direction="left" loop=-1 >
        <font color="#FFFFFF">
        test
    </marquee>
    -->
<!--
  <div class="div1">
      <h2>UPDATE LOG</h2>
      <a>2021.07.09:   功能内测<br></a>
      <br><br><br><br><br>
  </div> 
-->
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div> 
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="8480418184"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>  
<div>
    <div id="panel">
        <div class="panel-header">
	<h1>成绩查询测试（免密）</h1>
        </div>
        <div class="panel-content">
           <div class="user-pwd">
               
               <input placeholder="请输入学号" name="user" id="xh">
           </div>
           <div class="user-pwd">
               
               <input placeholder="请输入激活码/已激活请忽略" name="user" id="jhm">
           </div>
            <button class="login-btn" id="add">查&nbsp;询&nbsp;&nbsp;/&nbsp;&nbsp;激&nbsp;活</button>
        </div padding-left=50%>
		<!--<div><input id="resu" type="text" style="border:none;"></div>-->
                       
	
        <div class="panel-footer" align="center">
<a href="https://www.swiu.cn/detail/E37789D0139906F0" class="button">购买激活码</a>
<a href="https://www.hyluz.cn/?id=45880" class="button">免费查询方法（需密码）</a>
	<h4>一学号对应一激活码，使用后失效，该学号以后查询无需再使用激活码</h4>
<h4>服务器资源有限，查询缓慢，点击一次查询后不要重复点击，等待几分钟</h4>
        </div>
		

    </div>
</div>

  <script>
(function login(){
    //alert(1);
    b = document.getElementById('add');
    b.onclick = function() {
	    //alert(1);
	    var f = document.getElementById('xh');
                    var j= document.getElementById('jhm');
	    location.href="http://zjhu.h123456aa.ml/cjcx?xh="+xh.value+"&jhm="+jhm.value
    };

})();
</script>
<div style="display:none">
  				<script type="text/javascript" src="https://v1.cnzz.com/z_stat.php?id=1277949079&amp;web_id=1277949079">
  					</script><script src="https://c.cnzz.com/core.php?web_id=1277949079&amp;t=z" charset="utf-8" type="text/javascript"></script><a href="https://www.cnzz.com/stat/website.php?web_id=1277949079" target="_blank" title="站长统计">站长统计</a>

  					
		</div>
</html>

"""
@server.route('/',methods=['get','post'])
def index():
    return indexx

if __name__ == '__main__':
    server.run(port=80, host='0.0.0.0')  #
    
