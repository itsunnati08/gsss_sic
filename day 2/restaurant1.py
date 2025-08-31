print('1:Idly 2:Dosa 3:Upma 4:Puri')
user_choice = int(input('Enter your choice of food: '))

match user_choice:
    case 1 : print('Soft Idly')
    case 2 : print('Crispy Dosa')
    case 3 : print('Hot and tasty Upma')
    case 4 : print('The crispy Puri')
    case _ : print('Sorry we do not have that item')