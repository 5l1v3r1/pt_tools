# pt_tools
本脚本程序仅为学习交流分享，请遵守《中华人民共和国网络安全法》,勿用于非授权测试,如作他用所承受的法律责任一概与作者无关。  
测试平台为linux
***
  
### dirscan 更名为 ”nfuzz“ 并移动到 [n00B-tot / nfuzz](https://github.com/n00B-ToT/nfuzz)
  
***
moniter.py 是个netcat监控脚本（写完后觉得有点鸡肋）  
  
主要用处为：在目标机器上写入 后门（需要管理员上线才能触发的后门）后（例如替换ls命令为反向连接shell等）  
  
监听netcat程序交互，若有shell连进则发送邮件提醒  
  
可改造成后用作简易蜜罐
  
用法：./moniter.py 4444
```
./moniter.py
[!]Usage: ./moniter.py [PORT] 
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
