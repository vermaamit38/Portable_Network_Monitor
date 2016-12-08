
import bottle
import time
from bottle import route, run, template,debug
import MySQLdb
import os

db = MySQLdb.connect("localhost","root","","project" )
cursor = db.cursor()

time1=0


@route('/NW')
def index():
    return bottle.template("try.tpl")



@route('/start.tpl')
def index():
    return bottle.template("start.tpl")
@route('/old.tpl')
def index():
    return bottle.template("old.tpl")
@route('/start_java.tpl')
def index():
    return bottle.template("start_java.tpl")

@route("/button_java.tpl")
def b2():
	st="/home/amit/project/with_java/protocol_count_display.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("java_tpl/button_java.tpl",data=array)
        return t1
@route("/button1_java.tpl")
def b2():
	st="/home/amit/project/with_java/bandwidth.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("java_tpl/button1_java.tpl",data=array)
        return t1
@route("/button2_java.tpl")
def b2():
	st="/home/amit/project/with_java/conn_comp.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("java_tpl/button2_java.tpl",data=array)
        return t1
@route("/button3_java.tpl")
def b2():
	st="/home/amit/project/withmysql/amit.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("java_tpl/button3_java.tpl",data=array)
        return t1
@route("/compare.tpl")
def b2():
	st="/home/amit/project/with_java/execution_time.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("compare.tpl",data=array,data1=time1)
        return t1

@route("/button4_java.tpl")
def b2():
	st="/home/amit/project/with_java/protocol_capture.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("java_tpl/button4_java.tpl",data=array)
        return t1
          

@route("/save",method="POST")
def b1():
  pas1=bottle.request.POST.get('val', '').strip()
  print(pas1)
  if(pas1=="123"):
     return bottle.template("either.tpl")
  else:
        return bottle.template("try.tpl")
  
@route("/n1.jpg")
def b1():
    st="/home/amit/project/Ass1/n1.JPG"
    fo=open(st,"r")
    return fo
    
@route("/button1.tpl")
def b1():
  global time1
  start_time = time.time()*1000
  cursor.execute('delete from amit where ETH_SRC=""')
  cursor.execute('Select Distinct IP_SRC,ETH_SRC from amit where IP_SRC like "192.168.%";')
  results = cursor.fetchall()
  new_time=(time.time()*1000)-start_time
  time1=time1+new_time
  output=template('python_tpl/button1.tpl',rows=results)
  return output

@route("/button1_old.tpl")
def b1():
  global time1
  start_time = time.time()*1000
  cursor.execute('delete from amit where ETH_SRC=""')
  cursor.execute('Select Distinct IP_SRC,ETH_SRC from amit where IP_SRC like "192.168.%";')
  results = cursor.fetchall()
  new_time=(time.time()*1000)-start_time
  time1=time1+new_time
  output=template('python_tpl/button1.tpl',rows=results)
  return output



@route("/button2.tpl")
def b2():
  global time1
  start_time = time.time()*1000
  cursor.execute(' select ETH_SRC,count(frame_protocols) as IPV6 from amit where frame_protocols like "%ipv6%" group by ETH_SRC ;')
  results1 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) as IPV4 from amit where frame_protocols not like "%ipv6%" group by ETH_SRC ;')
  results2 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols)   from amit where frame_protocols like "%nbns%" group by ETH_SRC ;')
  results3 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols)  from amit where frame_protocols like "%http%" group by ETH_SRC ;')
  results4 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%igmp%" group by ETH_SRC ;')
  results5 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%dns%" group by ETH_SRC ;')
  results6 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%dhcp%" group by ETH_SRC ;')
  results7 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%arp%" group by ETH_SRC ;')
  results8 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%nbdgm:smb:browser%" group by ETH_SRC ;')
  results9 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%bootp%" group by ETH_SRC ;')
  results10 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%data%" group by ETH_SRC ;')
  results11 = cursor.fetchall()
  new_time=(time.time()*1000)-start_time
  time1=time1+new_time
  output=template('python_tpl/button2.tpl',rows1=results1,rows2=results2,rows3=results3,rows4=results4,rows5=results5,rows6=results6,rows7=results7,rows8=results8,rows9=results9,rows10=results10,rows11=results11)
  return output

@route("/button2_old.tpl")
def b2():
  global time1
  start_time = time.time()*1000
  cursor.execute(' select ETH_SRC,count(frame_protocols) as IPV6 from amit where frame_protocols like "%ipv6%" group by ETH_SRC ;')
  results1 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) as IPV4 from amit where frame_protocols not like "%ipv6%" group by ETH_SRC ;')
  results2 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols)   from amit where frame_protocols like "%nbns%" group by ETH_SRC ;')
  results3 = cursor.fetchall()

  cursor.execute(' select ETH_SRC,count(frame_protocols)  from amit where frame_protocols like "%http%" group by ETH_SRC ;')
  results4 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%igmp%" group by ETH_SRC ;')
  results5 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%dns%" group by ETH_SRC ;')
  results6 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%dhcp%" group by ETH_SRC ;')
  results7 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%arp%" group by ETH_SRC ;')
  results8 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%nbdgm:smb:browser%" group by ETH_SRC ;')
  results9 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%bootp%" group by ETH_SRC ;')
  results10 = cursor.fetchall()
  cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%data%" group by ETH_SRC ;')
  results11 = cursor.fetchall()
  new_time=(time.time()*1000)-start_time
  time1=time1+new_time
  output=template('python_tpl/button2.tpl',rows1=results1,rows2=results2,rows3=results3,rows4=results4,rows5=results5,rows6=results6,rows7=results7,rows8=results8,rows9=results9,rows10=results10,rows11=results11)
  return output

@route("/button4.tpl")
def b2():
	global time1
	start_time = time.time()*1000
	st="/home/amit/project/withmysql/amit.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("python_tpl/button4.tpl",data=array)
        new_time=(time.time()*1000)-start_time
        time1=time1+new_time
        return t1

@route("/button4_old.tpl")
def b2():
	global time1
	start_time = time.time()*1000
	st="/home/amit/project/withmysql/amit.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("python_tpl/button4.tpl",data=array)
        new_time=(time.time()*1000)-start_time
        time1=time1+new_time
        return t1

@route("/button_page.tpl")
def b2():
	global time1
	start_time = time.time()*1000
	st="/home/amit/project/with_java/dns.txt"
	array=[]
        with open(st,"r") as f:
	 for line in f:
	    array.append(line)
	    t1=bottle.template("python_tpl/button_page.tpl",data=array)
        new_time=(time.time()*1000)-start_time
        time1=time1+new_time
        return t1
          


@route("/button3.tpl")
def b3():
  global time1
  start_time = time.time()*1000
  cursor.execute('delete from amit where ETH_SRC="70:18:8b:d9:c9:c5" or ETH_SRC="94:44:52:72:b9:3c";');
  cursor.execute('delete from amit where ETH_SRC=""')
  cursor.execute("select ETH_SRC ,((sum(frame_len)/(select sum(frame_len) from amit))*100) AS per from amit group by ETH_SRC;")
  results = cursor.fetchall()
  cursor.execute("select count(distinct ETH_SRC) from amit;")
  results2=cursor.fetchone();
  new_time=(time.time()*1000)-start_time
  time1=time1+new_time
  output=template('python_tpl/button3.tpl',rows=results,row2=results2)
  return output

@route("/button3_old.tpl")
def b3():
  global time1
  start_time = time.time()*1000
  cursor.execute('delete from amit where ETH_SRC="70:18:8b:d9:c9:c5" or ETH_SRC="94:44:52:72:b9:3c";');
  cursor.execute('delete from amit where ETH_SRC=""')
  cursor.execute("select ETH_SRC ,((sum(frame_len)/(select sum(frame_len) from amit))*100) AS per from amit group by ETH_SRC;")
  results = cursor.fetchall()
  cursor.execute("select count(distinct ETH_SRC) from amit;")
  results2=cursor.fetchone();
  new_time=(time.time()*1000)-start_time
  time1=time1+new_time
  output=template('python_tpl/button3.tpl',rows=results,row2=results2)
  return output

@route('/button5.tpl')
def index():
    return bottle.template("python_tpl/button5.tpl")
@route('/button5_old.tpl')
def index():
    return bottle.template("python_tpl/button5.tpl")

     
debug(True)
run(host='localhost', port=8080)
