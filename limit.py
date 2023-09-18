from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep, time
from colorama import Fore,Style, init as color_ama
color_ama(autoreset=True)
import json, re, sys, os, random

banner = Style.BRIGHT+Fore.YELLOW +  """

   ____               _   
  / ___| ___ __ _ ___| |_ 
 | |  _ / __/ _` / __| __|
 | |_| | (_| (_| \__ \ |_ 
  \____|\___\__,_|___/\__|
                          
  Creator : MK KHAIRIL || Youtube : MK KHAIRIL
  Support : Cocentz404 || Youtube : Cocentz404"""

putih = Style.BRIGHT+Fore.WHITE
hijau = Style.BRIGHT+Fore.GREEN
merah = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
reset = Fore.RESET
biru = Style.BRIGHT+Fore.BLUE


os.system('clear') 
print(banner)
print("\n")
print(f'{hijau}[+] Indonesia/English')
import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.2)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik("[+] Ini Adalah Program Ilegal\n[+] Semua Resiko Harap Ditanggung Pengguna..!!\n[+] This Is An Illegal Program\n[+] All Risks Borne by Users...!\n")
if not os.path.exists('session'):
    os.makedirs('session')
if len(sys.argv) < 2:
    print( Fore.RED + '\n\nUsage : python main.py +62' + Fore.RESET)
    sys.exit(1)
api_id = 1148490
api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
phone_number = sys.argv[1]
client = TelegramClient('session/' + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input(Fore.WHITE + 'Enter Yout Code Code : '))
    except SessionPasswordNeededError:
        passw = input(Fore.RESET + 'Your 2fa Password : ')
        me = client.start(phone_number, passw)
saia = client.get_me()
print('[*]Account:',saia.first_name)
print('[*]Phone:',saia.phone,'\n')
channel_username = '@gcastod'
channel_entity = client.get_entity('@gcastod')
print('Memulai Bot Gcast..!')


while True:
  try:
    
    client.send_message(entity=channel_entity, message='.limit')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(10)
    client.send_message(entity=channel_entity, message='.limit')
    print(f'{hijau} Gcast berhasil.! {putih}gcast by : khairil')
    sleep(360)
    
  except:
    print(f'{hijau} Gcast gagal.! {putih} gcast by : khairil')
    sleep(30)

sys.exit()
client.disconnect()
