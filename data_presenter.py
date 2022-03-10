#2
open_file = open("CupcakeInvoices.csv")


#3
# for file in open_file:
#     print(file)
    
#4
grand_total = 0

open_file_list = []
for file in open_file:
    file = file.rstrip('\n').split(',')
    open_file_list.append(file)

for type in open_file_list:
    print(type[2])
    #5
    total = int(type[3]) * float(type[4])
    print(f"Total: {total}" )

    #6
    grand_total += total 

print(grand_total)


#7
open_file.close()