#!/usr/bin/env python3

import requests

class BaseApi:
    version = None
    def __init__(self, domain, api_key):
        self.endpoint = "https://{}.scuttle.bluesoul.net/api/v{}".format(
            domain, type(self).version)
        self.api_key = api_key

    def request(self, namespace, value=None):
        response = requests.get("{}/{}/{}".format(
            self.endpoint,
            namespace,
            "" if value is None else value),
            headers={"Authorization": "Bearer {}".format(self.api_key)})
        return response.json()

