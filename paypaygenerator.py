import datetime, time, os, random, string, uuid
from colorama import init
from colorama import Fore
 
init(autoreset=True)
zandaka = 0

def randomname(n):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n)) 

def paypay_gen():
    global zandaka
    time.sleep(random.randint(7, 13))
    zandaka += random.randint(4, 30)
    print(f"{Fore.CYAN}[{datetime.datetime.now():%H:%M:%S}][success]PayPayリンクが生成されました 生成残高:"+str(zandaka)+"円")
    print(f"{Fore.LIGHTGREEN_EX}[{datetime.datetime.now():%H:%M:%S}][info]リンクの受け取り中...")
    time.sleep(1)
    print(f"{Fore.CYAN}[{datetime.datetime.now():%H:%M:%S}][success]受け取りが完了しました 生成SEED:"+randomname(20)+" 受け取りアカウントUUID:"+str(uuid.uuid1()))
    print("--------------------------------------")
    paypay_gen()

print(f"""{Fore.LIGHTMAGENTA_EX}
 ____             ____              ____                           _             
|  _ \ __ _ _   _|  _ \ __ _ _   _ / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |_) / _` | | | | |_) / _` | | | | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  __/ (_| | |_| |  __/ (_| | |_| | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
|_|   \__,_|\__, |_|   \__,_|\__, |\____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
            |___/            |___/                                                                                            
{Fore.RESET}""")
input("Enter License-Key: ")
print(f"{Fore.LIGHTGREEN_EX}[{datetime.datetime.now():%H:%M:%S}][info]HWIDを確認中...")
time.sleep(3)
print(f"{Fore.CYAN}[{datetime.datetime.now():%H:%M:%S}][success]HWIDの確認が完了し、Keyが認証されました")
time.sleep(2)
os.system('cls')
print(f"{Fore.LIGHTGREEN_EX}[{datetime.datetime.now():%H:%M:%S}][info]PayPayリンクをジェネレート中...")
paypay_gen()
