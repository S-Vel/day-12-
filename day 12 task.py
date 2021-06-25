
f =open(r"30_days_30_hour_operations.txt","w+")

f.write("I have completed 12 days successfully")

f.close()

f1 =open(r"30_days_30_hour_operations.txt","a+") 
f1.writelines("Vel S")

f1 =open(r"30_days_30_hour_operations.txt","r") 
print(f1.read())

f1.close()