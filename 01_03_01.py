# FORMATING STRINGS

#variables
num1 = 78.5598746658
num2 = 8.85697423589
num3 = 856.854125441

# PREVIOUS METHOD
#print('num 1 will be',num1,' and num 2 would then be',num2,',num 3 would also be',num3)

#FORMAT METHOD
#print('num 1 will be {0:.5f} and num 2 would then be {1:.4f},num 3 would also be {2:.6f}'.format(num1,num2,num3))

#F-STRING METHOD
print(f'num 1 will be {num1:.4f} and num 2 would then be {num2:.4f} , num 3 would also be {num3:.4f}')