import os
timeout = 1
out_file = '/tmp/out.png'
width = 320
height = 240
img_buffer = open(
    os.path.join(
        os.path.split(__file__)[0], "app/images/cat.jpg"), 'rb').read()
