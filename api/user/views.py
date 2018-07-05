from .. import db
from . import user_blueprint
from flask import request,make_response,json
from urllib import parse
from bson.json_util import dumps
@user_blueprint.route('/<string:account>/profile',methods=['GET'])
def query_profile(account):
        if request.method =='GET':
                data = db.accountCollection.find({'profile.account':account},{'profile':1})
                return make_response(dumps(data[0]),200)


@user_blueprint.route('/profile2',methods=['GET'])
def query_profile2():
        if request.method == 'GET':
                #url = urlrequest.Request.get_full_url()
                url = request.url
                query_component = parse.urlparse(url).query
                account = parse.parse_qs(query_component)['account'][0]
                data = db.accountCollection.find({'profile.account':account},{'profile':1})
                return make_response(dumps(data[0]),200)

