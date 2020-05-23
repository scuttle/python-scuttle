#!/usr/bin/env python3

import requests

class BaseApi:
    version = None
    def __init__(self, domain, api_key):
        self.endpoint = "https://{}.scuttle.bluesoul.net/api/v{}".format(
            domain, type(self).version)
        self.api_key = api_key

    def request(self, namespace, value=None):
        response = requests.get(
            "{}/{}".format(
                self.endpoint,
                namespace.format(value)),
            headers={"Authorization": "Bearer {}".format(self.api_key)})
        print(response.text)
        return response.json()
