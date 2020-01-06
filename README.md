# pt_tools
本脚本程序仅为学习交流分享，请遵守《中华人民共和国网络安全法》,勿用于非授权测试,如作他用所承受的法律责任一概与作者无关。  
测试平台为linux
***

dirscan.py 是个 web目录扫描器  

缺点：没有自定义报错，看起来有点蠢

用法：./dirscan.py -w /usr/share/wordlists/wfuzz/general/common.txt -u xxxxxxxxxxxx.com -t 5

-t 线程数（默认5） -w 字典 （必须）-u （必须）
```
./dirscan.py -h
usage: dirscan.py [-h] [-t THREAD_NUM] [-u URLS] [-w WORDLISTS]
optional arguments:
-h, --help     show this help message and exit
-t THREAD_NUM  thread options
-u URLS        url options
-w WORDLISTS   wordlists options
```
***

ssh_brute.py 是个 ssh爆破脚本  

缺点：单线程，速度慢，且无法指定端口

用法：./ssh_brute.py xx.xx.xx.xx root /usr/share/wordlists/wfuzz/others/common_pass.txt

```
./ssh_brute.py
[!]Usage: ./ssh_brute.py [HOST] [USERNAME] [DICT]
```
***

DOS.java是DOS攻击demo  
并非DDOS  
经测试可以DOS自己导致死机👍非常牛逼
