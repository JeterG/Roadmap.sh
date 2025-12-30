import requests
from rich.pretty import pprint as print


class GithubActivity:
    def __init__(self):
        self.__request__("jeterg")

    def __request__(self, username):
        url = f"https://api.github.com/users/{username}/events"
        http_resp = requests.get(url)
        if http_resp.status_code == 200:
            output = ""
            json_resp = http_resp.json()
            # for obj in json_resp:
            # output+= f""
            import ipdb

            ipdb.set_trace()


GithubActivity()
