from multiprocessing.pool import ThreadPool

from src.actions.create_article import create_vg_account


def run_thread(thread_id):
    create_vg_account()


pool = ThreadPool(10)
pool.map(run_thread, range(0, 49))
pool.close()
pool.join()