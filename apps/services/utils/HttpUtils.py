import requests

"""
HttpUtils
---------

Contains all methods to execute HTTP calls.
"""


def doHttpGet(url, params={}, headers={}):
    """
    Do an HTTP GET call.
    :param url: String - Url to call.
    :param params: JSON - URI parameters. ex: {'key1':'value1', 'key2':'value2'}
        -> http://localhost?key1=value1&key2=value2
        Default: {}
    :param headers: JSON - Custom headers to give to the request.
        Default: {}
    :return: The result of the GET request.
    """
    return requests.get(url=url, params=params, headers=headers)


def doHttpPost(url, params={}, headers={}, body={}):
    """
    Do an HTTP POST call.
    :param url: String - Url to call.
    :param params: JSON - URI parameters. ex: {'key1':'value1', 'key2':'value2'}
        -> http://localhost?key1=value1&key2=value2
        Default: {}
    :param headers: JSON - Custom headers to give to the request.
        Default: {}
    :param body: Body of the request.
    :return: The result of the POST request.
    """
    return requests.post(url=url, params=params, data=body, headers=headers)


def doHttpDelete(url, params={}, headers={}):
    """
    Do an HTTP DELETE call.
    :param url: String - Url to call.
    :param params: JSON - URI parameters. ex: {'key1':'value1', 'key2':'value2'}
        -> http://localhost?key1=value1&key2=value2
        Default: {}
    :param headers: JSON - Custom headers to give to the request.
        Default: {}
    :return: The result of the DELETE request.
    """
    return requests.delete(url=url, params=params, headers=headers)


def doHttpPatch(url, params={}, headers={}, body={}):
    """
    Do an HTTP PATCH call.
    :param url: String - Url to call.
    :param params: JSON - URI parameters. ex: {'key1':'value1', 'key2':'value2'}
        -> http://localhost?key1=value1&key2=value2
        Default: {}
    :param headers: JSON - Custom headers to give to the request.
        Default: {}
    :param body: Body of the request.
    :return: The result of the PATCH request.
    """
    return requests.patch(url=url, params=params, data=body, headers=headers)


def doHttpPut(url, params={}, headers={}, body={}):
    """
    Do an HTTP PUT call.
    :param url: String - Url to call.
    :param params: JSON - URI parameters. ex: {'key1':'value1', 'key2':'value2'}
        -> http://localhost?key1=value1&key2=value2
        Default: {}
    :param headers: JSON - Custom headers to give to the request.
        Default: {}
    :param body: Body of the request.
    :return: The result of the PUT request.
    """
    return requests.put(url=url, params=params, data=body, headers=headers)
