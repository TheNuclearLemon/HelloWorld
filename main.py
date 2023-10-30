# def hello(**kwargs):
#     print("Hello " + kwargs['first'] + " | " + kwargs['middle'] + " | " + kwargs['last'])
#
# hello(first="First_name",last="Last_name",middle="Middle_name")

def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
hello(title="Mister", first="First_name",last="Last_name",middle="Middle_name")
