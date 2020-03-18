'''
@Author: your name
@Date: 2020-03-18 08:49:14
@LastEditTime: 2020-03-18 08:59:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /my_blog/server/utils.py
'''
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from models import User
from flask import request
import json
from secret_key import key
# 根据token解析用户信息
def get_user(token):
    s = Serializer(key)
    try:
        data = s.loads(token)
    except:
        return None
    return User.query.filter_by(id=data['id']).first()


def post_json():
    data = request.get_data()
    return  json.loads(data.decode('utf-8'))
