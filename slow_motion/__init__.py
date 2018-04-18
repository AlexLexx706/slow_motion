import subprocess
import time
from slow_motion import settings
from slow_motion import app
import sys
import threading

cmd = 'raspistill -w %s -h %s -o %s -ex night -rot 180' % (
    settings.width,
    settings.height,
    settings.out_file)


def proc():
    if sys.platform == 'win32':
        return

    while 1:
        res = subprocess.run(cmd.split())
        print("res:%s" % (res, ))
        time.sleep(settings.timeout)


def main():
    threading.Thread(target=proc).start()
    app.main()


if __name__ == "__main__":
    main()
