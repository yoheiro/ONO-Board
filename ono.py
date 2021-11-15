import speech_recognition as sr
import pyautogui 
import time
import tkinter as tk
import addGUI
import pickle




def saveCSV(saveData):
    with open('data.json', 'wb') as fp:
        pickle.dump(saveData, fp)
    
def loadCSV():
    with open('data.json', 'rb') as fp:
        newdata = pickle.load(fp)
    return newdata
user_data = [{'Name':'髙木','mode':{'プログラミング':{'ペタペタ':[{'hotkey':['ctrl','c']},{'write':'hallow'}],
                                                    'ジャバジャバ':[{'write':'    public static void main(String[] args) {'},{'press':'enter'},{'write':'     System.out.println("Hello World");  }'}]},
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
resetdata={'Name':'髙木','mode':{'プログラミング':{'ペタペタ':[{'hotkey':['ctrl','c']},{'write':'hallow'}],
                                                    'ジャバジャバ':[{'write':'    public static void main(String[] args) {'},{'press':'enter'},{'write':'     System.out.println("Hello World"); '},{'press':'enter'},{'write':'    }'}]},
                                    'デスクトップ':{'ペタペタ':[],
                                                    'じゃばじゃば':[]
                                                    }
                                    }
             }
        #ログイン後取得予定データの例
loginUserdata=loadCSV()
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
            print("敵は一人...お前も一人。何を畏れる必要がある・・・恐怖を捨てろ・・・前を見ろ・・・進め・・・決して立ち止まるな・・・！もう一度だ..")
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
               break
            elif currentUser=="リセット":
                saveCSV(resetdata)
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
            print("モードは！！")
            audio = r.listen(source)
    
        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            print("敵は一人...お前も一人。何を畏れる必要がある・・・恐怖を捨てろ・・・前を見ろ・・・進め・・・決して立ち止まるな・・・！もう一度だ..")
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
                " {0}".format(e))
        else:
            global currentmode
            currentmode = text
            print(text+"!!!!!!!!!!")
            if currentmode in loginUserdata['mode']:
               global currentBind
               currentBind = loginUserdata['mode'][currentmode]
               print(currentBind)
               break
            elif text == "モード 登録":
                
                loginUserdata = addGUI.addMode(loginUserdata)
                saveCSV(loginUserdata)
                print(loginUserdata)
            else :
                print("もう一度だ...")

def BindLisner(User,mode):
    #メインスレッド
    print(User+":"+mode+"実行中")
    global currentUser
    global currentmode
    global currentBind
    global loginUserdata
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("実行中")
            audio = r.listen(source)
    
        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            print("敵は一人...お前も一人。何を畏れる必要がある・・・恐怖を捨てろ・・・前を見ろ・・・進め・・・決して立ち止まるな・・・！もう一度だ..")
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
            elif text == "モード 変更": 
                print("モード 変更")
                currentmode="default"
                currentBind = None
                setmode(loginUserdata)
            elif text == "オノマトペ 登録":
                loginUserData=loginUserdata
                loginUserdata = addGUI.addBind(loginUserData,currentmode)
                currentBind = loginUserdata['mode'][currentmode]
                saveCSV(loginUserdata)
            elif text in currentBind:
                setOnomatope(currentBind,text)
            print(currentBind.keys())

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
