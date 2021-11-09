import requests
import time
from selenium import webdriver

def main():
    
    yid = "fsv2157"
    ypass = "lu9w7ent"

    url = "https://auth.login.yahoo.co.jp/yconnect/v2/authorization"
    client_id = "dj00aiZpPVFiRmpRV1Z4cjFQdSZzPWNvbnN1bWVyc2VjcmV0Jng9Y2U"
    redirect_uri = ""

    params = {
        "response_type" : "code",
        "client_id" : client_id,
        "redirect_uri" : redirect_uri,
        "scope" : "openid address profile email",
        "bail" : 1
    }

    res = requests.get(url, params=params)
    time.sleep(1)

    # 初回だけこのURLをブラウザで開いてログインし、同意ボタンを押してもう一度最初から実行
    # print(res.url)
    # while(True):
    #     pass

    driver = webdriver.PhantomJS()
    driver.get(res.url)
    time.sleep(1)

    # ログイン処理
    driver.find_element_by_name("login").send_keys(yid)
    driver.find_element_by_name("btnNext").click()
    time.sleep(1)

    driver.find_element_by_name("passwd").send_keys(ypass)
    driver.find_element_by_name("btnSubmit").click()
    time.sleep(1)

    # 認可コード
    start = driver.current_url.find("code=") + 5
    Length = len(driver.current_url)
    code = driver.current_url[start:Length]

    # アクセストークン
    url = "https://auth.login.yahoo.co.jp/yconnect/v2/token"

    data = {
        "grant_type" : "authorization_code",
        "client_id" : client_id,
        "redirect_uri" : redirect_uri,
        "code" : code,
    }

    headers = {
        'Host': 'auth.login.yahoo.co.jp',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    res = requests.post(url, data=data, headers=headers)

    res_json = res.json()
    access_token = res_json["access_token"]
    refresh_token = res_json["refresh_token"]

    # 属性取得API（UserInfoAPI）
    url = "https://userinfo.yahooapis.jp/yconnect/v2/attribute"

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Host': 'userinfo.yahooapis.jp',
    }

    res = requests.get(url, headers=headers)
    print(res.json())
    
if __name__ == "__main__":
    main()