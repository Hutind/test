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
    pid = os.fork()#获取进程id
    if pid >0:#如果为非子进程
        sys.exit() #父程序退出
        
    os.setsid()#进程成为新的会话组长和进程组长
    os.umask(0)#获得对写的对象完全控制
    
    pid =os.fork()#再次获得id
    if pid >0:
        sys.exit(0)
        
    f=open('text.txt','w')#打开文件
    a=1
    while True:#死循环
        a=a+1
        f.write(str(a))
    f.close()#关闭
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
import time
c=1

def funt(no,a):
    global c
    while True:
        time.sleep(1)
        c=c+1
        print 'thread no %d , =%d,'%(no,a)
def teste():
    thread.start_new_thread(func,(1,2))
    thread.start_new_thread(func,(2,2))
    time.sleep(20)
if __name__=='__main__':
    teste()
~~~

多线程threading：

~~~python
import threading
import time

exitflage = 0
class mythread (threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        print "start "+self.name
        print_time(self.name,self.counter,5)
        print "exiting" +self.name
    
def print_time(threadName,delay,counter):
    while counter:
        if exitflage:
            threading.Thread.exit()
        time.sleep(delay)
        print "%s : %s" %(threadName,time.ctime(time.time()))
        counter -= 1
thread1 =mythread(1,"Thread-1",1)
thread2 =mythread(2,"Thread-2",2)
thread1.start()
thread2.start()
print "exiting main thread"
~~~

锁机制(线程同步)：

~~~python
import threading
import time

class mythreading (threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID= threadID
        self.name= name
        self.counter=counter
    def run(self):
        print "starting" +self.name
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()
        
def print_time(threadName,delay,counter):
    while True:
        time.sleep(delay)
        print "%s : %s" %(threadName，time.ctime(time.time()))
        counter -=1
        
threadLock =threading.lock()
threads =[]

thread1 = mythread(1,"thread-1",1)
thread2 = mythread(2,"thread-2",2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print "Exiting Main Thread"
~~~

