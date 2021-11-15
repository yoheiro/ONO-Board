import speech_recognition as sr
import pyautogui 
import time
import tkinter as tk

def getOnomatope():

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
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
            print("「"+text+"」")
            if text != None:
                break
            else :
                print("もう一度")
    
    return text

#GUI

def addBind(loginUserdata,currentmode):
    
    print("バインド登録")
    
    autoFillSet = {} #write + テキスト　→addListに入れる
    keySet = {} #hotkey + キー　→addListに入れる
    keyList = [] #キーの組み合わせ（キーイベントの格納先）→keySetに入れる
    addList = [] #→ラベル表示部分
    
    def register():
        newBind = {txtBox_rec.get(): addList}
        print(newBind)
        loginUserdata['mode'][currentmode].update(newBind)
        print(loginUserdata['mode'][currentmode])
        print("登録完了")
        
    
    def changedata():#音声認識をして文字を書き換える関数
        
        txtBox_rec.configure(state='normal')
        txtBox_rec.delete(0,tk.END)
        txtBox_rec.insert(tk.END,getOnomatope())
        txtBox_rec.configure(state='readonly')

        return
    
    def op_check():#登録操作の選択判別
        
        x=radioValue.get()
        
#         if (btn_ope['state'] == tk.NORMAL):
#             btn_ope['state'] = tk.DISABLED
#         else:
#             btn_ope['state'] = tk.DISABLED
        
        if x==1:
            
            def getTxt():
                
                txt_op1 = txtBox_op1.get()
                ono = txtBox_rec.get()
                
                value = tk.StringVar()
                value.set("write："+txt_op1)
                label_showTxt = tk.Label(master=root, font=(None,12), fg="red", textvariable=value)#取得したテキストの表示
                
                label_showTxt.place(x=850,y=220)
            
                save1(ono,txt_op1)       
                    
            def save1(ono,txt): 
                
                autoFillSet['write'] = txt
                addList.append(autoFillSet)
                txtBox_op1.delete(0,tk.END)
                
            label_op1 = tk.Label(root, text="自動入力させたい文字列を入力してください")
            label_op1.place(x=650,y=150)
            
            txtBox_op1 = tk.Entry()
            txtBox_op1.configure(state='normal', width=50)
            txtBox_op1.place(x=650,y=180) #操作テキストボックス表示
            
            btn_op1 = tk.Button(root, text="追加",width=15,command=getTxt)
            btn_op1.place(x=650,y=220)#追加ボタン表示
            
        elif x==2:
            
            #入力キー表示関数
            def input_key(event):
                key_name = event.keysym
                
                keyList.append(key_name) #リストに格納
                
                value.set("hotkey："+'&'.join(keyList))
                save2()
                
            def save2(): #currentUser,currentmode取得
                
                keySet['hotkey'] = keyList
                addList.append(keySet)
            
            # ラベル表示変数
            value = tk.StringVar()
             
            label_op2 = tk.Label(root, text="登録したいキーを押して下さい") 
            label_showKey = tk.Label(master=root, font=(None,12), fg="red", textvariable=value)#取得したキーイベントの表示
            
            label_op2.place(x=650,y=250)
            label_showKey.place(x=650,y=300)
            
            # キー入力時のイベント取得
            label_showKey.bind("<KeyPress>", input_key)
 
            # フォーカスセット
            label_showKey.focus_set()
    
    root = tk.Tk()
    root.title(u"オノマトペ登録")#タイトル
    root.geometry("1100x500")#ウィンドウサイズ
    label_rec = tk.Label(root, text="-------------------------登録する言葉--------------------------",font=("Helvetica",10,"bold"))  # ラベルを作成
    label_rec.place(x=300,y=10)  #表示
    
    txtBox_rec = tk.Entry()
    txtBox_rec.configure(state='readonly', width=50)
    txtBox_rec.place(x=200,y=50) #録音データ表示用テキストボックス
    
    btn_rec = tk.Button(root, text="録音",command=changedata,font=("Helvetica",10,"bold"))
    btn_rec.place(x=650,y=40)#録音ボタン表示
    
    label_op = tk.Label(root, text="-------------------------登録する操作-------------------------",font=("Helvetica",10,"bold"))  # ラベルを作成
    label_op.place(x=500,y=100) #ラベル表示
    
    radioValue = tk.IntVar() 
 
    op1 = tk.Radiobutton(root, text='テキストの自動入力',
                             variable=radioValue, value=1,font=("Helvetica",10,"bold")) #選択肢１
    op2 = tk.Radiobutton(root, text='キーを押す操作',
                             variable=radioValue, value=2,font=("Helvetica",10,"bold")) #選択肢２

    op1.place(x=500,y=150)
    op2.place(x=500,y=250)
    
    list_var = tk.StringVar(value=addList) #addListの表示
    listbox = tk.Listbox(root, height=10,width=40, listvariable=list_var)
    listbox.place(x=100,y=150) 

    btn_ope = tk.Button(root, text="選択",width=15,command=op_check,font=("Helvetica",10,"bold")) 
    btn_ope.place(x=500,y=350)#操作選択ボタン表示
    
    btn_register = tk.Button(root, text="登録",width=15,command=register,font=("Helvetica",10,"bold")) 
    btn_register.place(x=800,y=450)#操作登録ボタン表示

    root.mainloop()#ウインドウ表示


def addMode(loginUserdata):
    
    print("モード名を言って下さい")
    text = getOnomatope()
    newMode = {text:None}
    loginUserdata['mode'].update(newMode)
    print(loginUserdata['mode'])
    return loginUserdata

