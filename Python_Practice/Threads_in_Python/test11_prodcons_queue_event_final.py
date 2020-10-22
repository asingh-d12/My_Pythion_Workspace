import concurrent.futures
import queue
import logging
import threading
import time
import random


def producer(queue, event):
    """Pretend we're getting a number from the network"""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got Message {}".format(message))
        queue.put(message)

    logging.info("Producer received event, exiting...")


def consumer(queue, event):
    """Pretend that this Consumer is reading message from Queue and storing it in DB"""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Consumer Storing {}, (queue size = {})".format(message, queue.qsize()))
    logging.info("Consumer received event, exiting...")


if __name__ == '__main__':
    format_l = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_l, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main about to set event...")
        event.set()
