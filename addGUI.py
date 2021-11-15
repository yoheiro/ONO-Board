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
            print("Google Web Speech APIは音声を認識できませんでした。")
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

def addBind():
    
    print("バインド登録")
    
    autoFillSet = {} #write + テキスト　→addListに入れる
    keySet = {} #hotkey + キー　→addListに入れる
    keyList = [] #キーの組み合わせ（キーイベントの格納先）→keySetに入れる
    addList = [] #→ラベル表示部分
    
    def register():
        
        print("登録処理")
    
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
                
                label_showTxt.pack()
            
                save1(ono,txt_op1)       
                    
            def save1(ono,txt): 
                
                autoFillSet['write'] = txt
                addList.append(autoFillSet)
                
                print(addList)
                
            label_op1 = tk.Label(root, text="\n自動入力させたい文字列を入力してください")
            label_op1.pack()
            
            txtBox_op1 = tk.Entry()
            txtBox_op1.configure(state='normal', width=50)
            txtBox_op1.pack() #操作テキストボックス表示
            
            btn_op1 = tk.Button(root, text="追加",width=30,command=getTxt)
            btn_op1.pack()#追加ボタン表示
            
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
                print(addList)
            
            # ラベル表示変数
            value = tk.StringVar()
             
            label_op2 = tk.Label(root, text="\n登録したいキーを押して下さい") 
            label_showKey = tk.Label(master=root, font=(None,12), fg="red", textvariable=value)#取得したキーイベントの表示
            
            label_op2.pack()
            label_showKey.pack()
            
            # キー入力時のイベント取得
            label_showKey.bind("<KeyPress>", input_key)
 
            # フォーカスセット
            label_showKey.focus_set()
    
    root = tk.Tk()
    root.title(u"オノマトペ登録")#タイトル
    root.geometry("1000x500")#ウィンドウサイズ
    label_rec = tk.Label(root, text="-------------------------登録する言葉--------------------------")  # ラベルを作成
    label_rec.pack()  #表示
    
    txtBox_rec = tk.Entry()
    txtBox_rec.configure(state='readonly', width=50)
    txtBox_rec.pack() #録音データ表示用テキストボックス
    
    btn_rec = tk.Button(root, text="録音",command=changedata)
    btn_rec.pack()#録音ボタン表示
    
    label_op = tk.Label(root, text="\n-------------------------登録する操作-------------------------")  # ラベルを作成
    label_op.pack() #ラベル表示
    
    radioValue = tk.IntVar() 
 
    op1 = tk.Radiobutton(root, text='テキストの自動入力',
                             variable=radioValue, value=1) #選択肢１
    op2 = tk.Radiobutton(root, text='キーを押す操作',
                             variable=radioValue, value=2) #選択肢２

    op1.pack()
    op2.pack()
    
    list_var = tk.StringVar(value=addList) #addListの表示
    listbox = tk.Listbox(root, height=3, listvariable=list_var)
    listbox.pack() 

    btn_ope = tk.Button(root, text="選択",width=15,command=op_check) 
    btn_ope.pack()#操作選択ボタン表示
    
    btn_register = tk.Button(root, text="登録",width=15,command=register) 
    btn_register.pack()#操作登録ボタン表示

    root.mainloop()#ウインドウ表示  

#設定 メソッド呼び出し＝関数実行
addBind()