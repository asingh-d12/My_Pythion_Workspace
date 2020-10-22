import logging
import time
import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread {}: starting update".format(name))
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread {}: finishing update".format(name))


if __name__ == '__main__':
    format_l = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_l, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is {}".format(database.value))

    # Here we are going to use threads now
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)

    logging.info("Testing update. Ending value is {}".format(database.value))
