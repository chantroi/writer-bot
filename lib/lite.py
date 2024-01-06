import requests
import base64
import os
import io

def local_test(test_url, pingonly=False):
  if pingonly:
    cmd = f"./lite -ping 1 -config ./config/ping.json -test {test_url}"
  else:
    cmd = f"./lite -ping 1 -config ./config/config.json -test {test_url}"
  os.system(cmd)
  
def endpoint_test(test_url, endpoint_url, pingonly=False):
  if pingonly:
    data = {"url": test_url, "mode": "ping", "re": 1}
  else:
    data = {"url": test_url, "mode": "all", "re": 1}
  r = requests.post(endpoint_url, json=data, timeout=10000)
  res = r.json()
  city = res['city']
  country = res['country']
  org = res['org']
  result = requests.get(res['result']).content
  result = io.BytesIO(result)
  result.name = "out.png"
  return result, city, country, org
  

def get_config(url):
  if any(scheme in url for scheme in ["vmess:", "trojan:", "vless:", "ss:"]):
    res = url
    url = requests.post("https://paste.rs/", data=url).text
  else:
    res = requests.get(url, headers={"User-Agent": "v2rayNG"})
    if res.text is None:
      return None
    res = res.text
    if not any(res.startswith(sche) for sche in ["vmess", "trojan", "vless", "ss://"]):
      res = base64.b64decode(res.encode('utf-8')).decode('utf-8')
      url = requests.post("https://paste.rs/", data=res).text
  count = len(res.splitlines())
  return url, count