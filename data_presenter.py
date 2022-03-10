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

    #6
    grand_total += total 

print(f"Total: {grand_total}")

#Part 3 go further
total_choc = 0.0
total_vanilla = 0.0
total_strawberry = 0.0

for flavor in open_file_list:
    single_order_total = int(flavor[3]) * float(flavor[4])

    if flavor[2] == "Chocolate":
        total_choc += single_order_total
    elif flavor[2] == "Strawberry":
        total_strawberry = total_strawberry + total
    elif flavor[2] == "Vanilla":
        total_vanilla += total

print(f"The totals for each flavor were; Chocolate: {total_choc}, Straberry: {total_strawberry}, Vanilla: {total_vanilla}")

#7
open_file.close()