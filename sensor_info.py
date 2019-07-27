import psutil

if __name__ == '__main__':
    """
    查看温度传感器信息psutil.sensors_temperatures(fahrenheit=False)
    返回硬件的温度传感器信息(可能是CPU，disk等，与操作系统有关)
    fahrenheit=False表示数值单位为：摄氏度
    fahrenheit=True 表示数值单位为：华氏度
    如果传感器不被支持，返回空的字典
    在Linux和FreeBSD系统可用
   """
    print('传感器温度信息:', psutil.sensors_temperatures())
    print()

    """
    查看风扇转速psutil.sensors_fans()
    转速单位：RPM
    支持Linux和macOS系统 
    """
    print('风扇转速:',psutil.sensors_fans())
    print()
    
    """
    查看系统电池信息psutil.sensors_battery()
    返回电池的状态信息，如果没有电池返回None
    字段含义:
      percent       - 剩余电量
      secsleft      - 电量剩余秒数，如果接通电源，被设置为psutil.POWER_TIME_UNLIMITED，如果不能确定则被设置为psutil.POWER_TIME_UNKNOWN
      power_plugged - 是否连接电源适配器,如果不能确定则返回None
    支持系统：Linux Windows FreeBSD
     """
    print('电池信息:', psutil.sensors_battery())

