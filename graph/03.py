pro=[1]
if len(pro):
   print('ok')


'''
    sanyuanzu = []  # 三元组
    n_id=[]
    m_id=[]
    for l in result:#
        rel = db.cypher_query(query='MATCH (n:'+kg_name+')-[:'+l+']->(m:'+kg_name+') RETURN id(n) as nid,id(m) as mid')
        for i in rel[0]:
            n_id.append(i[0])
            m_id.append(i[1])
            sanyuanzu.append([i[0], l, i[1]])
    entity=list(set(n_id))+list(set(m_id))
    index_result = []  # 搜索结果
    for en in entity:
        rel = db.cypher_query(
            query='MATCH (n:' + kg_name +') where id(n)='+str(en)+' RETURN n.name as n_name,id(n) as nid,properties(n) AS properties')
        index_dic = {}
        for i in rel[0]:
            index_dic.update({'id': i[1], 'name': i[0], "property": []})
            for k in i[2]:
                index_dic["property"].append([k, i[2][k]])
        index_result.append(index_dic)

    return JsonResponse({'entity':index_result,'sanyuanzu':sanyuanzu})
    '''

d=[{'db_name':'ddosi','db_type':'pg','table':'aa','ziduan':['python','java','c++']},{'db_name':'root','db_type':'mysql','table':'bb','ziduan':['jianghua','qiuyue','huanling']}]
#数据表aa(ddosi|pg)缺失['python','java','c++']字段的信息造成无法入库！请在检查修改后重新入库。)
res='其中'
for i in d:
   loda=''
   for data in i['ziduan']:
      loda+=data+','
   loda=loda[:-1]
   res+='数据表'+i['table']+'('+i['db_name']+'|'+i['db_type']+')缺失'+'['+loda+']'+'、'
res=res[:-1]+'字段的信息造成无法入库！请在检查修改后重新入库。'
print(res)