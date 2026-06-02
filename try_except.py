
def main():
   x=try_integer()
   print(f"You have successfully input a value for X. That is {x}")
   
def try_integer():
    while True:
         try:
            x=int(input(("Enter an integer for x: ")))
        
         except ValueError:
            print("Invalid input! Please enter an integer. ") #Or use 'pass' keyword to ignore this error without displaying anything.
         else:
          return x
       
if __name__=="__main__": 
         main()

    
   

   
 
 
