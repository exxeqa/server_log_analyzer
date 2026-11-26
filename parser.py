with open(r"C:\server_log_analyzer\data\logs.txt", "r") as file:
    logs = file.readlines()
with open(r"C:\server_log_analyzer\data\logs_stat.txt", "w") as f:
    pass

#2025-11-27 05:32:19 | 126.17.12.84 | /home | 503 | 110ms --- log_example

response_codes, commands = {}, {}
ping = {
    "10-39ms": 0,
    "40-110ms": 0,
    "110+ms": 0
}

def parser():
    global response_codes, commands, ping
    for log in logs:
        log = log.split(" | ")
        r_code = log[3]
        if response_codes.get(r_code) == None:
            response_codes[r_code] = 0
            response_codes[r_code] += 1
        else:
            response_codes[r_code] += 1
        command = log[2]
        if commands.get(command) == None:
            commands[command] = 0
            commands[command] += 1
        else:
            commands[command] += 1
        ping_c = log[4]
        ping_c = ping_c[:-3]
        if int(ping_c) <= 39:
            ping["10-39ms"] += 1
        elif int(ping_c) <= 110:
            ping["40-110ms"] += 1
        else:
            ping["110+ms"] += 1
    with open(r"C:\server_log_analyzer\data\logs_stat.txt", "a") as logs_stat_file:
        logs_stat_file.write(f"{response_codes}\n{commands}\n{ping}")

parser()