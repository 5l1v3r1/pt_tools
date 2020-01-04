# pt_tools
本脚本程序仅为学习交流分享，请遵守《中华人民共和国网络安全法》,勿用于非授权测试,如作他用所承受的法律责任一概与作者无关。

这是个web目录扫描器

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

