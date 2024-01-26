import logging

import redis
from redis import sentinel

logger = logging.getLogger(__name__)

REDIS_TIMEOUT = 2


def _get_redis_pool(redis_conf):
    """
    @param redis_conf: redis 配置
    sample1:
        {

            "host": "127.0.0.1",
            "port": 6379,
            "password": "xxx",
            "max_connections": 600,
            "db": 0,
        }
    sample2:
        {
            "use_sentinel": True,
            "sentinels": [
                ("127.0.0.1", 26379),
            ],
            "master_name": "mymaster",
            "password": "xxx",
            "max_connections": 600,
            "db": 0,
        }
    @return: redis 连接池
    """
    if redis_conf.get("use_sentinel", False):
        redis_sentinel = sentinel.Sentinel(redis_conf["sentinels"], socket_timeout=REDIS_TIMEOUT)
        return sentinel.SentinelConnectionPool(
            redis_conf["master_name"],
            redis_sentinel,
            db=redis_conf.get("db", 0),
            password=redis_conf["password"],
            max_connections=redis_conf["max_connections"],
        )

    return redis.BlockingConnectionPool(
        host=redis_conf["host"],
        port=redis_conf["port"],
        db=redis_conf.get("db", 0),
        password=redis_conf["password"],
        max_connections=redis_conf["max_connections"],
        socket_timeout=REDIS_TIMEOUT,
        timeout=REDIS_TIMEOUT,
    )


def get_redis_client(redis_conf):
    try:
        return redis.Redis(connection_pool=_get_redis_pool(redis_conf))
    except Exception:
        logger.exception("redis connection fail.")
        return None