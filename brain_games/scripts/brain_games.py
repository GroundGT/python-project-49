#!/usr/bin/env python3
import prompt


def greet():
    print('Welcome to the Brain games')


def welcome_user() -> str:
    name = prompt.string('May I have your name? ')
    return f'Hello,{name}'


def main():
    greet()
    print(welcome_user())


if __name__ == '__main__':
    main()
