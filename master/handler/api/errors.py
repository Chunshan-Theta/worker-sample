# coding:utf-8

status_0 = dict(status_code=405, reason='Method not allowed.')
status_1 = dict(status_code=404, reason='API not found.')
status_2 = dict(status_code=510, reason='Account is not logined.')
status_3 = dict(status_code=511, reason='Invalid ID.')

status_21 = dict(status_code=521, reason='The phone number has already been registered.')
status_22 = dict(status_code=404, reason='Resource not found.')
status_23 = dict(status_code=523, reason='Wrong password.')
status_24 = dict(status_code=524, reason='Upload file failed.')
status_25 = dict(status_code=404, reason='Post params not found.')


status_400_args_invalid = dict(status_code=400, reason='args invalid')
status_401_Unauthorized = dict(status_code=401, reason='Unauthorized')
status_401_not_support_model = dict(status_code=401, reason='Not Support Model')
status_401_header_incomplete = dict(status_code=401, reason='header incomplete')
status_406_Not_Acceptable_operation = dict(status_code=406, reason='Not Acceptable operation')


status_500_redis_responds_invalid = dict(status_code=500, reason='not correct respond')
status_500_redis_responds_Key_not_found = dict(status_code=500, reason='Key not found')
status_500_redis_connected_fail = dict(status_code=500, reason='redis connected fail')
status_504_redis_timeout = dict(status_code=504, reason='redis no responds')
status_500_unknown_error = dict(status_code=500, reason='unknown error')
