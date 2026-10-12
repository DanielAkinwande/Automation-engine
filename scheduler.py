import schedule
import time
from main import run_engine

def start():
    schedule.every(1).minutes.do(run_engine)

    while True:
        schedule.run_pending()
        time.sleep(1)   