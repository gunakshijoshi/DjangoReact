# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from .views import web_scraping
import time

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(web_scraping, trigger='interval', seconds=5)
    scheduler.start()

