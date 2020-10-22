import random
import threading
import logging
import concurrent.futures
import time
import queue


class Pipeline(queue.Queue):
    """This class allows a single element pipeline between a producer and a consumer"""
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logging.debug("{} about to get from the queue".format(name))
        value = self.get()
        logging.debug("{} got {} from queue".format(name, value))
        return value

    def set_message(self, value, name):
        logging.debug("{} about to add {} to the queue".format(name, value))
        self.put(value)
        logging.debug("{} added {} to the queue".format(name, value))


SENTINEL = object()


def producer(pipeline, event):
    """Let's image this random num generator is network and providing us messages"""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message {}".format(message))
        pipeline.set_message(message, "Producer")

    logging.info("Producer received EXIT event. Exiting")


def consumer(pipeline, event):
    """Pretending that it is saving number in DB"""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info("Consumer storing message {} (queue size = {})".format(message, pipeline.qsize()))

    logging.info("Consumer received EXIT event, Exiting")


if __name__ == '__main__':
    format_l = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_l, level=logging.DEBUG, datefmt="%H:%M:%S")

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(1)
        logging.info("Main about to set Event")
        event.set()
