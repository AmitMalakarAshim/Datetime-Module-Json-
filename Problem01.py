import datetime #datetime module import 

current_time = datetime.datetime.now() 
current_date_and_time = current_time.strftime("%d/%m/%Y, %I:%M:%S %p")  #time formating 

print(f"Current Date & Time: {current_date_and_time}") # show the output  
