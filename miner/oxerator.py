from .variables import DISCORD_API_URL
import requests
from fake_useragent import UserAgent
from base64 import b64encode
from json import dumps
from .utils import OxeratorException
from capmonster_python import ImageToTextTask
from .utils import log

class Miner:
    def __init__(self, token):
        self._token = token
        self.url = DISCORD_API_URL

    def token(self):
        return self._token

    def _headers(self, **kwargs):
        headers = {
            'authorization': self._token,
            "cookie": "__dcfduid = fabdb9f0ab9811ed96c4b7c7f8da6ecd__sdcfduid = fabdb9f1ab9811ed96c4b7c7f8da6ecd8bf0ec47c9c5e745dfd601add91d4cbd3472210d507fe58d308b308df194a54c",
            "origin": "https://discord.com",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": UserAgent().random,
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": self._x_super_props()
        }
        if kwargs:
            headers.update(kwargs)
        return headers

    def _x_super_props(self):
        browser_properties = {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "browser_user_agent": UserAgent().random,
            "browser_version": "96.0.4664.110",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 175517,
            "client_event_source": None
        }

        return b64encode(
            dumps(browser_properties).encode('utf-8')).decode('utf-8')

    def make_request(self, url, method, headers, json=None, data=None):
        try:
            r = requests.request(
                method=method, url=self.url + "{}".format(url), headers=headers, json=json, data=data)
            return r.json()
        except Exception as e:
            log(OxeratorException(type(e).__name__,
                  e, "Request Failed at %s" % url))

    def solve(self, apikey):
        capmonster = ImageToTextTask(apikey)
        task_id = capmonster.create_task(image_path='./captcha.png')
        result = capmonster.join_task_result(task_id)
        result = result.get("text")
        return result
