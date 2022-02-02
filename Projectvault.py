import pickle
sudo=str(input('''enter your path  
O===(ZZZZZZZ>'''))
vault=open(sudo+'\protect.bat','wb')
print('''
 ██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗
 ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝
 ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░
 ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░
 ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░
 ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░


   ██╗░░░██╗░█████╗░██╗░░░██╗██╗░░░░░████████╗
   ██║░░░██║██╔══██╗██║░░░██║██║░░░░░╚══██╔══╝
   ╚██╗░██╔╝███████║██║░░░██║██║░░░░░░░░██║░░░
   ░╚████╔╝░██╔══██║██║░░░██║██║░░░░░░░░██║░░░
   ░░╚██╔╝░░██║░░██║╚██████╔╝███████╗░░░██║░░░
   ░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝░░░╚═╝░░░
   ''')
code='''
@ECHO OFF
if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK
if NOT EXIST Private goto MDPrivate
:CONFIRM
echo Are you sure to lock this folder? (Y/N)
set/p "cho=>"
if %cho%==Y goto LOCK
if %cho%==y goto LOCK
if %cho%==n goto END
if %cho%==N goto END
echo Invalid choice.
goto CONFIRM
:LOCK
ren Private "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo Folder locked
goto End
:UNLOCK
echo Enter password to Unlock Your Secure Folder
set/p "pass=>"
if NOT %pass%== '''
panda=str(input('''enter the password you will like to have
O===(ZZZZZZZ>'''))
code2=''' goto FAIL
attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Private
echo Folder Unlocked successfully
goto End
:FAIL
echo Invalid password
goto end
:MDPrivate
md Private
echo Private created successfully
goto End
:End'''
maincode=(code+panda+code2)
pickle.dump(maincode,vault)
vault.close()
with open(sudo+'\protect.bat', 'r') as fin:
    data = fin.read().splitlines(True)
with open(sudo+'\protect.bat', 'w') as fout:
    fout.writelines(data[1:])
print ('''
                     █████████
  ███████          ███        ███
  █      █      ███             ███
   █      █    ██                  ██
    █     █   ██     ██      ██     ███
     █   █   █      ████    ████     ██
   █████████████                      ██
   █            █         █           ██
 ██             █   ██          ██    ██
██   ███████████     ██        ██     ██
█               █      ████████       ██
██              █                    ██
 █   ███████████                   ██
 ██          ████                 █
  ████████████   █████████████████
  
''') 
