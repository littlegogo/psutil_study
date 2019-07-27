import psutil

if __name__ == '__main__':
    """
    查看网络I./O统计信息 psutil.net_io_counters(pernic=False, nowrap=True)
    返回系统级别的网络I/O统计信息
    字段含义：
      bytes_sent   - 发送字节数
      bytes_recv   - 接收字节数
      packets_sent - 发送packet数量
      packets_recv - 接收packet数量
      errin        - 接收错误数
      errout       - 发送错误数
      dropin       - 接收丢包数
      dropout      - 发送丢包数(在 macOS 和 BSD上总是0)
    
     pernic ＝True 以词典形式返回每个网卡的上述信息，网卡的名称作为key
     在Linux，网络非常繁忙或者运行时间很长的系统中，返回的数值可能发生溢出或wrap(数值从0重新开始计数) 
     如果指定nowrap＝True， psutil 将会在每次函数调用时进行检测和调整，将旧的值与新的值相加或保持不变，
     从而不会减少 使用net_io_counters.cache_clear()方法可以清除nowrap的缓存值. 
     
     在没有网络接口(网卡)的机器上，如果指定pernic＝True，函数将返回None or {}     
    """
    print('网络I/O信息(pernic=False):', psutil.net_io_counters())
    print()
    print('网络I/O信息(pernic=True):', psutil.net_io_counters(pernic=True))
    print()

    """
    查看网络连接情况psutil.net_connections(kind='inet')
    返回系统的socket连接信息
    字段含义:
      fd     - socket描述符（在windows和SunOS上为-1）
      family - 地址族AF_INET, AF_INET6或AF_UNIX
      type   - 地址类型SOCK_STREAM, SOCK_DGRAM orSOCK_SEQPACKET
      laddr  - 本地地址（ip,port）或AF _UNIX路径
      raddr  - 远端地址（ip,port）或UNIX sockets绝对路径 ，当远端未连接时，（返回FA_INET*) 或AF_UNIX
      satus-TCP连接状态 psutil.CONN_*形式的字符串常量。对于UDP和Unix sosket，这个值始终为psutil.CONN_NONE
      pid-开启socket的进程的进程ID（pid）在一些平台上（如linux），该字段是否可用与进程的权限有关(通常来说需要root权限)
    
     函数中的kind参数取值为字符串，可以设置的内容及说明如下：
      Kind value	Connections using
       "inet"	        IPv4 and IPv6
       "inet4"	        IPv4
       "inet6"	        IPv6
       "tcp"	        TCP
       "tcp4"	        TCP over IPv4
       "tcp6"	        TCP over IPv6
       "udp"	        UDP
       "udp4"	        UDP over IPv4
       "udp6"	        UDP over IPv6
       "unix"	        UNIX socket (both UDP and TCP protocols)
       "all"	        the sum of all the possible families and protocols 
	
      注意:
          在macOS和AIX系统上，这个函数需要系统权限，为了得到每个进程的网络连接情况可以使用Process.connections()函数
          在macOS和AIX系统上，如果不是用root运行，将会触发psutil.AccessDenied异常。
          在Solaris，UNIX sockets不被支持
          在Linux, FreeBSD系统上针对UNIX socket，“raddr”字段将被设置为”This is a limitation of the OS.”
          在OpenBSD系统上针对UNIX socket“laddr” 和“raddr” 字段 将被设置为”This is a limitation of the OS.”     
    """
    print('网络连接信息:', psutil.net_connections())
    print()
    
    """
    查看网卡状态psutil.net_if_stats()
    返回每块网卡的状态信息
    字段含义:
       isup   - 网卡是否启动并运行
       duplex - NIC_DUPLEX_FULL(全双工) NIC_DUPLEX_HALF(半双工) NIC_DUPLEX_UNKNOWN(未知)
       speed  - 网络速度(MB)，如果不能获取则被设置为0
       mtu    - 以bytes表示的最大传输单元
    """
    print('网卡状态:', psutil.net_if_stats())

