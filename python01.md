父子进程演示：
~~~python
import os
import time
import signal

def onsinganal_term(a,b):
    print'over'
    signal.signal(signal.SIGTERM,onsinganal_term)
def myfork();
	r,w=os.pipe()
	a=1
	Pid=os.fork()
	If pid ==0:
        os.close(r)
        w=os.fdopen(w,'w')
		Print "child %d--%d--%d"(pid,os.getpid(),os.getppid())
        #time.sleep(1)
		#Print a+1
        while	True:
            a=a+1
            if a>100:
                os.kill(os.getppid,dignal.SIGTERM)
            w.write(str(a))
         w.close()
	Else:
        os.close(w)
        r=os.fdopen(r)
        print r.read()
        r.close()
		Status=os.waitpid(pid,0)   #等子进程执行后再..
		Print"parent %d--%d--%d" %(pid,os.getpid(),os.getppid())
        #time.sleep(2)
		#Print a+3
        #time.sleep(4)
If __name__=='__main__':
	Myfork()
~~~

守护进程案例：

~~~python
import os
import sys
def damen_test():
    pid = os.fork()
    if pid >0:
        sys.exit()
        
    os.setsid()
    os.umask(0)
    
    pid =os.fork()
    if pid >0:
        sys.exit(0)
        
    f=open('text.txt','w')
    a=1
    while True:
        a=a+1
        f.write(str(a))
    f.close()
if __name__=='__mian__':
    daemon_test()
~~~

结束进程（linux）：

~~~shell
ps -ef |grep daemon
kill [id]
ls -lh
~~~

多线程函数式：

~~~python
import Thread

c=1

def funt(no,a):
    global c
    while True:
        c=c+1
        print 'thread no %d , =%d,'%(no,a)
def test():
    thread.start_new_thread(func,(1,2))
    thread.start_new_thread(func,(2,2))
if __name__=='__main__':
    test()
~~~

