line = "My sentence! Is awesome?"
#make a dictionary of values
dic = {"a":1,
       "b":2,
       "c":3,
       }

output_message = [dic.get(n, n) for n in line]
print(output_message)
