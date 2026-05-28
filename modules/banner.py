"""
    COPYRIGHT DISCLAIMER

    Script : sh4d0u-sploit - All in One Android Hacking ADB Toolkit

    Copyright (C) 2026  sh4d0u

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Forking and modifying are allowed, but credit must be given to the
    original developer, [sh4d0u], and copying the code
    is not permitted without permission.

    
"""

version = "v1.0"

menu1 = """
    [white]1. [green]Connect a Device             [white]6. [green]Get Screenshot                       [white]11. [green]Install an APK
    [white]2. [green]List Connected Devices       [white]7. [green]Screen Record                        [white]12. [green]Uninstall an App
    [white]3. [green]Disconnect All Devices       [white]8. [green]Download File/Folder from Device     [white]13. [green]List Installed Apps
    [white]4. [green]Scan Network for Devices     [white]9. [green]Send File/Folder to Device           [white]14. [green]Access Device Shell
    [white]5. [green]Mirror & Control Device     [white]10. [green]Run an App                           [white]15. [green]Launch Metasploit Attack

  [yellow]N: Next Page                                      (Page : 1 / 5)[/yellow]"""

menu2 = """
    [white]16. [green]List All Folders/Files      [white]21. [green]Anonymous Screenshot                [white]26. [green]Play a Video on Device
    [white]17. [green]Send SMS                    [white]22. [green]Anonymous Screen Record             [white]27. [green]Get Device Information
    [white]18. [green]Copy WhatsApp Data          [white]23. [green]Open a Link on Device               [white]28. [green]Get Battery Information
    [white]19. [green]Copy All Screenshots        [white]24. [green]Display a Photo on Device           [white]29. [green]Restart Device
    [white]20. [green]Copy All Camera Photos      [white]25. [green]Play an Audio on Device             [white]30. [green]Advanced Reboot Options

  [yellow]P: Previous Page         N: Next Page            (Page : 2 / 5)[/yellow]"""

menu3 = """
    [white]31. [green]Unlock Device               [white]36. [green]Extract APK from Installed App      [white]41. [green]Record Mic Audio
    [white]32. [green]Lock Device                 [white]37. [green]Stop ADB Server                     [white]42. [green]Listen Device Audio
    [white]33. [green]Dump All SMS                [white]38. [green]Power Off Device                    [white]43. [green]Record Device Audio
    [white]34. [green]Dump All Contacts           [white]39. [green]Use Keycodes (Control Device)       [white]44. [green]TCP Port Forward / Reverse
    [white]35. [green]Dump Call Logs              [white]40. [green]Listen Mic Audio                    [white]45. [green]Force Stop App

  [yellow]P: Previous Page         N: Next Page            (Page : 3 / 5)[/yellow]"""

menu4 = """
    [white]46. [green]Clear App Data                 [white]51. [green]Network Snapshot               [white]56. [green]WiFi Status Dump
    [white]47. [green]Save Logcat Snippet            [white]52. [green]Install Split APKs             [white]57. [green]WLAN IP Info
    [white]48. [green]Grant / Revoke Permission      [white]53. [green]Developer Settings             [white]58. [green]WiFi Radio Toggle
    [white]49. [green]Restart App                    [white]54. [green]Read Locale                    [white]59. [green]Ping Connectivity
    [white]50. [green]Live Logcat Stream             [white]55. [green]Screen Stay-On                 [white]60. [green]Saved WiFi Networks

  [yellow]P: Previous Page         N: Next Page            (Page : 4 / 5)[/yellow]"""

menu5 = """
    [white]61. [green]Root Heuristics                [white]62. [green]Exit & Update Check           

  [yellow]P: Previous Page                                  (Page : 5 / 5)[/yellow]"""

menu = [menu1, menu2, menu3, menu4, menu5]

instruction = """
This attack will launch Metasploit-Framework    (msfconsole)

Use 'Ctrl + C' to stop at any point

1. Wait until you see:

    [green]meterpreter >      [/green]

2. Then use 'help' command to see all meterpreter commands:

    [green]meterpreter > [yellow]help       [/yellow][/green]

3. To exit meterpreter enter 'exit' or To exit Metasploit enter 'exit -y':

    [green]meterpreter > [yellow]exit       [/yellow][/green]

    [green]msf6 > [yellow]exit -y       [/yellow][/green]

[red]\\[sh4d0u-sploit][/red]   Press 'Enter' to continue attack / '0' to Go Back to Main Menu
    """

banner2 = """
          _     _  _       _  ___                  ____        _       _ _   
      ___| |__ | || |   __| |/ _ \ _   _          / ___| _ __ | | ___ (_) |_ 
     / __| '_ \| || |_ / _` | | | | | | |  _____  \___ \| '_ \| |/ _ \| | __|
     \__ \ | | |__   _| (_| | |_| | |_| | |_____|  ___) | |_) | | (_) | | |_ 
     |___/_| |_|  |_|  \__,_|\___/ \__,_|         |____/| .__/|_|\___/|_|\__|
                                                        |_|                  
        

                            [red]{version}[/red]            [white]By sh4d0u[/white]
""".format(version=version)

banner3 = """
                   #                ###                       #####                               
      ####  #    # #    #  #####   #   #  #    #             #     # #####  #       ####  # ##### 
     #      #    # #    #  #    # #     # #    #             #       #    # #      #    # #   #   
      ####  ###### #    #  #    # #     # #    #    #####     #####  #    # #      #    # #   #   
          # #    # ####### #    # #     # #    #                   # #####  #      #    # #   #   
     #    # #    #      #  #    #  #   #  #    #             #     # #      #      #    # #   #   
      ####  #    #      #  #####    ###    ####               #####  #      ######  ####  #   #   



                                [red]{version}[/red]             [white]By sh4d0u[/white]
""".format(version=version)

banner4 = """
    :'######::'##::::'##:'##::::::::'########::::'#####:::'##::::'##:::::::::::::::::'######::'########::'##::::::::'#######::'####:'########:
    '##... ##: ##:::: ##: ##:::'##:: ##.... ##::'##.. ##:: ##:::: ##::::::::::::::::'##... ##: ##.... ##: ##:::::::'##.... ##:. ##::... ##..::
     ##:::..:: ##:::: ##: ##::: ##:: ##:::: ##:'##:::: ##: ##:::: ##:::::::::::::::: ##:::..:: ##:::: ##: ##::::::: ##:::: ##:: ##::::: ##::::
    . ######:: #########: ##::: ##:: ##:::: ##: ##:::: ##: ##:::: ##::::'#######::::. ######:: ########:: ##::::::: ##:::: ##:: ##::::: ##::::
    :..... ##: ##.... ##: #########: ##:::: ##: ##:::: ##: ##:::: ##::::........:::::..... ##: ##.....::: ##::::::: ##:::: ##:: ##::::: ##::::
    '##::: ##: ##:::: ##:...... ##:: ##:::: ##:. ##:: ##:: ##:::: ##::::::::::::::::'##::: ##: ##:::::::: ##::::::: ##:::: ##:: ##::::: ##::::
    . ######:: ##:::: ##::::::: ##:: ########:::. #####:::. #######:::::::::::::::::. ######:: ##:::::::: ########:. #######::'####:::: ##::::
    :......:::..:::::..::::::::..:::........:::::.....:::::.......:::::::::::::::::::......:::..:::::::::........:::.......:::....:::::..:::::

                        [red]{version}[/red]                             [white]By sh4d0u[/white]
""".format(version=version)

banner5 = """
    .d8888. db   db   j88D  d8888b.  .d88b.  db    db                  .d8888. d8888b. db       .d88b.  d888888b d888888b 
    88'  YP 88   88  j8~88  88  `8D .8P  88. 88    88                  88'  YP 88  `8D 88      .8P  Y8.   `88'   `~~88~~' 
    `8bo.   88ooo88 j8' 88  88   88 88  d'88 88    88                  `8bo.   88oodD' 88      88    88    88       88    
      `Y8b. 88~~~88 V88888D 88   88 88 d' 88 88    88      C8888D        `Y8b. 88~~~   88      88    88    88       88    
    db   8D 88   88     88  88  .8D `88  d8' 88b  d88                  db   8D 88      88booo. `8b  d8'   .88.      88    
    `8888Y' YP   YP     VP  Y8888D'  `Y88P'  ~Y8888P'                  `8888Y' 88      Y88888P  `Y88P'  Y888888P    YP    
                                                                                                                      
                                                                                                                      
                            [red]{version}[/red]                        [white]By sh4d0u[/white]
""".format(version=version)

banner6 = """
          _    _  _      _  ___                    _____       _       _ _   
         | |  | || |    | |/ _ \                  / ____|     | |     (_) |  
      ___| |__| || |_ __| | | | |_   _   ______  | (___  _ __ | | ___  _| |_ 
     / __| '_ \__   _/ _` | | | | | | | |______|  \___ \| '_ \| |/ _ \| | __|
     \__ \ | | | | || (_| | |_| | |_| |           ____) | |_) | | (_) | | |_ 
     |___/_| |_| |_| \__,_|\___/ \__,_|          |_____/| .__/|_|\___/|_|\__|
                                                        | |                  
                                                        |_|                  

                            [red]{version}[/red]               [white]By sh4d0u[/white]
""".format(version=version)

banner10 = """
            .__        _____      .__________                           _________        .__           .__   __    
      ______|  |__    /  |  |   __| _/\   _  \   __ __                 /   _____/______  |  |    ____  |__|_/  |_  
     /  ___/|  |  \  /   |  |_ / __ | /  /_\  \ |  |  \     ______     \_____  \ \____ \ |  |   /  _ \ |  |\   __\ 
     \___ \ |   Y  \/    ^   // /_/ | \  \_/   \|  |  /    /_____/     /        \|  |_> >|  |__(  <_> )|  | |  |   
    /____  >|___|  /\____   | \____ |  \_____  /|____/                /_______  /|   __/ |____/ \____/ |__| |__|   
         \/      \/      |__|      \/        \/                               \/ |__|                              
                                                                                                               

                    [red]{version}[/red]                                [white]By sh4d0u[/white]
""".format(version=version)

banner11 = """
      ▌ ▖▖ ▌▄▖        ▄▖  ▜   ▘▗ 
    ▛▘▛▌▙▌▛▌▛▌▌▌  ▄▖  ▚ ▛▌▐ ▛▌▌▜▘
    ▄▌▌▌ ▌▙▌█▌▙▌      ▄▌▙▌▐▖▙▌▌▐▖
                        ▌        


            [red]{version}[/red]                            [white]By sh4d0u[/white]
""".format(version=version)

banner12 = """
             oooo              .o         .o8    .oooo.                                  .oooooo..o            oooo             o8o      .   
             `888            .d88        "888   d8P'`Y8b                                d8P'    `Y8            `888             `"'    .o8   
     .oooo.o  888 .oo.     .d'888    .oooo888  888    888 oooo  oooo                    Y88bo.      oo.ooooo.   888   .ooooo.  oooo  .o888oo 
    d88(  "8  888P"Y88b  .d'  888   d88' `888  888    888 `888  `888                     `"Y8888o.   888' `88b  888  d88' `88b `888    888   
    `"Y88b.   888   888  88ooo888oo 888   888  888    888  888   888       8888888           `"Y88b  888   888  888  888   888  888    888   
    o.  )88b  888   888       888   888   888  `88b  d88'  888   888                    oo     .d8P  888   888  888  888   888  888    888 . 
    8""888P' o888o o888o     o888o  `Y8bod88P"  `Y8bd8P'   `V88V"V8P'                   8""88888P'   888bod8P' o888o `Y8bod8P' o888o   "888" 
                                                                                                     888                                     
                                                                                                    o888o            

                                                                                                                                                                                                                           
                [red]{version}[/red]                            [white]By sh4d0u[/white]
""".format(version=version)

banner_list = [
    banner2,
    banner3,
    banner4,
    banner5,
    banner6,
    banner10,
    banner11,
    banner12,
]

instructions_banner = """[cyan]
        ____           __                  __  _
       /  _/___  _____/ /________  _______/ /(_)___  ____  _____
       / // __ \\/ ___/ __/ ___/ / / / ___/ __/ / __ \\/ __ \\/ ___/
     _/ // / / (__  ) /_/ /  / /_/ / /__/ /_/ / /_/ / / / (__  )
    /___/_/ /_/____/\\__/_/   \\__,_/\\___/\\__/_/\\____/_/ /_/____/
[/cyan]"""

hacking_banner = """[green]
    █░█ ▄▀█ █▀▀ █▄▀ █ █▄░█ █▀▀ ░ ░ ░
    █▀█ █▀█ █▄▄ █░█ █ █░▀█ █▄█ ▄ ▄ ▄
[/green]"""

keycode_menu = """
    [white]1. [green]Keyboard Text Input                [white]11. [green]Enter
    [white]2. [green]Home                               [white]12. [green]Volume Up
    [white]3. [green]Back                               [white]13. [green]Volume Down
    [white]4. [green]Recent Apps                        [white]14. [green]Media Play
    [white]5. [green]Power Button                       [white]15. [green]Media Pause
    [white]6. [green]DPAD Up                            [white]16. [green]Tab
    [white]7. [green]DPAD Down                          [white]17. [green]Esc
    [white]8. [green]DPAD Left
    [white]9. [green]DPAD Right
   [white]10. [green]Delete/Backspace[/green]
"""


