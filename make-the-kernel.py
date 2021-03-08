import os
print(
    "welcome,this program will install linux5.11.4+xanmod+uksm+cacule to your computer by it self(it's danger)"
)
print()
sysname = input("what\'s your system?(\"debian\"or\"arch\"):  ")
print("installing git and wget\n")
if sysname == "debian":
    os.system("sudo apt install git wget build-essential make gcc")
elif sysname == "arch":
    os.system("sudo pacman -S git wget make base-devel gcc")
cpucore = input("how many cpu core are in your cpu(enter a number): ")
os.system("mkdir make-the-kernel")
os.chdir("make-the-kernel")
os.system("git clone -b 5.11 https://hub.fastgit.org/xanmod/linux")
os.chdir("linux")
os.system(
    "wget https://raw.github.com/hamadmarri/cacule-cpu-scheduler/master/patches/CacULE/v5.11/cacule-5.11.patch"
)
os.system(
    "wget https://raw.github.com/dolohow/uksm/master/v5.x/uksm-5.11.patch")
os.system("patch -p1 < uksm-5.11.patch")
os.system("patch -p1 < cacule-5.11.patch")
os.system("make menuconfig")
os.system("make -j" + cpucore)
os.system("make modules_install -j" + cpucore)
print("already maked")
shure = input(
    "WARNING IT'S DANGER!: are you shure to install the new kernel to your computer?"
)
if shure == "y":
    os.system("sudo make install")
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
    print("all finished,please REBOOT")
else:
    exit(1)
