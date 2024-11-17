# T9Plus-ledoff
Turn Off LED light for T9Plus mini PC (N100 cpu)

There is an official utility for Windows to customize the backlighting on miniPC, but not for Linux, so this is it =)

# Requirements
You need python 3 installed
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3
```

# Autostart
Script Turn Off LED light on T9Plus mini PC, but LED turn ON every miniPC turn ON, so you can add script to autostart:
## Save script
Create script file for example in /etc
- `sudo nano /etc/t9plus-ledoff.py`
- paste code
- save file (ctrl + x, y)

OR copy downloaded file to the same folder /etc
- `cp ~/Documents/t9plus-ledoff.py /etc/t9plus-ledoff.py`

## Configure autostart
There are many options for autostarting scripts on Linux systems, this is one option that runs the script immediately after booting (before user login)
Create script file in /etc/rc.local
- `sudo nano /etc/rc.local`
- Add line `python3 /etc/t9plus-ledoff.py`
- save file (ctrl + x, y)

# Problems
There is one problem with the highlighting not related to the script
The LED controller automatically turns it ON when the system goes into sleep mode, so you need to turn OFF sleep mode to prevent turning on LED light at night =)

PS Reboot don't turn ON LED light, only sleep mode