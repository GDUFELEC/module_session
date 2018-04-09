# coding=utf-8
from tablestore import *
import hashlib
import uuid
OTS_ID = ""
OTS_SECRET = ""
OTS_ENDPOINT = ""
OTS_INSTANCE = ""
table_name = ''
client = OTSClient(OTS_ENDPOINT, OTS_ID, OTS_SECRET, OTS_INSTANCE)

def check(token):
    primary_key = [('token',token)]
    columns_to_get = []

    consumed, return_row, next_token = client.get_row(table_name, primary_key, columns_to_get)
    if return_row == None:
        return False
    return True
 
def new(columns = []):
    m1 = str(uuid.uuid1())
    m=hashlib.md5()
    m.update(m1.encode("UTF-8"))
    token =  m.hexdigest()
    primary_key = [('token',token)]
    attribute_columns =  columns
    row = Row(primary_key, attribute_columns)
    condition = Condition(RowExistenceExpectation.EXPECT_NOT_EXIST)
    consumed, return_row = client.put_row(table_name, row, condition)
    return token
    
def read(token):
    primary_key = [('token',token)]
    columns_to_get = []

    consumed, return_row, next_token = client.get_row(table_name, primary_key, columns_to_get)
    if return_row == None:
        return False
    reply = {}
    for att in return_row.attribute_columns:
        reply[att[0]] = att[1]
    return reply