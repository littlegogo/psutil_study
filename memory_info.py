import psutil

if __name__ == '__main__':
    """
    查看内存信息 psutil.virtual_memory()
    返回内存使用的统计信息,数值单位为bytes
    字段含义：
    total              - 物理内存总容量
    available          - 不需要进行内存交换(swap)，可直接分配给进程的内存容量。跨平台监控可用物理内存容量时使用该字段
    used               - 已用内存(仅供参考) total-free不一定等于used
    free               - 没有被使用的内存，不代表实际可用内存，实际可用内存参考available, total-used不一定等于free
    active(UNIX)       - 使用中或最近使用的内存
    inactive(UNIX)     - 被标记为未被使用的内存
    buffers(Linux BSD) - 一般用于文件系统等元数据的缓存
    cached(Linux BSD)  - 当做各种情况下的缓存
    shared(Linux BSD)  - 可被多个进程同时访问的内存
    slab(Linux)        - 内核数据结构缓存
    wired(BSD macOS)   - 被标记为永远驻留在RAM中的内存，不会被交换到磁盘
    说明: used + availiable 不是必须等于total；在Windows上aviable和free相等
    """
    print('内存信息', psutil.virtual_memory())
    print()

    """
    查看内存交换信息 psutil.swap_memory()
    返回内存交换情况的统计信息
    字段含义:
    total   - 以bytes表示的交换内存总容量
    used    - 以bytes表示的已使用的交换内存总容量
    free    - 以bytes表示的空间交换内存容量
    percent - 交换内存使用率
    sin     - 以bytes表示的从磁盘交换到内存的容量(累积的)，Windows上为0    
    sout    - 以bytes表示的从内存交换到磁盘的容量(累积的)，Windows上为0
    """
    print('内存交换信息:', psutil.swap_memory())
    print()


