# try:
#     f = open('simple.txt','r')
#     f.write("Test write to simple text!")
# except:
#     print("ERROR: COULD NOT FIND FILE OR READ DATA!")
# else:
#     print("Success!")
#     f.close()
# print("hello world!")


# f = open('simple.txt','r')
# f.write("Test write to simple text!")
# print("hello world!")


try:
    f = open('simple.txt','w')
    f.write("Test write to simple.txt file!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")