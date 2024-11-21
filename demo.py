import time
# Convert seconds since epoch to struct_time in UTC
utc_time = time.gmtime(1627987508.6496193)
print("UTC time:", utc_time)

# Convert seconds since epoch to struct_time in local time
local_time = time.localtime(1627987508.6496193)
print("Local time:", local_time)

# Convert struct_time to seconds since epoch
seconds_since_epoch = time.mktime(local_time)
print("Seconds since epoch:", seconds_since_epoch)