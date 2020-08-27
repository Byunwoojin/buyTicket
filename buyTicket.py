import easygui

easygui.msgbox("Welcome to buy lunch ticket!\n(Lunch : 11:00~15:00)")
choice=['Korean dish','Western dish',"Chinese's style","Japanese","Exit"]
reply=easygui.buttonbox("Choose lunch menu to buy",choices=choice)
while reply!="Exit":
    if reply=='Korean dish':
        k_num=easygui.enterbox("Korean dish is 2500 won.\nHow many tickets do you want to buy?")
        k_num=int(k_num)
    elif reply=='Western dish':
        w_num=easygui.enterbox("Western dish is 3000 won.\nHow many tickets do you want to buy?")
        w_num=int(w_num)
    elif reply=="Chinese's style":
        c_num=easygui.enterbox("Chinese food is 2000 won.\nHow many tickets do you want to buy?")
        c_num=int(c_num)
    elif reply=="Japanese":
        j_num=easygui.enterbox("Japanese food is 3500 won.\nHow many tickets do you want to buy?")
        j_num=int(j_num)
    reply=easygui.buttonbox("Choose lunch menu to buy",choices=choice)
    
total_num=(k_num*2500)+(w_num*3000)+(c_num*2000)+(j_num*3500)
easygui.msgbox("Total amount to pay : "+str(total_num)+"\nThanks for using!")
        

    

               
