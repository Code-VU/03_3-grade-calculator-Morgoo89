def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
try:
    score = float(input("Enter score:"))
    if score >= 0.9 and score <= 1.0:
        print("A")
    elif score >= 0.8 and score <= 0.9:
        print("B")
    elif score >= 0.7 and score <= 0.8:
        print("C")
    elif score >= 0.6 and score <= 0.7:
        print("D")
    elif score < 0.6 and score <= 0.6:
        print("F")
    else:
        print("Bad score")
except:
    print("Bad score")

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
