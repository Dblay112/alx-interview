#!/usr/bin/python3
"""
Prime Game
"""


def remove_multiples(num, numbers):
    """
    Remove multiples of a given number from a list.

    Parameters:
        num (int): The number whose multiples need to be removed.
        numbers (list): The list from which multiples
        of the given number are to be removed.

    Returns:
        list: The list after removing the multiples of the given number.
    """
    return [i for i in numbers if i % num != 0]


def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
        number (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number == 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def count_primes(number_set):
    """
    Count the number of prime numbers in a given set and remove
    prime numbers and their multiples from the set.

    Parameters:
        number_set (set): The set of numbers from which prime numbers
        and their multiples are to be removed.

    Returns:
        int: The count of prime numbers.
    """
    primes_count = 0
    numbers_list = list(number_set)
    for i in range(1, len(numbers_list) + 1):
        if is_prime(i):
            primes_count += 1
            numbers_list = remove_multiples(i, numbers_list)
    return primes_count


def isWinner(x, nums):
    """
    Parameters:
        x (int): The number of rounds to be played.
        nums (list): The list of integers representing the upper
        bounds of the ranges for each round.

    Returns:
        str: The name of the winner (Maria or Ben) for each round,
        or None if it's a tie.
    """
    players = {'Maria': 0, 'Ben': 0}
    for upper_bound in nums:
        number_set = set(range(1, upper_bound + 1))
        prime_count = count_primes(number_set)
        if prime_count % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
