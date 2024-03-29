import re
from datetime import datetime
import pytz, requests, base64

def convert_bytes_to_human_readable(bytes_value):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0

    while bytes_value >= 1024 and unit_index < len(units) - 1:
        bytes_value /= 1024.0
        unit_index += 1

    result = "{:.2f} {}".format(bytes_value, units[unit_index])
    return result

def convert_timestamp_to_datetime(timestamp, timezone='UTC'):
    utc_datetime = datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
    local_datetime = utc_datetime.astimezone(pytz.timezone(timezone))
    return local_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')

def parse_url(url):
    try:
        r = requests.get(url, headers={"User-Agent": "quantumult%20x"}, proxies={"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888"}, timeout=30)
        res_string = r.headers.get("subscription-userinfo")
    except Exception:
        r = requests.get(url, headers={"User-Agent": "quantumult%20x"},  timeout=30)
        res_string = r.headers.get("subscription-userinfo")
    res_text = r.text
    if "{" in res_text or not res_text:
        raise Exception("Unavailable")
    try:
        res_text = base64.b64decode(res_text)
    except Exception:
        pass
    result_dict = {}
    orgi_dict = {}
    if res_string:
        pairs = res_string.split('; ')
        for pair in pairs:
            key, value = pair.split('=')
            if key in ['upload', 'download', 'total']:
                orgi_dict[key] = value
                value = convert_bytes_to_human_readable(float(value))
            elif key == 'expire':
                try:
                    value = convert_timestamp_to_datetime(int(value), timezone='Asia/Ho_Chi_Minh')
                except:
                    value = "khong xac dinh"
            result_dict[key] = value
        if 'upload' in result_dict and 'download' in result_dict and 'total' in result_dict:
            available = int(orgi_dict['total']) - (int(orgi_dict['upload']) + int(orgi_dict['download']))
            result_dict['available'] = convert_bytes_to_human_readable(available)
    return result_dict, len(res_text.splitlines())