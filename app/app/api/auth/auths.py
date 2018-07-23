import jwt, datetime, time
from flask import jsonify
from app import db
from ..user.model import Users
from ... import returnMsg
from bson.json_util import dumps

class Auth():
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'username': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                'secret',
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, 'secret', options={'verify_exp': False})
            if ('data' in payload and 'username' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token expired'
        except jwt.InvalidTokenError:
            return 'Token invalid'


    def authenticate(self, username, password):
        """
        :param password:
        :return: json
        """
        userInfo = db.UserCollection.find_one({"username": username})
        if (userInfo is None):
            return jsonify(returnMsg.falseReturn('', 'user is empty'))

        else:
            if (Users.check_password(Users, userInfo['password'], password)):
                login_time = int(time.time())
                userInfo['login_time'] = login_time
                Users.update(Users, userInfo['username'], {"login_time": login_time})

                token = self.encode_auth_token(userInfo['username'], login_time)
                return jsonify(returnMsg.trueReturn(token.decode(), 'login success'))
            else:
                return jsonify(returnMsg.falseReturn({'ori': userInfo['password'], 'mine': password}, 'password not correct'))

    def identify(self, request):
        """
        :return: list
        """
        auth_header = request.headers.get('Authorization')
        if (auth_header):
            auth_tokenArr = auth_header.split(" ")
            if (not auth_tokenArr or auth_tokenArr[0] != 'JWT' or len(auth_tokenArr) != 2):
                result = returnMsg.falseReturn('', 'provide correct header')
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user = Users.get(Users, payload['data']['username'])

                    if (user is None):
                        result = returnMsg.falseReturn('', 'can`t find this user')
                    else:
                        if (user['login_time'] == payload['data']['login_time']):
                            result = returnMsg.trueReturn(user['username'], 'request success')
                        else:
                            result = returnMsg.falseReturn('', 'token has change, refresh')
                else:
                    result = returnMsg.falseReturn('', payload)
        else:
            result = returnMsg.falseReturn('', 'no token are provide')
        return result
