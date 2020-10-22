import concurrent.futures
import subprocess
import time
import threading


check_ip = "192.168.0.{}"
ping_cmd = "ping -c4 {}"


def ping_servers(ip_suff):
    try:
        print("Thread Name {} : {} --> {}".format(threading.get_ident(), check_ip.format(ip_suff),
                                                  subprocess.check_output(ping_cmd.format(check_ip.format(ip_suff)).
                                                                          split()).decode().strip().split('\n')[-2]))
    except subprocess.CalledProcessError:
        # pass
        print("Thread Name {} : {} -> {}".format(threading.get_ident(), check_ip.format(ip_suff),
                                                 "This ip is not present!!"))


if __name__ == '__main__':
    # Here I am going to use MultiThreading to start several ips
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(ping_servers, range(2, 200))
    end_time = time.time()

    print("Time taken = {}".format(end_time - start_time))
