from .oxerator import Miner
from .utils import OxeratorException
from time import sleep
from random import randint
from .utils import log


class Commands(Miner):
    def __init__(self, token):
        super().__init__(token)

    def getme(self):
        try:
            user = self.make_request(url='/users/@me', method='GET',
                                     headers=self._headers())
            return f"**USERNAME**: {user['username']} \n**ID**: <@{user['id']}>"
        except Exception as e:
            log(OxeratorException(type(e).__name__, e, 'cannot fetch user'))

    def getresponse(self, channel):
        try:
            response = self.make_request(url='/channels/{}/messages?limit=1'.format(channel), method='GET',
                                         headers=self._headers())
            for d in response:
                return "Response: " + d['content']
        except Exception as e:
            log(OxeratorException(type(e).__name__, e,
                                  "fetch response failed at channel id %s" % channel))

    def status(self, text, status):
        json = {
            'custom_status': {
                'text': text
            }
        }
        if status in ['dnd', 'online', 'idle']:
            json.update({'status': status})
            status = self.make_request(method='PATCH',
                                       url='users/@me/settings', headers=self._headers(), json=json)
            return status
        else:
            raise OxeratorException(
                'Invalid Status: `%s`' % status, 'Valid Status: {}'.format([i for i in ['dnd', 'online', 'idle']]))

    def send(self, channel, content, start, end, bool):
        json = {
            "content": str(content)
        }
        try:
            if bool:
                message = self.make_request(method='POST',
                                            url="channels/{}/messages".format(channel), json=json, headers=self._headers())
                sleep(randint(start, end))
                return 'Sent: ' + message['content']

        except Exception as e:
            log(OxeratorException(type(e).__name__, e,
                                  "Sending command failed at channel id %s | content %s" % (channel, content)))

    def owo(self, prefix: str, cmd: str):
        return prefix + str(cmd)
