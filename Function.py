problems = list()
pbm1 = ''
pbm2 = ''
pbm3 = ''
pbm4 = ''
pbm5 = ''

pbmC = input("Type the number of problems: ")
try:
    pbmC = float(pbmC)
except:
    print("Error: Numbers must only contain digits.")
    exit()

if pbmC > 5:
    print("Error: Too many problems.")
    exit()

if pbmC >= 1:
    pbm1 = input("Enter the problem: ")
    problems.append(pbm1)
    if pbmC >= 2:
        pbm2 = input("Enter the second problem: ")
        problems.append(pbm2)
        if pbmC >= 3:
            pbm3 = input("Enter the third problem: ")
            problems.append(pbm3)
            if pbmC >= 4:
                pbm4 = input("Enter the fourth problem: ")
                problems.append(pbm4)
                if pbmC >= 5:
                    pbm5 = input("Enter the fifth problem: ")
                    problems.append(pbm5)

print(problems)
