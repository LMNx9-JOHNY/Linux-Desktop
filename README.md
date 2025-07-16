<h2 align="center">
⚡ LMNx9 Linux Desktop 💻
</h2>

<p align="center">
<img src="https://img.shields.io/badge/Platform-Termux%20Android-ff2d75?style=for-the-badge&logo=android&logoColor=white">
<img src="https://img.shields.io/badge/Desktop-XFCE4-blueviolet?style=for-the-badge&logo=gnu-linux&logoColor=white">
<img src="https://img.shields.io/badge/Maintained%20by-LMNx9-darkgreen?style=for-the-badge">
</p>

---

<h2 align="center">⚡ Run Full Linux Desktop on Your Android Device Easily! 💻</h2>

---

## 📥 Download x11 Apk

> 📱 **Choose Your Device And Install APK**

<div align="center">

[![64-BIT Download](https://img.shields.io/badge/Download-64bit-green?style=for-the-badge&logo=google-play)](https://github.com/LMNx9-JOHNY/Linux-Desktop/raw/refs/heads/main/x11-armv64.apk)  
[![32-BIT Download](https://img.shields.io/badge/Download-32bit-orange?style=for-the-badge&logo=google-play)](https://github.com/LMNx9-JOHNY/Linux-Desktop/raw/refs/heads/main/x11-armv32.apk)

</div>

---

## 🔧 Required Package Installation

```bash
pkg update && pkg upgrade
pkg install git python
pkg install x11-repo
pkg install termux-x11-nightly
pkg install proot-distro
proot-distro install debian
```

---

## 💻 Login & Upgrade Debian

```bash
proot-distro login debian
```
```bash
apt update && apt upgrade
apt install nano adduser
apt install sudo
sudo apt install dbus-x11
```

---

## 👑 Create Root User & Permissions

```bash
adduser lmnx9
```
```bash
nano /etc/sudoers
```


➡️ Add this under `#root` line and save:
```bash
lmnx9 ALL=(ALL:ALL) ALL
```

✅ Then login and check:

```bash
su - lmnx9
```
```bash
sudo whoami
whoami
```
---

## 🖥️ Install XFCE4 Desktop Environment

```bash
sudo apt install xfce4 -y
```

---

## ▶️ Run Desktop Tool (First Time)

### For 64-bit Devices

```bash
git clone https://github.com/LMNx9-JOHNY/Linux-Desktop
cd Linux-Desktop
chmod +x *
python lmnX64.py
```

### For 32-bit Devices

```bash
git clone https://github.com/LMNx9-JOHNY/Linux-Desktop
cd Linux-Desktop
chmod +x *
python lmnX32.py
```

---

## 🔁 Next Time to Run

```bash
proot-distro login debian
```
```bash
su - lmnx9
```
```bash
cd Linux-Desktop
chmod +x *
```

### For 64-bit:
```bash
python lmnX64.py
```

### For 32-bit:
```bash
python lmnX32.py
```

---

<h2 align="center">📡 Community & Contact</h2>

<p align="center">
  <a href="https://t.me/+w84Y7jIUzPFmYzg1">
    <img src="https://img.shields.io/badge/Join-Telegram%20Group-0088cc?style=for-the-badge&logo=telegram&logoColor=white">
  </a>
  <a href="https://t.me/x_LMNx9">
    <img src="https://img.shields.io/badge/Contact-Developer-blueviolet?style=for-the-badge&logo=telegram&logoColor=white">
  </a>
</p>

---

<h3 align="center">
Made With 🇧🇩 By <a href="https://github.com/LMNx9-JOHNY">LMNx9</a>
</h3>
