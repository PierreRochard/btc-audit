import os
from datetime import datetime

import bitcoin.rpc
now = datetime.utcnow().timestamp()
proxy_connection = bitcoin.rpc.Proxy(timeout=60000)

data = proxy_connection.call('dumpcoinstats',
                             os.path.expanduser(f'~/src/btc-audit/btc_audit_data_{now}.csv'))
