from flask import Blueprint, Response, current_app
from bson import json_util

blueprint = Blueprint('bp_demo', __name__)

@blueprint.route('/people_alternative', methods=['GET'])
def bp_people():
    db = current_app.data.driver.db['people2']
    r = db.find({})
    result_json = json_util.dumps(r)
    resp = Response(response=result_json,
                    status=200,
                    mimetype="application/json")
    return resp