import json
from getpass import getpass
import os
from queue import Queue
from threading import Thread
from time import sleep

import click
import easygui
from js2py import eval_js
from path import Path
from rich import print

q = Queue()


convert = eval_js(r'function convert(t){let l=[],n=t.split("\n");return n.forEach(function(e,t){e=e.split("\t");if(7==e.length){let t={};t.domain=e[0],t.httpOnly="TRUE"===e[1],t.path=e[2],t.secure="TRUE"===e[3];let n=e[4];17==n.length&&(n=Math.floor(n/1e6-11644473600)),t.expirationDate=parseInt(n),t.name=e[5],t.value=e[6],l.push(t)}}),JSON.stringify(l,null,2)}')
os.system('cls')
bb = f'''[magenta]
d8b   db    d88b
888o  88    `8P'
88V8o 88     88
88 V8o88     88
88  V888 db. 88
VP   V8P Y8888P[.magenta]
[yellow]by https://lolz.guru/members/2977610[/yellow]
'''
#удалил гей
print(bb)

def get_cookies():
    path = easygui.diropenbox('Select logs floader')
    cookies = []
    for file in Path(path).glob('*.txt'):
        if file not in cookies and file:
            cookies.append(os.path.join(file))
    for file in Path(path).glob('**/*.txt'):
        if file not in cookies and file:
            cookies.append(os.path.join(file))
    print('[green]Count files .txt:[green]',len(cookies))
    return cookies


def convert_cookie():
        cookieFile = q.get()
        try:
            cookie = open(cookieFile,'r+',encoding='utf8',errors='ignore').read()
            cookie_json = json.loads(convert(cookie))
            cookie_str = json.dumps(cookie_json)
            if cookie_json:
                open('result.txt','a+').write(
                    cookie_str+'\n\n'
                )
        except:pass
        q.task_done()
        bar.update(1)

def main():
    global bar
    cookies = get_cookies()
    bar =  click.progressbar(length=len(cookies),label='Convert cookies:')
    for cookieFile in cookies:
        q.put(cookieFile)
    for cookieFile in cookies:
        sleep(0.1)
        Thread(target=convert_cookie,daemon=True).start()
    q.join()
try:
    main()
except KeyboardInterrupt:
    pass
getpass('\nPress enter...')

