mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num % 2 == 0

evens = filter(even_bool,mylist)
print(list(evens))


evens2 =filter(lambda num:num%2==0,mylist)
print(list(evens2))


st = 'hello'
st.lower()
st.upper()
st.split()

tweet = "Go Spports! #Sports"
result = tweet.split('#')
print(result)

print('x'in [1,2,3,4,'x'])
