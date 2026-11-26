from generator import logs_gen_menu
from parser import parser

def start():
    while True:
        try:
            choose = int(input(f"choose mode\n1.Generate logs\n2.Logs parser\n3.Exit"))
            if choose == 1:
                logs_gen_menu()
                continue
            elif choose == 2:
                parser()
                continue
            elif choose == 3:
                break
            else:
                print("choose must be 1 - 3")
                continue
        except ValueError:
            print("Enter a number!")
            continue

start()