'''
</> CODED BY - DARK LMNx9 
</> TELEGRAM - t.me/x_LMNx9
'''
import os,time,signal,subprocess

try:
    output = subprocess.check_output("pgrep -f termux.x11", shell=True).decode().strip().split("\n")
    for pid in output:
        os.kill(int(pid), signal.SIGKILL)
except subprocess.CalledProcessError:
    pass

subprocess.call(
    'pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1',
    shell=True
)

os.environ["XDG_RUNTIME_DIR"] = os.getenv("TMPDIR", "/data/data/com.termux/files/usr/tmp")
subprocess.Popen(
    'termux-x11 :0 -legacy-drawing >/dev/null &',
    shell=True
)

time.sleep(3)

subprocess.call(
    'am start --user 0 -n com.termux.x11/com.termux.x11.MainActivity > /dev/null 2>&1',
    shell=True
)
time.sleep(1)

os.environ["PULSE_SERVER"] = "127.0.0.1"

subprocess.Popen(
    'env DISPLAY=:0 dbus-launch --exit-with-session xfce4-session & > /dev/null 2>&1',
    shell=True
)

exit(0)
