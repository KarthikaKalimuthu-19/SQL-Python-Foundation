#--write json
import json

dict={'empid':1,'empname':'karthika','salary':30000}

#serilaization json: python obj to json
json_obj=json.dumps(dict)

with open('sample.json','w') as fp:
    fp.write(json_obj)
