from itertools import zip_longest 
  
test_list = [1,0,0,0,1] 
  
#print ("The original list is : " + str(test_list)) 
  
res = [i for i, j in zip_longest(test_list, test_list[1:]) 
                                                if i != j] 
  
print (str(res))