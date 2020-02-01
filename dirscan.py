#! /usr/bin/python3
#author : n00B & khan Team

import threading, argparse , requests , sys
from queue import Queue
#import pdb

GREEN = "\033[32m"
YELLOW = "\033[93m" 
cyan = "\033[0;36m"
none = "\033[0m"
red = "\033[0;31m"

class DirScan:
    def __init__(self , args):
        self.urls = args.urls
        self.thread_num = args.thread_num
        self.wordlists = args.wordlists 

    

    class n00b_DirScan(threading.Thread):
        def __init__(self, queue , total):
            threading.Thread.__init__(self)
            self._queue = queue
            self._total = total

        

        def run(self):
            while not self._queue.empty():
                urls = self._queue.get()
                try:
                    resp = requests.head(urls)
                    #sys.stdout.write('success')
                    if resp.status_code == 200 :
                        sys.stdout.write('\r' + '[*]-----%s\t\t'%urls + "------------"+ GREEN+"200" + none + "\n")
                    elif resp.status_code == 403 :
                        sys.stdout.write('\r' + '[*]-----%s\t\t'%urls + "------------"+ YELLOW+"403" + none + "\n")
                    elif resp.status_code == 302 :
                        sys.stdout.write('\r' + '[*]-----%s\t\t'%urls + "------------"+ cyan+"302" + none + "\n")
                    elif resp.status_code ==500 :
                        sys.stdout.write('\r' + '[*]-----%s\t\t'%urls + "------------"+ red +"500" + none + "\n")
                except Exception as e:
                    print(e)
                    pass

    def start(self):
        queue = Queue()
        f = open(self.wordlists,'r')
        for i in f.readlines():
            queue.put(self.urls + '/' + i.strip('\n'))
        total = queue.qsize()
        threads = []
        #pdb.set_trace()
        thread_count = int(self.thread_num)
        
        for i in range(thread_count):
            threads.append(self.n00b_DirScan(queue,total))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t',dest='thread_num',type=int,help="thread options",default=5)
    parser.add_argument('-u',dest='urls',type=str,help="url options")
    parser.add_argument('-w',dest='wordlists',type=str,help="wordlists options")
    args = parser.parse_args()
    if args.urls and args.wordlists:
        dirscan = DirScan(args)
        dirscan.start()
        sys.exit(1)
    else:
        txt = '''
        -w Please enter the WORDLIST file address
        -t Please enter the THREAD number
        -u Please enter the URL number
        '''
        print(txt)
        sys.exit(1)

if __name__ == '__main__':
    main()
