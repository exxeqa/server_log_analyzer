import ast

def ip_check(logs):
    ips = []
    for log in logs:
        ip = log.split(" | ")[1]
        ips.append(ip)
    ip_y = {}
    for ip in ips:
        count = ips.count(ip)
        if count > 1:
            ip_y[ip] = count
    return ip_y

def error_codes(logs_stat):
    logs_stat = ast.literal_eval(logs_stat)
    for code in list(logs_stat.keys()):
        if int(code) < 400:
            del logs_stat[code]
    return logs_stat

#2025-11-27 05:32:19 | 126.17.12.84 | /home | 503 | 110ms --- log_example

def analyzer():
    with open(r"C:\server_log_analyzer\data\logs.txt", "r") as file:
        logs = file.readlines()
    ip_check(logs)
    with open(r"C:\server_log_analyzer\data\logs_stat.txt", "r") as file:
        logs_stat = file.readlines()
    error_codes(logs_stat[0])
    with open(r"C:\server_log_analyzer\data\statistic.txt", "w") as f:
        for i in



analyzer()
