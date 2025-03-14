import easygui, os
'''
NordVPN GUI Interface (For Linux)

Written by A.I.
'''
print("Minimize this console.")

def globaltitle(): global title, version
version = '2.0.1'
title = f'NordVPN - v{version}'

globaltitle()

def msg(x): easygui.msgbox(x, title)

def nordvpngui():
    status = os.popen("nordvpn status").read() 
    optionVar = easygui.buttonbox(f'{status}', title, ('Refresh', 'Connect (Fastest)', 'Connect (Select)', 'Disconnect', 'Settings'))

    if optionVar == None: exit()
    elif optionVar == "Refresh": nordvpngui()
    elif optionVar == "Connect (Fastest)":
        coutput = str(os.popen("nordvpn connect").read()).split()
        loopcounter=0
        for i in coutput:
            if i == "You": coutput = coutput[loopcounter:]; break
            loopcounter+=1
        msg(str(' '.join([str(elem) for elem in coutput])))
        nordvpngui()

    elif optionVar == "Disconnect":
        doutput = str(os.popen("nordvpn disconnect").read()).split()
        loopcounter=0
        for i in doutput:
            if i == "You": doutput = doutput[loopcounter:]; break
            loopcounter+=1
        loopcounter=0
        for i in doutput:
            if i == "How": doutput = doutput[:loopcounter]; break
            loopcounter+=1
        msg(str(' '.join([str(elem) for elem in doutput])))
        nordvpngui()

    elif optionVar == "Connect (Select)":
        countries = str(os.popen("nordvpn countries").read()).split()
        remove_these = {'-'}
        countries = [ele for ele in countries if ele not in remove_these]
        countries.sort()
        countryVar = easygui.choicebox('Select a country:', title, (countries))
        if countryVar == None: nordvpngui()
        command = "nordvpn cities "+countryVar

        cities = str(os.popen(command).read()).split()
        remove_these = {'-'}
        cities = [ele for ele in cities if ele not in remove_these]        
        cities.sort()
        cities.insert(0,'(Choose Fastest)')
        
        cityVar = easygui.choicebox(f'Select a city: ({countryVar})', title, (cities))
        if cityVar == None: nordvpngui()
        if cityVar == '(Choose Fastest)':
            command1 = "nordvpn connect "+countryVar
        else:
            command1 = "nordvpn connect "+cityVar
        coutput = str(os.popen(command1).read()).split()
        loopcounter=0
        for i in coutput:
            if i == "You": coutput = coutput[loopcounter:]; break
            loopcounter+=1
        msg(str(' '.join([str(elem) for elem in coutput])))
        nordvpngui()

    elif optionVar == "Settings":
        settings = os.popen("nordvpn settings").read()
        settings = str(settings.replace(': ', ':'))
        settings = str(settings.replace('Kill Switch', 'Killswitch'))
        settings = str(settings.replace('Auto-connect', 'Autoconnect')).split()
        remove_these = {'-'}
        settings = [ele for ele in settings if ele not in remove_these]

        for i in settings:
            if 'Technology:' in i: settings.remove(i)
        for i in settings:
            if 'Protocol:' in i: settings.remove(i)
        for i in settings:
            if 'DNS:' in i: settings.remove(i)
        settings.sort()
        loopcounter=0
        for i in settings:
            for j in i:
                if j == ':':
                    i = i.replace(':', ': ')
                    settings[loopcounter] = i
            loopcounter+=1

        settingVar = easygui.choicebox('Choose what setting to toggle:', title, (settings))
        if settingVar == None: nordvpngui()
        loopcounter=0
        for j in settingVar:
            if j == ":":
                settingSelected = settingVar[:loopcounter].lower()
                break
            loopcounter +=1
        
        if settingSelected == 'autoconnect': settingDesc = 'Enables or disables auto-connect. When enabled, this feature will automatically try to connect to VPN on operating system startup.'
        elif settingSelected == 'cybersec': settingDesc = 'Enables or disables CyberSec. When enabled, the CyberSec feature will automatically block suspicious websites so that no malware or other cyber threats can infect your device. Also removes flashy ads.'
        elif settingSelected == 'killswitch': settingDesc = 'Enables or disables Kill Switch. This security feature blocks your device from accessing the Internet while not connected to the VPN or in case connection with a VPN server is lost.'
        elif settingSelected == 'notify': settingDesc = 'Enables or disables notifications.'
        elif settingSelected == 'obfuscate': settingDesc = 'Enables or disables obfuscation. When enabled, this feature allows to bypass network traffic sensors which aim to detect usage of the protocol and log, throttle or block it.'

        boolVar = easygui.buttonbox(f'{settingVar}\n\n{settingDesc}', title, ('Enable', 'Disable', 'Cancel'))
        if boolVar == "Enable": boolVar = "true"
        elif boolVar == "Disable": boolVar = "false"
        elif boolVar == None or boolVar == 'Cancel': nordvpngui()
        
        command1 = f'nordvpn set {settingSelected} {boolVar}'
        
        soutput = str(os.popen(command1).read()).split()
        if '-' in soutput: soutput.remove('-')
        if '/' in soutput: soutput.remove('/')
        if '|' in soutput: soutput.remove('|')
        if '\\' in soutput: soutput.remove('\\')
        msg(str(' '.join([str(elem) for elem in soutput])))
        nordvpngui()

nordvpngui()
