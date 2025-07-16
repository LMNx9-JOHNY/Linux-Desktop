'''
</> CODED BY - DARK LMNx9 
</> TELEGRAM - t.me/x_LMNx9
'''
import os,time,signal,subprocess

try:
    pgrep = subprocess.check_output(["pgrep", "-f", "termux.x11"]).decode().strip().split("\n")
    for pid in pgrep:
        try:
            os.kill(int(pid), signal.SIGKILL)
        except ProcessLookupError:
            pass
except subprocess.CalledProcessError:
    pass

subprocess.Popen([
    "pulseaudio", "--start",
    '--load=module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1',
    "--exit-idle-time=-1"
])

os.environ["XDG_RUNTIME_DIR"] = os.environ.get("TMPDIR", "/data/data/com.termux/files/usr/tmp")
subprocess.Popen(["termux-x11", ":0"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

time.sleep(3)

subprocess.call([
    "am", "start", "--user", "0",
    "-n", "com.termux.x11/com.termux.x11.MainActivity"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)

os.environ["PULSE_SERVER"] = "127.0.0.1"

subprocess.Popen([
    "env", "DISPLAY=:0", "dbus-launch", "--exit-with-session", "xfce4-session"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

exit(0)
