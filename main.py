print("List Generator")
print()
start_num = int(input("What is the starting number? "))
end_num = int(input("What is the end number? "))
increment = int(input("What is the increment? "))

for i in range(start_num, end_num, increment):
  print(i)