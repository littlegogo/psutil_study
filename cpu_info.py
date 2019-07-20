import psutil

if __name__ == '__main__':
    # 查看cpu数量 psutil.cpu_count(logical=True)
    # logic=True 返回逻辑cpu数量或None
    # logic=False 返回物理cpu的数量或None，不考虑超线程
    # 在OpenBSD和NetBSD总是返回None
    print('cpu数量(logical=True):', psutil.cpu_count(logical=True))
    print('cpu数量(logical=False):', psutil.cpu_count(logical=False))
    print('')    

    # 查看cpu利用率 psutil.cpu_percent(interval=None, percpu=False)
    # 以浮点数返回系统当前的cpu整体占用情况
    # interval > 0.0 对间隔起始和间隔结束的cpu时间进行比较
    # interval为0.0或None，cpu时间比较范围为上一次调用开始，立即返回，首次调用时立刻返回0
    # 为保证精确，至少设置间隔为0.1而不是立即调用
    # percpu=True将对每个cpu进行单独统计
    for i in range(5):
        print('cpu总体利用率:', psutil.cpu_percent(interval=1))
    for i in range(5):
        print('cpu利用详情:', psutil.cpu_percent(interval=1, percpu=True))
    print('')

    # 查看cpu时间 psutil.cpu_times(percpu=False)
    # 以命名元组的形式返回系统的cpu时间占用信息，返回的信息内容与平台有关
    # user   - 用户态占用时间
    # system - 内核态占用时间
    # idle   - 空闲时间
    # 当percpu=True时，返回每个cpu的时间占用情况
    print('cpu时间:', psutil.cpu_times(percpu=True))
    print('')
    
    # 查看cpu频率 psutil.cpu_freq(percpu=Fale)
    # 返回命名元组，频率数值单位MHz
    # 字段含义：
    # current - 当前频率
    # min     - 最小频率
    # max     - 最大频率
    # 在linux平台上current是实时值,其它平台基本是固定值
    # percpu=True 返回每个cpu的频率情况(需要系统支持)
    # 如果无法确定min和max那么设置为0
    print('cpu频率:', psutil.cpu_freq())
    if psutil.LINUX:
        print('cpu频率(percpu=True):', psutil.cpu_freq(percpu=True))
    else:
        print('查看每个cpu频率仅支持linux')
    print()

    # 查看cpu状态 psutil.cpu_status
    # 返回命名元组
    # 字段含义：
    # ctx_switches - 启动后上下文切换次数
    # interrupts   - 启动后中断触发次数
    # soft_interrtups - 启动后软中断触发次数
    # syscalls     - 启动后的系统调用次数(linux下为0)
    print('cpu状态:', psutil.cpu_stats())

