# name = "Professional"
# print(name)
# char = name[0]
# print(char)
# print(name.replace("Professional", "Pro"))
# print(name)

# name = "safiullah the president of the ai here is not important to me to do there with nothting"




# name = ['p']*6
# print(name)





# from itertools import product
# a = [1,2]
# b = [3,4]
# prod = product(a,b, repeat=2)
# # prod = product(a,b)
# print(list(prod))


# from itertools import permutations
# a = [1,2,3]
# perm = permutations(a)
# # prod = product(a,b)
# print(list(perm))   






# from itertools import combinations
# a = [1,2,3]
# perm = combinations(a,2)
# print(list(perm))   








# from itertools import accumulate
# a = [1,2,3,4]
# acc = accumulate(a)
# print(a)
# print(list(acc))



from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i ==15:
        break