from datetime import datetime
import time as pytime
from time import sleep
 
 
# Below is modified from python pause module, fixed an error
def until(time):
    """
   Pause your program until a specific end time.
   'time' is either a valid datetime object or unix timestamp in seconds (i.e. seconds since Unix epoch)
   """
    end = time
 
    # Convert datetime to unix timestamp
    if type(time) is datetime:
        end = time.timestamp() # float(time.strftime('%S.%f'))
 
    # Type check
    if type(end) not in [int, float]:
        raise Exception(
            'The time parameter is not a number or datetime object')
 
    # Now we wait
    while True:
        now = pytime.time()
        diff = end - now
 
        #
        # Time is up!
        #
        if diff <= 0:
            break
 
        #
        # Let's try to tune the precision, as we get closer to the end time
        #
 
        # Sleep by 0.001, when we're within 0.1 seconds
        if diff <= 0.1:
            sleep(0.001)
 
        # Sleep by 0.01, when we're within 0.5 seconds
        elif diff <= 0.5:
            sleep(0.01)
 
        # Sleep by 0.1, when we're within 1.5 seconds
        elif diff <= 1.5:
            sleep(0.1)
 
        # Otherwise sleep by 1 second
        else:
            sleep(1)
 
def main():
    dt = datetime(2018, 6, 5, 15, 27, 10, 0)
    dx = datetime.now()
    print("Seconds until epoch of wait time " + str(dt.timestamp()))
    print("Waiting until: " + str(dt) + ". It is currently: " + str(dx))
    until(dt)
    print("Done! It is now " + str(dt))
 
 
if __name__ == '__main__':
    main()
