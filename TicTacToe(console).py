def cell():
    for cell in Area:
        print(cell)    
Area=[["*","*","*"],["*","*","*"],["*","*","*"]]
Turns=True
cell()
for turn in range(1,10):
    print(f"Turn: {turn}")
    row=int(input("Enter the row: "))
    print(row)
    row=row -1
    collumn=int(input("Enter the collumn: "))
    print(collumn)
    collumn=collumn -1
    if Turns == True:
        turn_char="X"
        Turns=False
        print("X's turn:")
    else:
        turn_char="0"
        Turns=True
        print("0's turn:")
    
    Area[row][collumn]=turn_char
    cell()
    if Area[0][0] == "X" and Area[0][1] == "X" and Area[0][2] == "X":
        print("X won!")
        break
    if Area[1][0] == "X" and Area[1][1] == "X" and Area[1][2] == "X":
        print("X won!")
        break
    if Area[2][0] == "X" and Area[2][1] == "X" and Area[2][2] == "X":
        print("X won!")
        break


    if Area[0][0] == "0" and Area[0][1] == "0" and Area[0][2] == "0":
        print("0 won!")
        break
    if Area[1][0] == "0" and Area[1][1] == "0" and Area[1][2] == "0":
        print("0 won!")
        break
    if Area[2][0] == "0" and Area[2][1] == "0" and Area[2][2] == "0":
        print("0 won!")
        break

    if Area[0][0] == "X" and Area[1][0] == "X" and Area[2][0] == "X":
        print("X won!")
        break
    if Area[0][1] == "X" and Area[1][1] == "X" and Area[2][1] == "X":
        print("X won!")
        break
    if Area[0][2] == "X" and Area[1][2] == "X" and Area[2][2] == "X":
        print("X won!")
        break

    if Area[0][0] == "0" and Area[1][0] == "0" and Area[2][0] == "0":
        print("0 won!")
        break
    if Area[0][1] == "X" and Area[1][1] == "0" and Area[2][1] == "0":
        print("0 won!")
        break
    if Area[0][2] == "0" and Area[1][2] == "0" and Area[2][2] == "0":
        print("0 won!")
        break

    if Area[0][0] == "X" and Area[1][1] == "X" and Area[2][2] == "X":
        print("X won!")
        break
    if Area[0][2] == "X" and Area[1][1] == "X" and Area[2][0] == "X":
        print("X won!")
        break

    if Area[0][0] == "0" and Area[1][1] == "0" and Area[2][2] == "0":
        print("0 won!")
        break
    if Area[0][2] == "0" and Area[1][1] == "0" and Area[2][0] == "0":
        print("X won!")
        break
    
    
   
