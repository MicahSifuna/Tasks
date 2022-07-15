i = None
y = 0
question = None
selection = True
quiz = True
career_choice = None
var = None


career_advices = ['Engineering is tough but you can manage',
                  'Medicine requires dedication and precision.',
                  'Anyone with interest in technology can do Computer Science',
                  'Justice-loving people say Law is worth it',
                  'Without teachers, no careers will be available',
                  'Being a soldier takes one to be courageous']

career_question = ['Will you manage to handle complex equation?',
                   'Can you be reliable in future?',
                   'Do you have passion in technology?',
                   'will you be just when conducting your cases?',
                   'will you be patient with your students?',
                   'are you ready to serve your nation and its people?']

choices_options = ['Engineering', 'Medicine',
                   'Computer Science', 'Law', 'Education', 'Military']


def career_quiz():
    for i in range(len(choices_options)):
        if i == (choices_options.index(choices_options[y])):
            print('\n', 'CAREER QUESTIONS\n', career_question[i], ': Y / N')
            question = input(' ').lower()
            quiz = True
            while quiz == True:
                if question == ('y') or question == ('yes'):
                    print(' Okay, your best selection of career is',
                          choices_options[i])
                    break
                    quiz = True
                else:
                    print(' You should check again your best options then')
                    for n in question:
                        choices()
                        if question == ('n') or question == ('no'):
                            break
                    break
                    quiz == False
            break
        elif i == (len(choices_options.index[y])-1):
            print('the career choice number is not available')


def choices(options=choices_options):
    print('Choose the career that you want to pursue: ')

    for x, element in enumerate(options):
        print("{}). {}".format(x + 1, element))

    try:
        i = int(input('Enter the choice number: '))
    except ValueError:
        print('ERROR: Choice Must Be A Number')
        choices(options)

    try:
        print(
            f'You have choosen {choices_options[i - 1]} an excellent choice!')
        print(f'Now, the ADVICE:\n{career_advices[i - 1]}')
    except IndexError:
        print('ERROR: Choice Must Be Between 1 and 6')
        choices(options)
    else:
        y = i


choices()
