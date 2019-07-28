import psutil

if __name__ == '__main__':
    """
    获取系统的进程列表psutil.pids()
    返回排序的进程ID列表，如果用来遍历进程，推荐使用psutil.process_iter
    """
    print('进程编号列表:', psutil.pids())
    print()

    """
    遍历进程信psutil.process_iter(attrs=None, ad_value=None)
    返回Process对象实列的迭代器
    attrs和ad_value在调用Process.as_dict()时具有相同的含义。用于指定要检索的进行的属性
    指定attrs，那么Process.as_dict()将会被内部调用，返回一个带有info属性的字典,否则将
    会检索进程的所有信息
    """
    print('获取进程信息示例1(基本用法)')
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        except psutil.NoSuchProcess:
            pass
        else:
            print(pinfo)
   
    print('获取进程信息示例2(指定attrs)')
     # 在调用时指定attrs，返回info字典，字典的key为每个属性名称
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        print(proc.info)
    
     # 使用词典解析，创建{pid: info, ...}的数据结构
    print('\n获取进程信息示例3(词典解析)')
    procs = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])}
    print(procs)
    
    # 根据进程名称过滤信息
    print('\n获取进行信息示例4(进程名过滤)')
    filter_list = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['name']]
    print(filter_list)
    
    """
    根据进程id判断进程是否存在psutil.pid_exists(pid)
    该方法比调用"pid in psutil.pids()" 要快，推荐用该方法判断进程是否存在
    """
    print('\n查看进程是否存在')
    print('查看pid=1的进程是否存在:', psutil.pid_exists(1))

    """
    等待进程结束psutil.wait_procs(procs, timeout=None, callback=None)
    等待procs指定的进程结束，返回一个(gone, alive)的元组表示哪些进程已经结束，哪些进程仍然存活
    已经结束的进程将会有一个表示退出状态的返回码。callback指定了一个在进程结束时被调用的回调函数
    函数的参数为Process示例对象。当procs中的进程全部结束，或者超时后，psutil.wait_procs()将会返回
    与Process.wait()不同，当等待超时时本函数不会触发TimeoutExpired异常。本方法的典型应用场景:
    向一系列进程发送SIGTERM信号
    给进程种植设置一些时间
    向存活状态的进程发哦是那个SIGKILL信号
    """
    def on_terminate(proc):
        print('process {} terminated with exit code {}'.format(proc, proc.returncode))

    procs = psutil.Process().children()
    for p in procs:
        p.terminate()
    gone, alive = psutil.wait_procs(procs, timeout=3, callback=on_terminate)
    for p in alive:
        p.kill()
