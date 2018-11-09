import datetime
from pprint import pprint

import psutil

_ONE_GIGABYTES_ = 1073741824


def net_traffic():
    sent = {}
    receive = {}
    network_counters = psutil.net_io_counters(pernic=True)
    network_keys = network_counters.keys()
    for key in network_keys:
        sent[key] = (network_counters.get(key).bytes_sent) / 1024
        receive[key] = (network_counters.get(key).bytes_recv) / 1024
    return sent, receive


def net_stat():
    data = psutil.net_connections()
    return data


def top():
    data = psutil.test()
    return data


def disk_io():
    data = psutil.disk_io_counters()
    return data


def memory():
    base_data = psutil.virtual_memory()
    print(type(base_data))
    data = {}
    data['total'] = base_data.total
    data['available'] = base_data.available
    data['percent'] = base_data.percent
    data['used'] = base_data.used
    data['time'] = datetime.datetime.now().strftime('%Y/%m/%d %H:%m')
    return data


if __name__ == '__main__':
    pprint(net_stat())
    # print(top())
    # print(disk_io())
    print(memory())
