import os
from csv import DictWriter

import bitcoin.rpc

proxy_connection = bitcoin.rpc.Proxy()


def flatten_dict(dd, separator='_', prefix=''):
    return {prefix + separator + k if prefix else k: v
            for kk, vv in dd.items()
            for k, v in flatten_dict(vv, separator, kk).items()
            } if isinstance(dd, dict) else {prefix: dd}


height = 0

while True:
    data = proxy_connection.call('gettxoutsetinfo', 'none', height, True)
    print(data)
    data = flatten_dict(data)
    with open(os.path.expanduser('~/src/btc-audit/btc_audit_data_v2.csv'), 'a', newline='') as csvfile:
        writer = DictWriter(csvfile, fieldnames=data.keys())
        if height == 0:
            writer.writeheader()
        writer.writerow(data)
        height += 1
