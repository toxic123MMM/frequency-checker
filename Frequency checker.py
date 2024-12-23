test_dict={'I':9,'love':9,'icecream':9,'and':2,'Milkshakes':1}
print("the dictionary: "+str(test_dict))
M=9
res=0
for key in test_dict:
    if test_dict[key]==M:
        res=res+1
print("frequency of M is: "+str(res))