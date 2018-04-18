import subprocess
import time

timeout = 1
out_file = '/tmp/out.jpg'
width = 640
height = 640
cmd = 'raspistill -w %s -h %s -o %s -ex night -rot 180' % (
    width, height, out_file)

while 1:
    res = subprocess.run(cmd.split())
    print("res:%s" % (res, ))
    time.sleep(timeout)
