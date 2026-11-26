import random
from datetime import datetime, timedelta

TimeB = datetime.now()
TimeB -= timedelta(weeks=52)
TimeB = TimeB.replace(microsecond=0)

def ip_generator():
    field = []
    for i in range(4):
        field.append(str(random.randint(0, 255)))
    ip_address = ".".join(field)
    return str(ip_address)

def response_generator():
    ranges = [(200, 204), (301, 304), (400, 404), (500, 503)]
    start, end = random.choice(ranges)
    response_code = random.randint(start, end)
    return str(response_code)

def command_generator():
    commands = ["/login", "/register", "/profile", "/home"]
    command = random.choice(commands)
    return command

def time_generator():
    global TimeB
    TimeB += timedelta(minutes=random.randint(1, 120))
    TimeB += timedelta(seconds=random.randint(1, 60))
    time = TimeB
    return time

def delay_generator():
    delay_rare = random.randint(1, 9)
    if delay_rare <= 6:
        delay = random.randint(40, 110)
    elif delay_rare == 7:
        delay = random.randint(10, 39)
    else:
        delay = random.randint(111, 300)
    return str(delay)

def logs_generator(generations_amount):
    logs = []
    with open(r"C:\server_log_analyzer\data\logs.txt", "w") as f:
        pass
    for log in range(generations_amount):
        time = time_generator()
        time = str(time)
        ip = ip_generator()
        r_code = response_generator()
        command = command_generator()
        delay = delay_generator() + "ms"

        log_comp = [time, ip, command, r_code, delay]

        log = " | ".join(log_comp)

        print(log)

        logs.append(log)

    with open(r"C:\server_log_analyzer\data\logs.txt", "a") as file:
        for log in logs:
            file.write(f"{log}\n")

def logs_gen_menu():
    generations_amount = 0
    generations_amount += int(input(f"choose how many logs you want to generate"))
    logs_generator(generations_amount)