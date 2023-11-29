def find_cargo():
    total_weight = 713
    box_weights = [0, 0, 0]
    
    while True:
        for i in range(3):
            kilometer_mark = int(input(f"Enter the kilometer mark for box {i + 1}: "))
            box_weights[i] = int(input(f"Enter the weight buried at {kilometer_mark} km for box {i + 1}: "))

        if sum(box_weights) == total_weight:
            print("Congratulations! You found all the boxes.")
            break
        else:
            print("Oops! The total weight of the boxes is not 713. Try again.")

if __name__ == "__main__":
    print("Welcome to the Martian Cargo Finder!")
    print("Enter the kilometer marks and weights to find the buried cargo.")
    find_cargo()
