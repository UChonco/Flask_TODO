names = "C:/Users/Admin/Desktop/Names.txt"
output ="C:/Users/Admin/Desktop/output.txt"

#Reading file and display
with open(names, 'r') as file:
    text = file.read()
    wordCount = len(text.split())
    print(text)
    print("Word count: " ,wordCount)

#Writing to a 
with open(output, 'w') as file:
    line1 = file.write('Careers IT \n')
    line2 = file.write('System developers \n')
    line3 = file.write('Assessor - Mr Masiya ')
    file.close()
