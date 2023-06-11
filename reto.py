def my_gen():
    for i in range(1, 101):
        if i % 2 == 0:
            yield i
        
my_first_gen = my_gen()

for i in range(50):
    print(next(my_first_gen))