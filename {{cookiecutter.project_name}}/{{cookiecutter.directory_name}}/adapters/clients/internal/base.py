
import requests
from config import SETUP
from urllib.parse import urlencode


class ClientBase(object):
    __CLIENTS = {
        'msa_api': SETUP.MSA_API_URL,
        'msa_communicator': SETUP.MSA_COMMUNICATOR_URL
    }

    def __init__(self, apikey: str = SETUP.API_FK_KEY, clients=__CLIENTS):
        self.__apikey = apikey
        self.__clients: dict = clients

    def get_predefined_clients(self):
        return self.__CLIENTS.copy()

    def __get_url(self, host):
        url = self.__clients.get(host, None)
        assert url is not None, 'Not found: %s' % host
        return url

    def get_url(self, segment: str, params: dict = None, client='msa_api'):
        host = self.__get_url(client)
        query = ''
        if params:
            query = "&{}".format(urlencode(params))
        url = "{}/{}?apikey={}{}".format(host, segment, self.__apikey, query)
        return url

    def consume_request(self, method: str = 'get', payload: dict = {},
                        url: str = None, headers: dict = None, files: dict = None,
                        data: dict = None, response_file: bool = False):
        assert method in ['get', 'post', 'put', 'patch', 'delete'], f"method {method} not valid"
        if method == 'post':
            response = requests.post(url, json=payload, headers=headers, files=files, data=data)
        elif method == 'put':
            response = requests.put(url, json=payload, headers=headers, files=files, data=data)
        elif method == 'patch':
            response = requests.patch(url, json=payload, headers=headers, files=files, data=data)
        elif method == 'delete':
            response = requests.delete(url, json=payload, headers=headers, files=files, data=data)
        elif method == 'get':
            response = requests.get(url, headers=headers)
        else:
            response = None

        assert response is not None
        assert response.status_code in [200, 201, 203, 204, 422], f"Error on getting information " \
            f"{response.status_code} {payload} | {response.json()}"
        try:
            if response_file is False:
                if type(response.json()) == dict and 'data' in response.json():
                    return response.json()['data']
                return response.json()
            else:
                return response.content
        except Exception:
            return True
