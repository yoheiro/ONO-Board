import speech_recognition as sr
import pyautogui 
import time

user_data = [{'Name':'髙木','mode':{'プログラミング':{'ペタペタ':[{'hotkey':['ctrl','c']},{'write':'hallow'}],
                                                    'じゃばじゃば':[{'press':['win']}]},
                                    'デスクトップ':{'ペタペタ':[],
                                                    'じゃばじゃば':[]
                                                    }
                                    }
             },
            {'Name':'村田','mode':{'ガンダム':{'ペタペタ':[],
                                                'じゃばじゃば':[]},
                                    'マクロス':{'ペタペタ':[],
                                                'じゃばじゃば':[]}
                                    }
            },
            {'Name':'吉田','mode':{'プログラミング':{'ペタペタ':[],
                                                'じゃばじゃば':[]
                                                    },
                                    'マクロス':{'ペタペタ':[],
                                                'じゃばじゃば':[]}
                                    }
            }            
            ]
        #ログイン後取得予定データの例
loginUserdata={'Name':'髙木','mode':{'プログラミング':{'ペタペタ':[{'hotkey':['ctrl','c']},{'write':'hallow'}],
                                                    'じゃばじゃば':[{'press':['win']}]},
                                    'デスクトップ':{'ペタペタ':[],
                                                    'じゃばじゃば':[]
                                                    }
                                    }
             }
currentUser='admin'
currentmode="default"
currentBind = None


# 音声入力
def recognition():#音声認識スタート
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("引けば老いるぞ、臆せば死ぬぞ、、叫べ！我が名は....!!!")
            audio = r.listen(source)
    
        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            print("Google Web Speech APIは音声を認識できませんでした。")
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
                " {0}".format(e))
        else:
            global currentUser
            currentUser = text
            print(text+"!!!!!!!!!!")
            #login実装したい
            #userplofileをすべて取ってくる
            if currentUser =="高木":
               print("succsess")
               break
            else :
                print("もう一度だ...")
                
# bind設定
# mode1 = {'プログラミング':{'ペタペタ':[{'hotkey':['ctrl','c']},{'write':'hallow'}],
#                                                     'じゃばじゃば':[{'press':['win']}]},
#                                     'デスクトップ':{'ペタペタ':[],
#                                                     'じゃばじゃば':[]
#                                                     }
#                                     }
mode1 =user_data[0]['mode']['プログラミング']                               
list =[{'hotkey':['ctrl','c']},{'write':'hallow'}]

def setmode(loginUserdata):
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("解号は！！")
            audio = r.listen(source)
    
        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            print("Google Web Speech APIは音声を認識できませんでした。")
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
                " {0}".format(e))
        else:
            global currentmode
            currentmode = text
            print(text+"!!!!!!!!!!")
            if currentmode in loginUserdata['mode']:
               print("succsess") 
               global currentBind
               currentBind = loginUserdata['mode'][currentmode]
               print(currentBind)
               break
            else :
                print("もう一度だ...")

def BindLisner(User,mode):
    #メインスレッド
    print(User+":"+mode+"実行中")
    global currentUser
    global currentmode
    global currentBind
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("実行中")
            audio = r.listen(source)
    
        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            print("Google Web Speech APIは音声を認識できませんでした。")
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
                " {0}".format(e))
        else:
            print(text)
            if text =="終わりだよ":
                print("終了。")
                break
            elif text == "ユーザー変更": 
                print("ユーザ変更")
                currentUser='admin'
                currentmode="default"
                currentBind = None
                recognition()
                setmode(loginUserdata)
            elif text == "モード変更": 
                print("モード変更")
                currentmode="default"
                currentBind = None
                setmode(loginUserdata)
            elif text in currentBind:
                print(text)
                setOnomatope(currentBind,text)
            print(currentBind)

def setOnomatope(modex,text):
    #バインドマッチング
    keyPushFunc(modex[text])

def keyPushFunc(listx):
    #マクロの実行部分
    for k in listx:
        print(k)
        if 'hotkey' in k:
            pyautogui.hotkey(*k['hotkey'])
        elif 'write' in k:
            pyautogui.write(k['write'])
        elif 'press' in k:
            pyautogui.press(k['press'])

#設定
recognition()
setmode(loginUserdata)
BindLisner(currentUser,currentmode)