# LMNx9 Linux Desktop
Run Linux Desktop On Your Android Device Easily


### Required Packages installation :
    pkg update && pkg upgrade;pkg install git python;pkg install x11-repo;pkg install termux-x11-nightly;pkg install proot-distro;proot-distro install debian
### Login Debian :
    proot-distro login debian
### Upgrade Debian :
    apt update;apt upgrade;apt install nano adduser;apt install sudo;sudo apt install dbus-x11
### User ROOT Access :
    adduser lmnx9
### Set All Permission Manually :
    nano /etc/sudoers
### Add Under #root & Save :
    lmnx9 ALL=(ALL:ALL) ALL
### Login ROOT & Check :
    su - lmnx9
    sudo whoami 
    whoami
### Install XFCE4 Terminal :
    sudo apt install xfce4 -y

## Run Tool For Desktop >>>
### For 64bit Device :
    git clone https://github.com/LMNx9-JOHNY/Linux-Desktop
    cd Linux-Desktop
    chmod +x *
    python lmnX64.py
### For 32bit Device :
    git clone https://github.com/LMNx9-JOHNY/Linux-Desktop
    cd Linux-Desktop
    chmod +x *
    python lmnX32.py

## Next Time If Need Run >>>
### Finally Run :
    proot-distro login debian 
    sudo - lmnx9
    cd Linux-Desktop
    chmod +x *
### For 64bit :
    python lmnX64.py 
### For 32bit :
    python lmnX32.py







