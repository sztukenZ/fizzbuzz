def fizzbuzz():
    for i in range(1,101):
        if not i % 3 and not i % 5:
            print('fizzbuzz')
        if not i % 3:
            print('fizz')
        elif not i % 5:
            print('buzz')

        else:
            print(i)

if __name__ == '__main__':
    fizzbuzz()