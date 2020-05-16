time = int(input('Введите время в секундах: '))
hours = int(time / 3600)
minutes = int((time % 3600 / 60))
seconds = int(time % 60)
if hours < 10:
    hours = '0%s' % hours
else:
    hours = str(hours)
if minutes < 10:
    minutes = '0%s' % minutes
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = '0%s' % seconds
else:
    seconds = str(seconds)
print('{}:{}:{}'.format(hours, minutes, seconds))
