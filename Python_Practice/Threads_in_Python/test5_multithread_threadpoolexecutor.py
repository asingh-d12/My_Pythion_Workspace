import concurrent.futures
import logging
import time


def thread_function(name):
    logging.info("Thread {} starting".format(name))
    time.sleep(2)
    # print(threading.get_ident())
    logging.info("Thread {} ending".format(name))


if __name__ == '__main__':
    format_l = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_l, level=logging.INFO, datefmt="%H:%M:%S")

    # Here is where it gets interesting
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
