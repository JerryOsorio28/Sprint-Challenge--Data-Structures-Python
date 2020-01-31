import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = [name for name in names_1 if name is name in names_2] #ALL HAIL LIST COMPREHENSIONS! :D
# --------------------------------------------------------
# INITIAL PROBLEM TO IMPROVE - RUN TIME COMPLEXITY = QUADRATIC TIME!
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# # -------------------------------------------------------- SO MUCH WORST XD
# duplicates = []
# def find_dups(names1, names2, first_index=0, second_index=0):
#     done = False
#     while not done:
#         if names1[first_index] is names2[second_index]:
#             duplicates.append(names1[first_index])
#         second_index += 1
#         if names2[second_index] is names2[-1]:
#             second_index = 0
#             first_index += 1
#         if names1[first_index] is names1[-1]:
#             done = True
#     return duplicates
# find_dups(names_1, names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
