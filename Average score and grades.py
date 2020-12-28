print("***************************************")
print("\tResult")
print("***************************************")
Eng=float(input("Enter the marks obtained in English:"))
while Eng:
    if Eng<0 or Eng>100:
      print("Error! Enter the marks again.")
      Eng=float(input("Enter the marks obtained in English:"))
    if Eng>0 and Eng <100:
        break
    else:
        continue

Mat=float(input("Enter the marks obtained in Mathematics:"))
while Mat:
    if Mat<0 or Mat>100:
      print("Error! Enter the marks again.")
      Mat=float(input("Enter the marks obtained in Mathematics:"))
    if Mat>0 and Mat<100:
        break
    else:
        continue

Sci=float(input("Enter the marks obtained in Science:"))
while Sci:
    if Sci<0 or Sci>100:
      print("Error! Enter the marks again.")
      Sci=float(input("Enter the marks obtained in Science:"))
    if Sci>0 and Sci<100:
        break
    else:
        continue

Soc=float(input("Enter the marks obtained in Social:"))
while Soc:
    if Soc<0 or Soc>100:
      print("Error! Enter the marks again.")
      Soc=float(input("Enter the marks obtained in Social:"))
    if Soc>0 and Soc<100:
        break
    else:
        continue

print("***************************************")
print("English:\t\t{}\nMathematics:\t\t{}\nScience:\t\t{}\nSocial:\t\t\t{}".format(Eng,Mat,Sci,Soc))


totalMarks=400
marksObtained=Eng+Mat+Sci+Soc
Average=(marksObtained/totalMarks)*100

print("***************************************")
print("\n\Total marks:\t\t{}\nTotal marks obtained:\t{}\nAverage:\t\t{}".format(totalMarks,marksObtained,Average))


if Average<95:
    print("Grade:\t\t\t A")

elif 90<Average and Average>94.99:
    print("Grade:\t\t\t B")

elif 80<Average and Average>89.99:
    print("Grade:\t\t\t C")

elif 70<Average and Average>70.99:
    print("Grade:\t\t\t D")

elif 35<Average and Average<70:
    print("Grade:\t\t\t E")

else:
    print("Grade:\t\t\t F")
print("***************************************")
