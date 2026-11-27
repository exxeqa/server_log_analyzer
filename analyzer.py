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

    print(ip_y)

#2025-11-27 05:32:19 | 126.17.12.84 | /home | 503 | 110ms --- log_example

def analyzer():
    with open(r"C:\server_log_analyzer\data\logs.txt", "r") as file:
        logs = file.readlines()
    ip_check(logs)

analyzer()
