import requests
import re
import json

def login(username: str, passwd: str) -> requests.session():
    sess = requests.session()
    login_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'ua.scu.edu.cn',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '5',
        'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'
    }
    login_get = 'http://ua.scu.edu.cn/login'
    res = sess.get(login_get, headers=login_headers)
    exec_value = re.findall('.*"execution" value="(.*?)"/>', res.text)[0]
    login_post = 'http://ua.scu.edu.cn/login'
    login_post_args = {
        'username': username,
        'password': passwd,
        'submit': 'LOGIN',
        'type': 'username_password',
        'execution': exec_value,
        '_eventId': 'submit'
    }
    sess.post(login_post, data=login_post_args)
    return sess


def casLogin(username: str, passwd: str) -> requests.session():
    sess = requests.session()
    casUrl = 'http://my.scu.edu.cn/userPasswordValidate.portal'
    casHeaders = {
        'Accept': 'text/html,application/xhtml+xml,'
                  'application/xml;q=0.9,image/avif,'
                  'image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '169',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'my.scu.edu.cn',
        'Origin': 'http://my.scu.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://my.scu.edu.cn/',
        'Upgrade-Insecure-Requests': '10',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36'
    }
    casData = {
        'Login.Token1': username,
        'Login.Token2': passwd,
        'goto': 'http://my.scu.edu.cn/loginSuccess.portal',
        'gotoOnFail': 'http://my.scu.edu.cn/loginFailure.portal'
    }
    sess.headers = casHeaders
    res = sess.post(casUrl, headers=casHeaders, data=casData)
    if len(res.text) == 99:
        raise Exception
    return sess


def zhjwLogin(username: str, passwd: str) -> requests.session():
    sess = casLogin(username, passwd)
    zhjw_headers = {
        'Accept': 'text/html,application/xhtml+xml,'
                  'application/xml;q=0.9,image/avif,'
                  'image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'zhjw.scu.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://zhjw.scu.edu.cn/choose.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36'
    }
    sess.headers = zhjw_headers
    sess.get('http://zhjw.scu.edu.cn/')
    sess.get('http://zhjw.scu.edu.cn/zgsyLogin')
    sess.get('http://zhjw.scu.edu.cn/login')
    sess.get('http://zhjw.scu.edu.cn/casLogin')
    sp_check_headers = {
        'Accept': 'text/html,application/xhtml+xml,'
                  'application/xml;q=0.9,image/avif,'
                  'image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '48',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'zhjw.scu.edu.cn',
        'Origin': 'http://zhjw.scu.edu.cn',
        'Referer': 'http://zhjw.scu.edu.cn/casLogin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36'
    }
    sp_check_data = {
        'j_username': username,
        'j_password': '1',
        'j_captcha': ''
    }

    sess.post('http://zhjw.scu.edu.cn/j_spring_security_check',
              headers=sp_check_headers,
              data=sp_check_data)
    return sess



