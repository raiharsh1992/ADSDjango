from ads.celery import app

@app.task
def activate_task(duration):
    import time
    print(duration)
    time.sleep((duration))
    print("HELLO")