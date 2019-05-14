def twofer(who='you'):
    return f'One for {who}, one for me'

def limerick():
  lim_list = ['Był skrzypek rodem z Prabutów,',
              'miał nogi za duże do butów.',
              'Wszystkie go uwierały,',
              'więc nosił futerały',
              'od skrzypiec zamiast butów.']
  for line in lim_list:
      print(line)

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
    while True:
        name = input('Give me your name: ')
        twofer(name)
        shall_continue = input('Print again?')
        if shall_continue.lower() != 'y':
            break