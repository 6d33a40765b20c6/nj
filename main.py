from queue import Queue
from threading import Thread
from time import sleep
import easygui
from path import Path
import click
from colorama import Fore, init
from js2py import eval_js

init()
q = Queue()
C=Fore
convert = eval_js(r'function convert(t){let l=[],n=t.split("\n");return n.forEach(function(e,t){e=e.split("\t");if(7==e.length){let t={};t.domain=e[0],t.httpOnly="TRUE"===e[1],t.path=e[2],t.secure="TRUE"===e[3];let n=e[4];17==n.length&&(n=Math.floor(n/1e6-11644473600)),t.expirationDate=parseInt(n),t.name=e[5],t.value=e[6],l.push(t)}}),JSON.stringify(l,null,2)}')

bb = f'''{C.LIGHTGREEN_EX}
d8b   db    d88b
888o  88    `8P'
88V8o 88     88
88 V8o88     88
88  V888 db. 88
VP   V8P Y8888P
{C.LIGHTBLACK_EX}by https://lolz.guru/members/2977610
'''
#удалил гей
print(bb)

def get_cookies():
    global c
    cookies = Path(easygui.diropenbox('Select logs floader')).glob('**/*.txt')
    print(C.GREEN+'Count files .txt:',C.MAGENTA+str(c))
    return cookies

def convert_cookie(i):
        cookieFile = q.get()
        try:
            cookie = open(cookieFile,'r+',encoding='utf8',errors='ignore').read()
            cookie = str(convert(cookie))
            open(cookieFile.replace('.txt','.json'),'w').write(cookie)
        except:pass
        q.task_done()
        bar.update(1,i)
def main():
    global bar
    cookies = get_cookies()
    print(C.CYAN,end='')
    bar =  click.progressbar(length=c,label='Convert cookies:')
    for cookieFile in cookies:q.put(cookieFile)
    for i,cookieFile in enumerate(cookies):sleep(0.1),Thread(target=convert_cookie,args=(i,),daemon=True).start()
    print(C.BLUE+'Wait...')
    q.join()






main()
input(C.RED+'Press enter.')

