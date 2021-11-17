from neomodel import db, Q
from kgmodel.models import Kgmodel
from graph.models import graphnode
import psycopg2
# x=Kgmodel.nodes.get(name='土地供应模型')
# print(x)
# db.cypher_query(
#   query='MATCH (r) WHERE id(r) = 27 SET r.模型版本 = "kg1.0",r.自然资源要素="土地",r.业务类型="供应",'
#        'r.模型描述="土地供应模型描述了土地流转供应中的业务关系逻辑。",r.创建时间="2021-10-1",r.模型状态="可用"')

#db.cypher_query(query='LOAD CSV WITH HEADERS FROM "file:///H:/python文件/ziran/test.csv" AS line MERGE (p:郑州国土{name:line.name})')
# graphnode(name='郑州市国土供应').save()

#db.cypher_query(query='MERGE (n:Kgmodel {name: "国土规划"}) SET n.区号 = 0371')

'''
rel = db.cypher_query(query='MATCH (n:f) RETURN n.name as n_name,id(n) as nid')
index_result=[]#搜索结果
for i in rel[0]:
        index_result.append([i[0],i[1]])
print(index_result)
'''
#result1 = db.cypher_query(
#  query="MATCH (a:行政区划)-[r]->(b:行政区划) RETURN id(a) as a_id,type(r),r.name as rname,id(r) as r_id,id(b) as b_id")


#result=db.cypher_query(query='MATCH (p1:xiangzhen {name: "永和镇"}), (p2:地点 {name: "新郑机场"}),path = (p1)-[*]-(p2) RETURN path AS shortestpath,NODES(path) AS nodes')
#print(result[0][0])


'''
conn = psycopg2.connect(dbname="xingxing", user="postgres", password="123456",host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("select  DISTINCT bz from cun")
rows = cur.fetchall()
column_name=[]
for row in rows:
    if row[0]:
        column_name.append(row[0])
print(column_name)
'''

'''
rel = db.cypher_query(query='MATCH (n:行政区划{name:"乡镇"}) RETURN properties(n) AS properties')
arr=[]#某个节点的全部属性
sx=rel[0][0][0]
for s in sx:
    arr.append(s)
print(arr)
'''


li=['乡镇','地级市']

'''
for i in range(len(li)):
    for j in range(i+1,len(li)):
        rel = db.cypher_query(query='MATCH (n:行政区划{name:'+'\''+li[i]+'\''+'})-[r]->(m:行政区划{name:'+'\''+li[j]+'\''+'}) RETURN type(r),properties(r) AS properties')
        if len(rel[0]):
            re_name=rel[0][0][0]#关系名
            re_type=rel[0][0][1]['lx']#关系类型

        rel = db.cypher_query(query='MATCH (n:行政区划{name:' + '\'' + li[i] + '\'' + '})<-[r]-(m:行政区划{name:' + '\'' + li[
            j] + '\'' + '}) RETURN type(r),properties(r) AS properties')
        if len(rel[0]):
            re_name = rel[0][0][0]  # 关系名
            re_type = rel[0][0][1]['lx']  # 关系类型
'''

#获取节点的数据库信息

dl=db.cypher_query(query='MATCH (p1), (p2),path =(p1)-[*]-(p2)  WHERE id(p1)=2914 AND id(p2)=2912 RETURN NODES(path) as node')
print(dl[0][0][0])



#db.cypher_query(query='MATCH (r:'+dl[0][0][0]+') DETACH DELETE r')
'''
relaiton={}
sx=[]
re_name=result2[0][0][0]
relaiton.update({'re_name':re_name})

for i in result2[0][0][1]:
    sx.append([i,'string',result2[0][0][1][i]])
relaiton.update({'sx':sx})
relaiton.update({'id':result2[0][0][2]})
print(relaiton)
'''

#rel = db.cypher_query(query='MATCH (n:Kgmodel) where n.bq="乡镇" RETURN count(n)')
#print(rel)


#s='库名1:[表名1,表名2,表名3]'
#print(s.split(':')[1])

#rel = db.cypher_query(query='MATCH (n:Kgmodel{name:"行政区划"}) RETURN n.Resourcemeta as n_re,n.Businesstype as n_bu')
#print(rel[0][0][0])


'''
model_name=[]
rel = db.cypher_query(query='MATCH (n:行政区划) RETURN n.name as n_name')
for md in rel[0]:
    model_name.append(md[0])
print(model_name)
'''

'''
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
except:
   print ("Error: unable to fetch data")
# 关闭数据库连接
db.close()
'''
'''
oritg={}
rel = db.cypher_query(query='MATCH (n) where id(n)=18108 RETURN n.orign as norign,n.create_time as ntime')
oritg.update({'create_time':rel[0][0][1]})
st=rel[0][0][0]#
database=[]
for s in st:
    fen=s.split(':')
    db_name=fen[0] #获取数据库名
    db_type=fen[1] #数据库类型
    tables=fen[2] #数据库中的表

    table_list=[]
    tabl=tables[1:][:-1].split(',')

    for tab in tabl:
        table_list.append(tab)
    database.append({'db_name':db_name,'db_type':db_type,'table':table_list})
oritg.update({'database':database})
print(oritg)
'''
'''
dbifno=[{'db_name':'ddosi','db_type':'pg','tables':['aa','bb','cc']},{'db_name':'xingxing','db_type':'Mysql','tables':['aa','bb','cc']}]
dborign={'ddosi':['aa'],'xingxing':['dd','ee']}
sf=''
for orig in dborign:
    s = '\''+orig + ':['
    for og in dborign[orig]:
        s += og + ','
    s = s[:-1] + ']'+'\''
    sf+=s+','
sf=sf[:-1]
print(sf)
'''

'''
link=[]
rel = db.cypher_query(query='MATCH (n)-[r]->(m) where id(n)=2545 and id(m)=2546 RETURN type(r),properties(r) AS properties')
print(rel[0][0][1]['lx'])
'''

'''
rel = db.cypher_query(query='MATCH (n:ee{name:"乡镇"}) RETURN properties(n) AS properties')
arr = []  # 某个节点的全部属性
sx = rel[0][0][0]
for s in sx:
  arr.append(s)
remo_list=['name','entity_id','名称']
for re in remo_list:
    arr.remove(re)
arr_map={}
for ar in arr: #属性名
    rel = db.cypher_query(query='MATCH (n:ee{name:"乡镇"}) RETURN n.'+ar+'')
    sxm=rel[0][0][0]
    arr_map.update({sxm:ar})
print(arr_map)
'''
#s='业务,'
#print(s.split(',')[:-1])



