import subprocess
import time
from slow_motion import settings
from slow_motion import app

import threading

cmd = 'raspistill -w %s -h %s -o %s -ex night -rot 180' % (
    settings.width,
    settings.height,
    settings.out_file)


def proc():
    while 1:
        res = subprocess.run(cmd.split())
        print("res:%s" % (res, ))
        time.sleep(settings.timeout)


threading.Thread(target=proc).start()
app.main()
