import psutil

if __name__ == '__main__':
    """
    查看磁盘分区信息 psutil.dis_partitions(all=False)
    返回磁盘分区信息，包括：设备，挂载点，文件系统类型
    all=False 仅返回物理设备信息，如：disk cd-rom USB，忽略其它分区(如dev/shm)
    all 参数与平台有关，在BSD上会忽略all参数的取值
    返回的字段包括：
    device     - 设备
    mountpoint - 挂载点
    fstype     - 文件系统类型
    opts       - 其它选项
    文件系统类型fstype字段取值随操作系统而定
   """
    print('磁盘分区信息:', psutil.disk_partitions())
   # print('磁盘分区信息(all=True):', psutil.disk_partitions(all=True))
    print()
    
    """
    查看每个磁盘分区的占用情况 psutil.disk_useage(path)
    返回对应分区的统计信息
    返回字段包括：
    total - 分区总容量(bytes)
    used  - 分区已用容量(bytes)
    free  - 分区空闲容量(bytes)
    percentage - 分区使用百分比
    """
    for partition in psutil.disk_partitions():
        print('分区使用情况({}): '.format(partition.mountpoint), psutil.disk_usage(partition.mountpoint))
    print()
    
    """
    统计磁盘I/O计数器信息 psutil.disk_io_counters(perdisk=False, nowrap=True)
    返回磁盘计数器统计信息
    perdisk=True 返回每个物理磁盘的信息
    nowrap=True 防止长时间运行系统中返回结果的数值溢出，通过disk_io_counters.cache_clear()可使nowrap=True无效
    在windows上，需要先执行"diskperf -y”，否则该函数将找不到任何磁盘
    """
    print('磁盘计数器信息:', psutil.disk_io_counters())
    print()
    print('磁盘计数器信息(perdisk=True):', psutil.disk_io_counters(perdisk=True))
 
