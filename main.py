from generator import logs_gen_menu

def start():
    while True:
        try:
            choose = int(input(f"choose mode\n1.Generate logs\n2.Exit"))
            if choose == 1:
                logs_gen_menu()
                continue
            elif choose == 2:
                break
            else:
                print("choose must be 1 - 2")
                continue
        except ValueError:
            print("Enter a number!")
            continue

start()