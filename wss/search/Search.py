#对搜索内容进行处理，生成字典
def queryProcess(query):
    tmp = query.split(' ')
    print(tmp)
    meta = []
    query_dict = []
    for x in tmp:
        if x.count(':') == 0:
            query_dict.append(x)
        else:
            x = x.replace('+', ' ')
            meta = x.split(':')
            query_dict.append({meta[0]: meta[1]})
    return query_dict

#向es查询
# def search(query_dict):
#     should_list = []
#     must_list = []
#     tmp = []
#     for x in query_dict:
#         if str(x).count(':') == 0:
#             tmp = [
#                 {'match': {'age': x}},
#                 {'match': {'gender': x}},
#                 {'match': {'city': x}},
#                 {'match': {'employer': x}},
#                 {'match': {'state': x}},
#             ]
#             should_list.extend(tmp)
#         else:
#             must_list.append({'match': x})
#
#     query_dsl = {
#         'query': {
#             'bool': {
#                 'should': should_list,
#                 'must': must_list
#             }
#         }
#     }
#
#     es = Elasticsearch("127.0.0.1:9200")
#     responce = es.search(index="bank", body=query_dsl)
#     data = responce["hits"]["hits"]
#     return data