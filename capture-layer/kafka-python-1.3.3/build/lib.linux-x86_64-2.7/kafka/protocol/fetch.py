from __future__ import absolute_import

from .api import Request, Response
from .message import MessageSet
from .types import Array, Int16, Int32, Int64, Schema, String


class FetchResponse_v0(Response):
    API_KEY = 1
    API_VERSION = 0
    SCHEMA = Schema(
        ('topics', Array(
            ('topics', String('utf-8')),
            ('partitions', Array(
                ('partition', Int32),
                ('error_code', Int16),
                ('highwater_offset', Int64),
                ('message_set', MessageSet)))))
    )


class FetchResponse_v1(Response):
    API_KEY = 1
    API_VERSION = 1
    SCHEMA = Schema(
        ('throttle_time_ms', Int32),
        ('topics', Array(
            ('topics', String('utf-8')),
            ('partitions', Array(
                ('partition', Int32),
                ('error_code', Int16),
                ('highwater_offset', Int64),
                ('message_set', MessageSet)))))
    )


class FetchResponse_v2(Response):
    API_KEY = 1
    API_VERSION = 2
    SCHEMA = FetchResponse_v1.SCHEMA  # message format changed internally


class FetchResponse_v3(Response):
    API_KEY = 1
    API_VERSION = 3
    SCHEMA = FetchResponse_v2.SCHEMA


class FetchRequest_v0(Request):
    API_KEY = 1
    API_VERSION = 0
    RESPONSE_TYPE = FetchResponse_v0
    SCHEMA = Schema(
        ('replica_id', Int32),
        ('max_wait_time', Int32),
        ('min_bytes', Int32),
        ('topics', Array(
            ('topic', String('utf-8')),
            ('partitions', Array(
                ('partition', Int32),
                ('offset', Int64),
                ('max_bytes', Int32)))))
    )


class FetchRequest_v1(Request):
    API_KEY = 1
    API_VERSION = 1
    RESPONSE_TYPE = FetchResponse_v1
    SCHEMA = FetchRequest_v0.SCHEMA


class FetchRequest_v2(Request):
    API_KEY = 1
    API_VERSION = 2
    RESPONSE_TYPE = FetchResponse_v2
    SCHEMA = FetchRequest_v1.SCHEMA


class FetchRequest_v3(Request):
    API_KEY = 1
    API_VERSION = 3
    RESPONSE_TYPE = FetchResponse_v3
    SCHEMA = Schema(
        ('replica_id', Int32),
        ('max_wait_time', Int32),
        ('min_bytes', Int32),
        ('max_bytes', Int32),  # This new field is only difference from FR_v2
        ('topics', Array(
            ('topic', String('utf-8')),
            ('partitions', Array(
                ('partition', Int32),
                ('offset', Int64),
                ('max_bytes', Int32)))))
    )


FetchRequest = [FetchRequest_v0, FetchRequest_v1, FetchRequest_v2,
    FetchRequest_v3]
FetchResponse = [FetchResponse_v0, FetchResponse_v1, FetchResponse_v2,
    FetchResponse_v3]