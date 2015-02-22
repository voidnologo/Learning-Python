# Trivia Challenge
# trivia game that reads a plain text file for questions

#pg 212

import sys

def open_file(file_name, mode):
    try:
        return open(file_name, mode)
    except IOError as e:
        print('Unable to open the file', file_name, 'Ending program.\n', e)

def next_line(the_file):
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explaination = next_line(the_file)

    return category, question, answers, correct, explaination

def welcome(title):
    print('\t\tWelcome to trivia challenge\n')
    print('\t\t', title, '\n')

def main():
    trivia_file = open_file('trivia.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    category, question, answers, correct, explaination = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print('\t', i + 1, '-', answers[i])

        answer = input('What\'s your answer?: ')

        if answer == correct:
            print('\nRight!', end=' ')
            score += 1
        else:
            print('\nWrong.', end=' ')
        print(explaination)
        print('Score:', score, '\n\n')

        category, question, answers, correct, explaination = next_block(trivia_file)

    trivia_file.close()

    print('That was the last question.')
    print('Your final score is', score)

main()
