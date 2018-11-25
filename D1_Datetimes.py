from datetime import datetime
from datetime import date
from datetime import timedelta

todaydate = date.today()

sleephour = timedelta(hours=6)

todaydate + sleephour

set_date = date(2018, 11, 22)
set_date

todaytime = datetime.today()
todaytime + sleephour

set_datetime = datetime(2018, 11, 23, 4, 46, 18, 650656)
str(todaytime + sleephour)
christmas = date(2018,12,25)
christmas
str(christmas)

todaydate - christmas
christmas - todaydate
(christmas - todaydate).days
str((christmas - todaydate).days)
