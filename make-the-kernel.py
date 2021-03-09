import os
print(
    "welcome,this program will install linux5.11.4+xanmod+uksm+cacule to your computer by it self(it's danger)"
)
print("Please make shure your terminal has 80x80 char")
sysname = input("what\'s your system?(\"debian\"or\"arch\"):  ")
print("installing build tools\n")
if sysname == "debian":
    os.system("sudo apt install tar build-essential make gcc aria2")
elif sysname == "arch":
    os.system("sudo pacman -S tar make base-devel gcc aria2")
cpucore = input("how many cpu core are in your cpu(enter a number): ")
os.system("mkdir src")
os.chdir("src")
os.system(
    "aria2c --split=100 https://hub.fastgit.org/xanmod/linux/archive/5.11.4-xanmod1-cacule.tar.gz"
)
os.system("tar -zxvf  linux-5.11.4-xanmod1-cacule.tar.gz")
os.chdir("linux-5.11.4-xanmod1-cacule")
os.system("pwd")
os.system(
    "aria2c --split=100 https://raw.github.com/dolohow/uksm/master/v5.x/uksm-5.11.patch"
)
os.system("patch -p1 < uksm-5.11.patch")
os.system("sudo make menuconfig")
os.system("sudo make -j" + cpucore)
os.system("sudo make modules_install -j" + cpucore)
print("already maked")
shure = input(
    "WARNING IT'S DANGER!: are you shure to install the new kernel to your computer?"
)
if shure == "y":
    os.system("sudo make install")
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
    os.system("make clean")
    print("all finished,please REBOOT")
else:
    os.system("make claen")
    exit(1)
