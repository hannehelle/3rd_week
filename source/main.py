from datetime import datetime, timedelta

one_day = timedelta(days=1)

today = datetime.now().strftime("%Y/%m/%d")
yesterday = (datetime.now()-one_day).strftime("%Y/%m/%d")
tomorrow = (datetime.now()+one_day).strftime("%Y/%m/%d")

print('Сегодня ',today, ', вчера ', yesterday, ', завтра', tomorrow)

date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

print ('Строка - в дату. Проверка класса date_dt:', type(date_dt))