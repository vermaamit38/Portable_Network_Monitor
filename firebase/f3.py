import MySQLdb
import json
import collections

import time
now = time.strftime("%c")

db = MySQLdb.connect("localhost","root","","project" )
cursor = db.cursor()
from firebase import firebase
firebase=firebase.FirebaseApplication("https://networkmonitor.firebaseIO.com")



 #Getting distinct IP and Mac addresss---------------------------------------------
cursor.execute('Select Distinct IP_SRC,ETH_SRC from amit where IP_SRC like "192.168.%";')
 
rows = cursor.fetchall()
 
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], row[1])
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'mac_ip.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['IP_SRC'] = row[0]
    d['ETH_SRC'] = row[1]
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'mac_ip_object.js'
f = open(objects_file,'w')

da=time.strftime("%d-%m-%y")

firebase.post(now,{"Mac-IP":j})

print >> f, j
#------Bandwidth------------------------------------------------
cursor.execute("select ETH_SRC ,TRUNCATE(((sum(frame_len)/(select sum(frame_len) from amit))*100),2) AS per from amit group by ETH_SRC")
rows = cursor.fetchall()
 
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'bandwidth.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['ETH_SRC'] = row[0]
    d['per'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'bandwidth_object.js'
f = open(objects_file,'w')
da=time.strftime("%d-%m-%y")

firebase.post(now,{"bandwidth":j})

#------Protocol count-------------------------------------------
cursor.execute(' select ETH_SRC,count(frame_protocols) as IPV6 from amit where frame_protocols like "%ipv6%" group by ETH_SRC ;')
results1 = cursor.fetchall()
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_ipv6_packet.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['ipv6'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_ipv6_packet_object.js'
f = open(objects_file,'w')
parse1=j

#---@@@@@@@@@@@@@------------------
cursor.execute(' select ETH_SRC,count(frame_protocols) as IPV4 from amit where frame_protocols not like "%ipv6%" group by ETH_SRC ;')
results2 = cursor.fetchall()
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_ipv4_packet.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['ipv6'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_ipv4_packet_object.js'
f = open(objects_file,'w')

parse2=j

#-----------@@@@@@@@@@@@@@--------------------


cursor.execute(' select ETH_SRC,count(frame_protocols)   from amit where frame_protocols like "%nbns%" group by ETH_SRC ;')
results3 = cursor.fetchall()
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_nbns_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['nbns'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_nbns_protocol_object.js'
f = open(objects_file,'w')
parse3=j

#-----------@@@@@@@@@@@@@@--------------------



cursor.execute(' select ETH_SRC,count(frame_protocols)  from amit where frame_protocols like "%http%" group by ETH_SRC ;')
results4 = cursor.fetchall()

# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_http_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['http'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_http_protocol_object.js'
f = open(objects_file,'w')
parse4=j

#-----------@@@@@@@@@@@@@@--------------------



cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%igmp%" group by ETH_SRC ;')
results5 = cursor.fetchall()
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_igmp_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['igmp'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_igmp_protocol_object.js'
f = open(objects_file,'w')
parse5=j

#-----------@@@@@@@@@@@@@@--------------------


cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%dns%" group by ETH_SRC ;')
results6 = cursor.fetchall()
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_dns_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['dns'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_dns_protocol_object.js'
f = open(objects_file,'w')
parse6=j

#-----------@@@@@@@@@@@@@@--------------------



cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%dhcp%" group by ETH_SRC ;')
results7 = cursor.fetchall()
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_dhcp_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['dhcp'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_dhcp_protocol_object.js'
f = open(objects_file,'w')
parse7=j

#-----------@@@@@@@@@@@@@@--------------------



cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%arp%" group by ETH_SRC ;')
results8 = cursor.fetchall()
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_arp_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['arp'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_arp_protocol_object.js'
f = open(objects_file,'w')
parse8=j

#-----------@@@@@@@@@@@@@@--------------------


cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%nbdgm:smb:browser%" group by ETH_SRC ;')
results9 = cursor.fetchall()

# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_nbdgm:smb:browser_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['nbdgm'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_nbdgm:smb:browser_protocol_object.js'
f = open(objects_file,'w')
parse9=j

#-----------@@@@@@@@@@@@@@--------------------



cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%bootp%" group by ETH_SRC ;')
results10 = cursor.fetchall()

# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_bootp_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['bootp'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_bootp_protocol_object.js'
f = open(objects_file,'w')
parse10=j

#-----------@@@@@@@@@@@@@@--------------------



cursor.execute(' select ETH_SRC,count(frame_protocols) from amit where frame_protocols like "%data%" group by ETH_SRC ;')
results11 = cursor.fetchall()
# Convert query to row arrays
 
rowarray_list = []
for row in rows:
    t = (row[0], float(row[1]))
    rowarray_list.append(t)
 
j = json.dumps(rowarray_list)
rowarrays_file = 'count_http:data_protocol.js'
f = open(rowarrays_file,'w')
print >> f, j
 
# Convert query to objects of key-value pairs
 
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['mac'] = row[0]
    d['http-data'] = float(row[1])
    objects_list.append(d)
 
j = json.dumps(objects_list)
objects_file = 'count_http:data_protocol.js'
f = open(objects_file,'w')
parse11=j

#-----------@@@@@@@@@@@@@@--------------------
#-----------------
firebase.post(now,{"count_ipv6_packet":parse1,"count_ipv4_packet":parse2,"count_nbns_protocol":parse3,"count_http_protocol":parse4,"count_igmp_protocol":parse5,"count_dns_protocol":parse6,"count_dhcp_protocol":parse7
,"count_arp_protocol":parse8,"count_nbdgm_smb_browser_protocol":parse9,"count_bootp_protocol":parse10,"count_http-data_protocol":parse11})

