print("=== kids quiz game ===")
name = input("enter your name:")
score =0

q1 = input("1.4 + 5 = ?")
if q1 == "9":
    score += 1
    print("correct! great gop!")
q2 = input("2. 10 - 3 = ?")
if q2 =="7":
    score += 1
    print("correct! great gop!")
    
print(f"Done {name}! your score : {score}/2")
