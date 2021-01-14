import os
import signal
import subprocess

import pytest

@pytest.fixture(scope='module', autouse=True)
def record_video():
    cmd = 'scrcpy --record video.mp4'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield
    os.kill(p.pid, signal.SIGTERM)  # 这个是Mac的杀进程
    # os.kill(p.pid, signal.CTRL_C_EVENT)  #这个是Windows的杀进程
