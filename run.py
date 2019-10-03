import requests
import json
import yaml

yaml.warnings({'YAMLLoadWarning': False})
data = yaml.load(open('data.yml','r',encoding='utf-8').read())

def login(url,mail,passwd) -> str:
    s = requests.session()
    r = s.post('%s/auth/login'%url,data={'email':mail,'passwd':passwd,'remember_me':True})
    if r.status_code!=200:
        return '%s @ %s : HTTP Error %s'%(mail,url,r.status_code)
    try:
        d = json.loads(r.text)
    except:
        return '%s @ %s : Error'%(mail,url)
    if d['ret'] != 1:
        return '%s @ %s : %s'%(mail,url,d['msg'])
    try:
        r2 = s.post('%s/user/checkin'%url)
    except:
        return '%s @ %s : Error'%(mail,url)
    if r2.status_code!=200:
        return '%s @ %s : HTTP Error %s'%(mail,url,r2.status_code)
    d2 = json.loads(r2.text)
    return '%s @ %s : %s'%(mail,url,d2['msg'])

for airport in data['airport']:
    for user in data['user']:
        print(login(airport,user['mail'],user['passwd']))
