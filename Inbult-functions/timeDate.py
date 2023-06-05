import datetime

currentDate = datetime.date.today()
date_formatted = currentDate.strftime('Day %d- Month %m- Year %y')

print('Not farmatted ',currentDate)
print('Date formatted ', date_formatted)

print('----------------------------------------')

currentTime = datetime.datetime.now().time()
formattedTime = currentTime.strftime('%H:%M:%S')
print('Not formatted ',currentTime)
print('formatted time ', formattedTime)
