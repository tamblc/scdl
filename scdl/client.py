# -*- encoding: utf-8 -*-

import requests
from scdl import CLIENT_ID


class Client():

    def get_collection(self, url):
        resources = list()
        while url:
            response = requests.get(url, params={
                'client_id': CLIENT_ID,
                'linked_partitioning': '1',
            })
            json_data = response.json()
            if 'collection' in json_data:
                resources.extend(json_data['collection'])
            else:
                resources.extend(json_data)
            if 'next_href' in json_data:
                url = json_data['next_href']
            else:
                url = None
        return resources
