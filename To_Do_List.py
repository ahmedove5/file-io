


y_or_n= input("do you want to add a new:")

while y_or_n == "y"or "n"or "exit":
      
    if y_or_n=="y":
        f=input("type in his new To-Do item")
    
        write_in_file =open('TO_DO.txt',"w", encoding="utf-8")
        write_in_file.write(f)
        write_in_file.close
        break
    elif y_or_n == "n":
        t=input("do you want to list your To-Do items ?")
          
        if t=="y":
             read_in_file =open('TO_DO.txt',"r", encoding="utf-8")
             print(read_in_file.read())
             read_in_file.close
             break
             
    if y_or_n == "exit":
     print("thankyou")
     break
            
               



     


    

    