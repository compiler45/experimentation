from celery import Celery


app = Celery('custom_task',
             backend='redis://localhost',
             broker='amqp://',
             include=['custom_task.tasks'])

app.conf.update(worker_send_task_events=True)


if __name__ == '__main__':
    app.start()