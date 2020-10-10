x = "y"

def average(list):
    print(list)
    return sum(list) / len(list)

while x == "y":
    numbers = input("Please input your numbers separated by a comma (i.e., x, y, z...): ")
                        
    nums = numbers.split(',')

    nums = [int(n) for n in nums]
                        
    print(f"{average(nums)}")
    
    x = input("Would you like to enter more numbers? Type (y)es or (n)o: ")

print("Thank you for using Average calculator!")