username = "HarshMuskan"

def func():
    # username = "Priti"
    msg = "hello " + username +"! Welcome to the world of Python."
    print(msg)


print(username)  # Output: HarshMuskan
func()  # Output: helloPriti! Welcome to the world of Python.


def chai_maker(num):
    def actual(x):
        return x ** num
    return actual

chai_tea = chai_maker(5)
chai_mashala = chai_maker(10)

print(chai_tea(2))  # Output: 32
print(chai_tea(3))  # Output: 243
print(chai_mashala(2))  # Output: 1024
print(chai_mashala(3))  # Output: 59049