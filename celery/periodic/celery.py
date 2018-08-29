from celery import Celery
from celery.schedules import crontab

app = Celery(backend='redis://localhost',
             broker='amqp://')

app.conf.update({'timezone': 'Europe/London',
                 'enable_utc': False})


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds
    sender.add_periodic_task(10.0, test.s('hello'), name='Add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Wednesday evening at 9:51pm
    sender.add_periodic_task(
        crontab(hour=21, minute=51, day_of_week=3),
        test.s('How many planets there are with sad lights, thought Tetsuro.'),
        name='Lone thoughts, passing fogs of mind, upon the 999'
    )


@app.task
def test(arg):
    print(arg)
