import json


def pprint_response(response):
    request = response.request
    if 'X-API-KEY' in request.headers:
        request.headers['X-API-KEY'] = '********'

    try:
        response_json = response.json()
    except Exception:
        response_json = {}

    request_body = request.method == 'POST' and json.dumps(
        json.loads(request.body), indent=4
    ) or ""

    return f'''
Request:
Method: {request.method}
Url: {request.url}
Body: {request_body}
Headers: {json.dumps(dict(request.headers), indent=4)}

Response:
Status Code: {response.status_code}
Body:
{json.dumps(response_json, indent=4)}
'''
