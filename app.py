import tkinter, os
from tkinter import *
 
def temp(string):
  temp=tkinter.Frame(string,width=20,height=50)
  temp.pack()
 
flag=0
node=0
def num_work():   #更新顯示框Lable
  global flag
  global node
  with open("D:\\num.txt") as f:
    for length in f:
      string=length
  top_work.configure(text=string.strip('\n'))  # 重新設定標籤文字
  root.after(500,num_work) # 每隔0.5s呼叫函式num_work自身獲取結果
 
def num_math_int(num1,num2):#整數運算
  try:
    if num2[0]=='+':
      string=int(num1)+int(num2[1:])
    elif num2[0]=='-':
      string=int(num1)-int(num2[1:])
    elif num2[0]=='x':
      string=int(num1)*int(num2[1:])
    elif num2[0]=='/':
      string=int(num1)/int(num2[1:])
       
    with open("D:\\num.txt",'a') as f:
      f.write('\n'+str(string)+'\n')
  except:
    with open("D:\\num.txt",'a') as f:
        f.write('\n錯誤')
def num_math_float(num1,num2):#小數運算
  try:
    if num2[0]=='+':
      string=float(num1)+float(num2[1:])
    elif num2[0]=='-':
      string=float(num1)-float(num2[1:])
    elif num2[0]=='x':
      string=float(num1)*float(num2[1:])
    elif num2[0]=='/':
      string=float(num1)/float(num2[1:])
    if flag==0:
      with open("D:\\num.txt",'a') as f:
        f.write('\n'+str(string)+'\n')
    else:
      with open("D:\\num.txt",'a') as f:
        f.write('\n'+str(string))
  except:
    with open("D:\\num.txt",'a') as f:
        f.write('\n錯誤')
        
def decimal(num):
  if num.count('%')>0:
    num=num.replace('%','')
    num=num.replace('\n','')
    if num.isnumeric():
      num=str(float(num)/100)
    else:
      num=num[0]+str(float(num[1:])/100)
  return num
     
def work(string):#按鍵對應的功能
  if string.isnumeric():
    with open("D:\\num.txt","a") as file:
      file.write(string)
  else:
    #讀取檔案D:\\num.txt所有內容
    lists=[]
    with open("D:\\num.txt","r") as file:
      for length in file:
        lists.append(length)
           
    if string=='AC':
      with open("D:\\num.txt","w") as file:
        file.write('0.0\n')
         
    elif string=='=':
      num1=lists[-2]
      num2=lists[-1]
      if num1=='\n':#解決末尾為換行的情況
        num1=lists[-3]
         
      #將百分數小數化
      #出現結果多0.0000000001
      num1=decimal(num1)
      num2=decimal(num2)
         
      try:      #判斷兩個數是整數還是小數
        number=int(num1)
        number=int(num2[1:])
        num_math_int(num1,num2)#兩個數進行整數運算
      except:
        num_math_float(num1,num2)#兩個數進行小數運算
         
    elif string=='.':
      if lists[-1].count('.')==0:#判斷結尾是否有小數點，沒有寫入否則報錯
        with open("D:\\num.txt","a") as file:
          file.write(string)
      else:
        with open("D:\\num.txt","a") as file:
          file.write('\n錯誤')
           
    elif string=='+/-':
      if lists[-1].count('-')==0:#-+為-
        if lists[-1].count('+')==1:
          lists[-1]=lists[-1].replace('+','')
        lists[-1]='-'+lists[-1]
      else:           #--為+
        lists[-1]=lists[-1].replace('-','+')
      #更新檔案
      with open("D:\\num.txt","w") as file:
        pass
      for length in lists:
        with open("D:\\num.txt","a") as file:
          file.write(length)
           
    elif string=='delete':
      number=lists[-1]
      lists[-1]=number[0:(len(number)-1)]#刪除一位
      #更新檔案
      with open("D:\\num.txt","w") as file:
        pass
      for length in lists:
        with open("D:\\num.txt","a") as file:
          file.write(length)
    elif string=='%':
      if lists[-1].endswith("%")==False:
        with open("D:\\num.txt","a") as file:
          file.write(string)
      else:
        with open("D:\\num.txt","a") as file:
          file.write('\n錯誤')
       
    else:
      with open("D:\\num.txt","a") as file:
        file.write('\n'+string)
   
def run():#計算器顯示介面主體
  if os.path.exists("D:\\num.txt")==False:
    with open("D:\\num.txt",'w') as f:
      f.write('0.0\n')
  global root#定義全域性變數root,方便Label更新
  root=tkinter.Tk()
  root.title("計算器")
   
  #x = root.winfo_screenwidth()
  #獲取當前螢幕的寬
  #y = root.winfo_screenheight()
  #獲取當前螢幕的高
  #print(((x-500)//2),((y-600)//2))#為居中提供的引數
   
  root.geometry('400x500+760+290')#主體長400，高500，居中
  top=tkinter.Frame(root,width=20,height=50)
  top.pack()
 
  global top_work#定義全域性變數root
  temp(top)#空白間隔
  #計算器顯示框
  top_work=tkinter.Label(top,text='',justify='left',relief=SUNKEN,bd=10,bg='white',width=40)
  top_work.pack(side='bottom')#計算器顯示框（位置居下）
  num_work()
  temp(root)#空白間隔
   
  number=tkinter.Frame(root)#成放計算機鍵盤的容器
  number.pack()
  #所有按鍵，AC鍵為事例
  numberAC=tkinter.Button(number,text="AC",width=10,command=lambda : work('AC')).grid(row=0,column=0)
  #左鍵點選，執行函式work
  #按鍵位置（0,0）
   
  numberdelete=tkinter.Button(number,text="delete",width=10,command=lambda : work('delete')).grid(row=0,column=1)
  numberzhengfu=tkinter.Button(number,text="+/-",width=10,command=lambda : work('+/-')).grid(row=0,column=2)
  numberchu=tkinter.Button(number,text="/",width=10,command=lambda : work('/')).grid(row=0,column=3)
   
  tkinter.Button(number,text="7",width=10,command=lambda : work('7')).grid(row=1,column=0)
  tkinter.Button(number,text="8",width=10,command=lambda : work('8')).grid(row=1,column=1)
  tkinter.Button(number,text="9",width=10,command=lambda : work('9')).grid(row=1,column=2)
  tkinter.Button(number,text="x",width=10,command=lambda : work('x')).grid(row=1,column=3)
   
  tkinter.Button(number,text="4",width=10,command=lambda : work('4')).grid(row=2,column=0)
  tkinter.Button(number,text="5",width=10,command=lambda : work('5')).grid(row=2,column=1)
  tkinter.Button(number,text="6",width=10,command=lambda : work('6')).grid(row=2,column=2)
  tkinter.Button(number,text="-",width=10,command=lambda : work('-')).grid(row=2,column=3)
   
  tkinter.Button(number,text="1",width=10,command=lambda : work('1')).grid(row=3,column=0)
  tkinter.Button(number,text="2",width=10,command=lambda : work('2')).grid(row=3,column=1)
  tkinter.Button(number,text="3",width=10,command=lambda : work('3')).grid(row=3,column=2)
  tkinter.Button(number,text="+",width=10,command=lambda : work('+')).grid(row=3,column=3)
   
  tkinter.Button(number,text="%",width=10,command=lambda : work('%')).grid(row=4,column=0)
  tkinter.Button(number,text="0",width=10,command=lambda : work('0')).grid(row=4,column=1)
  tkinter.Button(number,text=".",width=10,command=lambda : work('.')).grid(row=4,column=2)
  tkinter.Button(number,text="=",width=10,command=lambda : work('=')).grid(row=4,column=3)
 
  root.mainloop()
if __name__=='__main__':
  run()
