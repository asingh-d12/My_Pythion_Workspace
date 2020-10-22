import logging
import threading
import time


def thread_function(name):
    logging.info("Thread {} starting".format(name))
    time.sleep(2)
    # print(threading.get_ident())
    logging.info("Thread {} ending".format(name))


if __name__ == '__main__':
    # This is the format for logging
    format_l = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_l, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main: Before creating thread.")

    # Now here we think of using Multiple Threads
    threads = list()

    for i in range(3):
        # x is the thread created with name set to i
        x = threading.Thread(target=thread_function, args=(i,))

        # Add the thread created to list of threads
        threads.append(x)

        # finally, start the thread
        x.start()

    # Let's wait for these threads to end and exit the program
    for index, thread in enumerate(threads):
        logging.info("Main: Before joining thread {}".format(index))
        thread.join()
        logging.info("Main: After joining thread {}".format(index))

    logging.info("Main: All done")
