import random
import threading
import logging
import concurrent.futures


class Pipeline:
    """This class allows a single element pipeline between a producer and a consumer"""
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        # I understand now why we have this consumer lock
        # basically consumer can not read until producer has written
        # Once producer writes, he will release the conumer lock
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("{} about to acquire getlock".format(name))
        self.consumer_lock.acquire()
        logging.debug("{} have getlock".format(name))
        message = self.message
        logging.debug("{} about to release setlock".format(name))
        # And here, Consumer has to  release the producer lock
        # This will only happen after Consumer have consumed the data
        # Once Consumer consumes the data, it release producer lock so that producer can produce more data
        self.producer_lock.release()
        logging.debug("{} setlock released".format(name))
        return message

    def set_message(self, message, name):
        logging.debug("{} about to acquire setlock".format(name))
        self.producer_lock.acquire()
        logging.debug("{} have setlock".format(name))
        self.message = message
        logging.debug("{} about to release getlock".format(name))
        self.consumer_lock.release()
        logging.debug("{} getlock released".format(name))


SENTINEL = object()


def producer(pipeline):
    """Let's image this random num generator is network and providing us messages"""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message {}".format(message))
        pipeline.set_message(message, "Producer")

    # Send a SENTINEL message to tell consumer we are done
    pipeline.set_message(SENTINEL, "PRODUCER")


def consumer(pipeline):
    """Pretending that it is saving number in DB"""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message {}".format(message))


if __name__ == '__main__':
    format_l = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_l, level=logging.DEBUG, datefmt="%H:%M:%S")

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
