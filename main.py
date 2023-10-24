name = "Test_name"
first_word=name[0:7:1]
last_word=name[5:9]
step=name[::2]
print(first_word)
print(last_word)
print(step)

reversed_name=name[-3:-10:-1]
print(reversed_name)

website="http://google.com"
website2="http://wikipedia.com"
slice_var=slice(7,-4)
print(type(slice_var))
print(str(slice_var))
website=website[slice_var]
print(website)
print(website2[slice_var])