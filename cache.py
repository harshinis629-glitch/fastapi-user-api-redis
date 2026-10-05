import json
import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)


def set_cache(key, value, expire=60):
    redis_client.setex(
        key,
        expire,
        json.dumps(value)
    )


def get_cache(key):
    cached_data = redis_client.get(key)

    if cached_data:
        return json.loads(cached_data)

    return None


def delete_cache(key):
    redis_client.delete(key)