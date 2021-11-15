

import pickle

loginUserdata={'Name':'髙木','mode':{'プログラミング':{'ペタペタ':[{'hotkey':['ctrl','c']},{'write':'hallow'}],
                                                    'ジャバジャバ':[{'write':'    public static void main(String[] args) {'},{'press':'enter'},{'write':'     System.out.println("Hello World"); '},{'press':'enter'},{'write':'    }'}]},
                                    'デスクトップ':{'ペタペタ':[],
                                                    'じゃばじゃば':[]
                                                    }
                                    }
             }
with open('data.json', 'wb') as fp:
    pickle.dump(loginUserdata, fp)

with open('data.json', 'rb') as fp:
    data = pickle.load(fp)
print(data)
print(loginUserdata)