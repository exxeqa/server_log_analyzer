with open(r"C:\server_log_analyzer\data\logs.txt", "r") as file:
    logs = file.readlines()

#2025-11-27 05:32:19 | 126.17.12.84 | /home | 503 | 110ms --- log_example

response_codes, commands = {}, {}
ping = {
    "1-9ms": 0,
    "10-39ms": 0,
    "40-110ms": 0,
    "110+ms": 0
}

def parser():
    global response_codes, commands, ping
    for log in logs:
        log = log.split(" | ")
        print(log)
        r_code = log[3]
        response_codes[r_code] += 1
        command = log[2]
        commands[command] += 1
        ping_c = log[4]
        ping_c = ping_c[::4]
        print(ping_c)
        if int(ping_c) <= 9:
            ping["1-9ms"] += 1
        elif int(ping_c) <= 39:
            ping["10-39ms"] += 1
        elif int(ping_c) <= 110:
            ping["40-110ms"] += 1
        else:
            ping["110+ms"] += 1
    print(response_codes, commands, ping)

parser()