try:
    
    num = 20 / 5
   
except ZeroDivisionError:
    
    print("non si puo' dividere un numero per zero")
 
except TypeError:
    
    print("solo e' possibile dividere numeri interi")
    

    
else:
    
    print(f"La divisione tra i due numeri il risultato e' {num}")
    
finally:    
    
    print("questo si va a eseguire sempre")
    
    
##x = -5
#if x < 0:
    #raise Exception("non si posso utilizzare numeri negativi")



#try:
    
    int("Ciao a tutti")
    
#except:
    #print("questo non ha senso")    

