import os
import logging
import threading
from blockchain import statistics
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
workers = os.getenv('WORKERS')
str_task = 'Task Executed {0}'


def get_stats(opt: int):
    stats = statistics.get()

    if opt == 1:
        logging.info('{0}'.format(stats.total_btc_sent))
        logging.info(str_task.format(threading.current_thread()))
    elif opt == 2:
        logging.info('{0}'.format(stats.number_of_transactions))
        logging.info(str_task.format(threading.current_thread()))
    elif opt == 3:
        logging.info('{0}'.format(stats.btc_mined))
        logging.info(str_task.format(threading.current_thread()))


def main():
    executor = ThreadPoolExecutor(max_workers=int(workers))
    executor.submit(get_stats, 1)
    executor.submit(get_stats, 2)

    executor.submit(get_stats, 3)
    executor.submit(get_stats, 2)

    executor.submit(get_stats, 1)


if __name__ == '__main__':
    main()
