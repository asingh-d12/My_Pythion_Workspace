import logging
import threading
import time


def thread_function(name):
    logging.info("Thread {} starting".format(name))
    time.sleep(2)
    print(threading.get_ident())
    logging.info("Thread {} ending".format(name))


if __name__ == '__main__':
    # This is the format for logging
    format_l = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_l, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main: Before creating thread.")

    # x is the thread created with name set to 1
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main: before running thread.")

    x.start()
    logging.info("Main: wait for thread to finish.")

    # Now, main thread is waiting for x thread to finish
    # Basically, Main: All done will be printed after thread_function is completely done
    x.join()
    logging.info("Main: All done")
