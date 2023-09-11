import wget
import os
import sys
from colorama import Fore, init
import tkinter

c = tkinter.Canvas()
def Notdone():
    init(convert=True)
    print(Fore.RED + '\nURL does not exist or process failed!')
def Done():
    init(convert=True)
    print(Fore.GREEN + '\nDONE!')
def openfile(a):
    init(convert=True)
    print(f'Starting to download Patch-{a.keysym}')
    if a.keysym == 'h' or a.keysym == 'p' or a.keysym == 's':
        if os.path.exists('Data\patch-{a.keysym}.MPQ'):
            os.remove('Data\patch-{keysym}.MPQ')
            remote_url = 'https://bradavice-online.cz/patches/patch-{a.keysym}.MPQ'
            local_file = 'Data\patch-{a.keysym}.MPQ'
            wget.download(remote_url, local_file)
            if os.path.exists('Data\patch-{a.keysym}.MPQ'):
                Done()
            else:
                NotDone()
    if a.keysym == 't' or a.keysym == 'm':
        if os.path.exists('Data\patch-{a.keysym}.mpq'):
            os.remove('Data\patch-{keysym}.mpq')
            remote_url = 'https://bradavice-online.cz/patches/patch-{a.keysym}.mpq'
            local_file = 'Data\patch-{a.keysym}.mpq'
            wget.download(remote_url, local_file)
            if os.path.exists('Data\patch-{a.keysym}.mpq'):
                Done()
            else:
                NotDone()
    
c.bind_all('<Key>', openfile)
