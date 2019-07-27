import psutil
import datetime


if __name__ == '__main__':
    """
    查看系统的启动时间psutil.boot_time()
    返回系统的启动时间，UINX时间戳
    """
    print('系统启动时间:', datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
    print()

    """
    查看系统用户信息psutil.users()
    返回当前已经连接到系统的用户列表
    字段含义：
      user - 用户名
      terminal - 终端
      host - 主机名
      started - 起始时间(unix 时间戳，秒)
      pid - 登录进程(sshd,tmux,gdm-session-worker)的进程ID,在Windows和OpenBSD系统上，该字段被设置为None
    """
    print('用户信息:',psutil.users())
    print()
   
