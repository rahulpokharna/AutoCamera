import astral
import datetime
from pause import until
a = astral.Astral()
location = a['Columbia']
print('Information for %s' % location.name)
timezone = location.timezone
print('Timezone: %s' % timezone)
print('Latitude: %.02f; Longitude: %.02f' % (location.latitude, location.longitude))
d = datetime.date.today()
dTom = datetime.date.today() + datetime.timedelta(days=1)
sun = location.sun(local=True, date=dTom)
 
dt = sun['sunrise']
print("The time since epoch of sunrise tomorrow: ")
print(dt.timestamp())
print("The time of sunrise tomorrow: ")
print(dt)
print("The time of all sun positions tomorrow: ")
print(sun)
