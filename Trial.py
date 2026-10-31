import time

start_time = time.monotonic()
print(start_time)
elapsed = time.monotonic() - start_time
print(elapsed)

while time.monotonic() - start_time <= 10:
    time.sleep(1)
    print (f"The timer is {time.monotonic()}")
    elapsed = time.monotonic()