import requests, json, secrets, uuid, time, random
import httpx, asyncio
import string
import urllib
from user_agent import generate_user_agent
from MedoSigner import Gorgon,Ladon,Argus,md5
PROXY_INPUT = input("Enter Proxy (or press Enter to skip. Format: http://proxy): ").strip()
GLOBAL_PROXIES = {"http": PROXY_INPUT, "https": PROXY_INPUT} if PROXY_INPUT else None
HTTPX_PROXIES = PROXY_INPUT if PROXY_INPUT else None
def sign(params: str  = "" , payload: str = "", sec_device_id: str = "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)) , cookie: str = "", aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = 'v05.00.06-ov-android', sdk_version: int = 167775296, platform: int = 0, unix: int = int(round(time.time()))):
    params= urllib.parse.urlencode(params) if isinstance(params, dict) else params
    payload = urllib.parse.urlencode(payload) if isinstance(payload, dict) else (payload or "")
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
    return Gorgon(params, unix, payload, cookie).get_value() | {
        'content-length' : str(len(payload)),
        'x-ss-stub'      : x_ss_stub.upper(),
        'x-ladon'        : Ladon.encrypt(int(unix), license_id, aid),
        'x-argus'        : Argus.get_sign(params, x_ss_stub, int(unix),
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )}
class EmailToUsernameTikTok:
   def __init__(self,email : str) -> None:
      self.email=email
      self.secret = secrets.token_hex(16)
      self.client=self.client_builder()
      self.xor_email = self.xor(self.email)
      self.params = self.__get_param()
      self.cookies =  {"passport_csrf_token": self.secret,"passport_csrf_token_default": self.secret,"install_id": self.params["iid"],}
   def client_builder(self) -> httpx.AsyncClient:
       if HTTPX_PROXIES:
           return httpx.AsyncClient(http2=True,follow_redirects=True,proxy=HTTPX_PROXIES)
       return httpx.AsyncClient(http2=True,follow_redirects=True)
   def xor(self,string:str) -> str:
      return "".join([hex(ord(c) ^ 5)[2:] for c in string])
   def __get_param(self) -> dict:
       return {
    "request_tag_from": "h5",
    "fixed_mix_mode": "1",
    "mix_mode": "1",
    "account_param": self.xor_email,
    "scene": "1",
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "type": "3736",
    "_rticket": str(round(int(time.time()*1000))),
    "cdid": str(uuid.uuid4()),
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "380404",
    "version_name": "38.4.4",
    "manifest_version_code": "2023804040",
    "update_version_code": "2023804040",
    "ab_version": "38.4.4",
    "app_version": "38.4.4",
    "build_number": "38.4.4",
    "resolution": "2340*1080",
    "dpi": "440",
    "device_type": "SM-S918B",
    "device_brand": "samsung",
    "os_api": "33",
    "os_version": "13",
    "host_abi": "arm64-v8a",
    "language": "en",
    "ac": "wifi",
    "ac2": "wifi",
    "is_pad": "0",
    "current_region": "TW",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": str(round(int(time.time()))-random.randint(86400,86400*30)),
    "mcc_mnc": "46692",
    "timezone_name": "Asia/Baghdad",
    "carrier_region_v2": "466",
    "residence": "TW",
    "app_language": "en",
    "carrier_region": "TW",
    "timezone_offset": "10800",
    "locale": "en-GB",
    "op_region": "TW",
    "region": "GB",
    "ts": str(round(int(time.time()))),
    "iid": str(random.randint(7500000000000000000,7699999999999999999)),
    "device_id": str(random.randint(7500000000000000000,7699999999999999999)),
    "openudid": str(uuid.uuid4().hex[:16]),
    "uoo": "1",
    "support_webview": "1",
    "okhttp_version": "4.2.240.4-tiktok",
    "use_store_region_cookie": "1"
}
   def __get_token(self,email:str) -> str | None:
    headers = {
        'User-Agent': str(generate_user_agent()),
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Referer': 'https://mail.tm/',
        'Origin': 'https://mail.tm',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
        'Priority': 'u=4',
    }
    json_data = {
        'address':email,
        'password':"NtroAtro",
    }
    response = requests.post('https://api.mail.tm/token', headers=headers, json=json_data, proxies=GLOBAL_PROXIES)
    try:
        return response.json()["token"]
    except:
        return None
   async def __get_email(self) -> dict[str:str,str:str]:
    headers = {
        'User-Agent':str(generate_user_agent()),
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Referer': 'https://mail.tm/',
        'Origin': 'https://mail.tm',
        'Sec-Fetch-Dest': 'empty',
        'Seccd-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
        'Priority': 'u=0',
    }
    json_data = {
        'address': "".join(random.choices(string.ascii_lowercase + string.digits, k=12)) + '@web-library.net',
        'password': 'NtroAtro',
    }
    response = requests.post('https://api.mail.tm/accounts', headers=headers, json=json_data, proxies=GLOBAL_PROXIES)
    try:
        return {"id":response.json()["id"],"email":response.json()["address"]}
    except:
        return {"id":None,"email":None}
   async def __get_inbox(self,email:str,token:str,id:str) -> httpx.Response.json:
       try:
           headers = {
    'User-Agent': str(generate_user_agent()),
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://mail.tm/',
    'Origin': 'https://mail.tm',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'authorization': 'Bearer '+token,
    'Connection': 'keep-alive',
    'If-None-Match': '{}'.format(id),
    'Priority': 'u=0',
}
           response = requests.get('https://api.mail.tm/messages', headers=headers, proxies=GLOBAL_PROXIES)
           return response.json()
       except json.JSONDecodeError as e:
            return str(e)
   def __get_header(self, signature) -> httpx.Headers:
      return  {
        'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en_GB; SM-G998B; Build/SP1A.210812.016;tt-ok/3.12.13.16)",
        'Accept': "application/json, text/plain, */*",
        'x-ss-stub':signature['x-ss-stub'],
        'x-tt-dm-status': "login=1;ct=1;rt=1",
        'x-ss-req-ticket':signature['x-ss-req-ticket'],
        'x-ladon': signature['x-ladon'],
        'x-khronos': signature['x-khronos'],
        'x-argus': signature['x-argus'],
        'x-gorgon': signature['x-gorgon'],
        'content-type': "application/x-www-form-urlencoded",
        'content-length': '0',
        }
   async def __ticket_request(self) -> httpx.Response | None:
      for host in ["api16-normal-va.tiktokv.com",
        "api16-normal-c-alisg.tiktokv.com",
        "api16-normal-zr.tiktokv.com",
        "api31-normal-useast2a.tiktokv.com",
        "api16-normal-useast5.us.tiktokv.com",
        "api19-normal-useast8.us.tiktokv.com",
        "api31-normal-alisg.tiktokv.com",
        "api16-normal-c-tw.tiktokv.com",
        "api31-normal-zr.tiktokv.com",
        "api16-normal-no1a.tiktokv.eu",
        "api19-normal-ycru.tiktokv.com",
        "api16-normal.tiktokv.com",
        "api16-normal.ttapis.com",
        "api31-normal.tiktokv.com",
        "api22-normal.tiktokv.com",
        "api19-normal.tiktokv.com",
        "api-normal.tiktokv.com",
        "api21-normal.tiktokv.com",
        "api16-core.tiktokv.com",
        "api16-core-va.tiktokv.com",
        "api32-normal.tiktokv.com",
        "api33-normal.tiktokv.com"]:
            try:
                signature = sign(params=self.params,payload="",aid=1233)
                response = await self.client.post("https://"+host+"/passport/account_lookup/email/", headers=self.__get_header(signature), params=self.params, cookies=self.cookies)
                # print(response.json())
                if response.json()["data"] == None:
                    return None
                return response
            except Exception as e:
                continue 
      return None
   async def __send_code(self) -> str | function :
      try:
          tmMail = await self.__get_email() 
      except:
          return await self.__get_email()
      email = tmMail["email"]
      id = tmMail["id"]
      token = self.__get_token(email=email)
      response_ticket = await self.__ticket_request()
      if response_ticket == None:
          return "Email Not found in TikTok"
      try:
          ticket = response_ticket.json()["data"]["accounts"][0]["passport_ticket"]
      except Exception as e:
        return await self.__send_code()
      host = str(response_ticket.url).split("/passport/account_lookup/email/")[0].split("https://")[1]
      self.params.update({"not_login_ticket": ticket, "email": self.xor(email)})
      signature = sign(params=self.params,payload="",aid=1233)
      response = await self.client.post("https://"+host+"/passport/email/send_code/", headers=self.__get_header(signature), params=self.params, cookies=self.cookies)
    #   print(response.json())
      if "email_ticket" in response.text:
          await asyncio.sleep(5)
          inbox = await self.__get_inbox(email=email,token=token,id=id)
          username = await self.__extraxt_username(inbox=inbox,token=token)
          return username
      else:
          return await self.__send_code()
   async def __extraxt_username(self,inbox:httpx.Response.json,token:str) -> str:
       try:
           username =inbox["hydra:member"][0]["intro"].split("code Hi ")[1].split(",")[0]
           return username
       except Exception as e:
           return str(e)
   async def run(self) -> dict[str:str,str:str] | function :
    try:
        username = await self.__send_code()
        if username == "Email Not found in TikTok":
            return {"status": "Failed", "username": "", "email": self.email,"message": "Email Not found in TikTok"}
        return {"status": "success", "username": username, "email": self.email}
    except Exception as e:
        await self.__send_code()
if __name__ == "__main__":
    print(asyncio.run(EmailToUsernameTikTok(input("Enter Email :")).run()))
#by -> https://t.me/saftey_1