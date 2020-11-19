from datetime import datetime
from dateutil import tz

def get_current_timestamp(include_ms=True):
    # Eg. 2020-09-03 02:58:49.501749
    now = datetime.utcnow()
    # Eg. 1599073129.501749
    timestamp = datetime.timestamp(now)

    if include_ms is True:
        # Eg. 1599073129501
        result = int(timestamp * 1000)
    else:
        # Eg. 1599073129
        result = int(timestamp)

    return result


def get_year():
    now = datetime.now()
    return now.year


def get_datetime(timestamp,
                 to_timezone="Etc/GMT+8",
                 format="%Y-%m-%d %H:%M:%S"):
    # Format to include milliseconds = %Y-%m-%d %H:%M:%S.%f
    ms_timestamp = timestamp / 1000000
    from_zone = tz.gettz('UTC')
    from_datetime_obj = datetime.fromtimestamp(ms_timestamp, from_zone)
    to_zone = tz.gettz(to_timezone)
    to_datetime_obj = from_datetime_obj.astimezone(to_zone)
    to_datetime = to_datetime_obj.strftime(format)

    return to_datetime