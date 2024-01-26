import datetime

import arrow
from dateutil.tz import tzutc
from django.conf import settings
from django.utils import timezone

ARROW_FORMAT_WITH_TZ = "YYYY-MM-DD HH:mm:ssZ"


def now():
    return timezone.now()


def now_str():
    """
    :return: local format str
    """
    return arrow.now("local").format(ARROW_FORMAT_WITH_TZ)


def aware_time(value):
    if not timezone.is_aware(value):
        value = timezone.make_aware(value)
    return value


def utctime(value, *args, **kwargs):
    """
    Convert value to arrow utc time
    :param value: datetime object, tz time str, arrow object
    :return: a arrow object with utc tzinfo
    """
    if isinstance(value, datetime.datetime):
        value = aware_time(value)
    return arrow.get(value, *args, **kwargs).to("utc")


def format(value, fmt=ARROW_FORMAT_WITH_TZ, *args, **kwargs):
    """
    :param value: timestamp, utc time str, arrow object, datetime object
    :return: local format str
    """
    if isinstance(value, datetime.datetime):
        value = aware_time(value)
    return arrow.get(value, *args, **kwargs).to("local").format(fmt)


def now_datetime():
    """
    :return datetime: now datetime
    """
    return arrow.utcnow().datetime

    
def now_timestamp():
    """
    :return: int, current timestamp
    """
    return arrow.utcnow().timestamp


def timestamp(value):
    """
    :param value: utc time str, arrow object, datetime object
    :return: int, the timestamp
    """
    if isinstance(value, datetime.datetime):
        value = aware_time(value)

    return arrow.get(value).timestamp


def far_away_future():
    if settings.USE_TZ:
        return datetime.datetime(year=2100, month=1, day=1, tzinfo=timezone.utc)

    return datetime.datetime(year=2100, month=1, day=1)


class NeverExpiresTime:
    # 永久有效期，使用2100.01.01 00:00:00 的unix time作为永久有效期的表示，时间戳为：4102444800
    time = datetime.datetime(2100, 1, 1, 0, 0, tzinfo=tzutc())

    @staticmethod
    def is_never_expired(value):
        return value >= NeverExpiresTime.time