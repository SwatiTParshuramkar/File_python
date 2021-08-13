my_file3 = open("QUESTION3.txt", "w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
my_file3.write("banks_list")
i=0
while i <len(banks_list):
    my_file3.write(banks_list[i])
    my_file3.write("\n")
    i+=1
my_file3.close()