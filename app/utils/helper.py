from flask import jsonify


def Json(data):
    '''
    transform model(s) to json string
    '''
    if isinstance(data, list):
        r = {}
        for k, d in enumerate(data):
            r[k] = {c.name: getattr(d, c.name, '') for c in d.__table__.columns}
        return jsonify(r)
    else:
        return jsonify({c.name: getattr(data, c.name, '') for c in data.__table__.columns})
