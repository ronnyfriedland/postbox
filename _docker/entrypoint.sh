#!/bin/bash

set -e

setsid /usr/bin/python3 /postbox/postbox_poller.py &
setsid /usr/bin/python3 /postbox/postbox_process_mail.py &
setsid /usr/bin/python3 /postbox/postbox_process_influxdb.py &

bash
