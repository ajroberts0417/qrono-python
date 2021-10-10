import requests
import datetime
import json


api_key = None
api_base = "https://qrono.dev"


class QronoError(Exception):
    pass


class QronoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            # TODO This will need to be adjusted for timezones somehow
            return obj.isoformat()
        return super().default(obj)


class QronoObject(dict):
    '''
    A simple class that wraps a dictionary and allows
    object dot notation style access.

    Used to convert requests response json into objects.

    Based off of the StripeObject class here:
    https://github.com/stripe/stripe-python/blob/master/stripe/stripe_object.py

    TODO add more edge case functionality.
    '''

    def __getattr_(self, key):
        try:
            return self[key]
        except KeyError as err:
            raise AttributeError(*err.args)

    @staticmethod
    def from_dict(data):
        obj = QronoObject()

        if isinstance(data, list):
            return [
                QronoObject.from_dict(value)
                for value in data
            ]
        elif isinstance(data, dict):
            for key, value in data.items():
                obj[key] = QronoObject.from_dict(value)
            return obj
        else:
            return data
        return obj


class APIRequestor:
    '''
    Wrap the requests library
    '''
    def _get_headers(self):
        if api_key is None:
            raise QronoError("`qrono.api_key` is not set!")

        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-API-KEY": api_key,
        }

    def get(self, url, params):
        return requests.request(
            "GET",
            api_base + url,
            params=params,
            headers=self._get_headers())

    def post(self, url, data):
        return requests.request(
            "POST",
            api_base + url,
            data=json.dumps(data, cls=QronoJSONEncoder),
            headers=self._get_headers())

    def put(self, url, data):
        pass

    def patch(self, url, data):
        pass

    def delete(self, url):
        pass


'''
API resource wrappers inspired by the stripe-python wrapper

See the contents of this folder:
https://github.com/stripe/stripe-python/tree/master/stripe/api_resources

Consider adding a base class to collect functionality, like:
https://github.com/stripe/stripe-python/blob/master/stripe/api_resources/abstract/api_resource.py
'''


class Item():
    @classmethod
    def list(cls, **params):
        requestor = APIRequestor()
        result = requestor.get("/api/items/", params)
        return result

    @classmethod
    def create(cls, **kwargs):
        requestor = APIRequestor()
        result = requestor.post("/api/items/", kwargs)
        return result


class Booking():
    @classmethod
    def list(cls, **params):
        requestor = APIRequestor()
        result = requestor.get("/api/items/", params)
        return result

    @classmethod
    def create(cls, **kwargs):
        requestor = APIRequestor()
        result = requestor.post("/api/items/", kwargs)
        return result
