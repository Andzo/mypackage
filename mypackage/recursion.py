def sum_array(array):
    '''
    Returns the sum of all items in array.

    Args:
        array (array): array containing numerical values.

    Returns:
        numerical value: the sum of all items in array.

    Examples:
        >>> sum_array([1,2,3,4])
        10
        >>> sum_array([4,-2,0,2.5])
        4.5
    '''
    sum = 0

    for i in array:
        sum += i #Add values in array
    return sum

def fibonacci(n):
    '''
    Return nth term in fibonacci sequence.

    Args:
        n (numerical value): the index of the n_th fibonacci sequence
    Returns:
        numerical value: nth term in fibonacci sequence.

    Examples:
        >>> fibonacci(4)
        3
        >>> fibonacci(12)
        144
    '''
    if (n < 0):
        raise ValueError('"n" must be non-negative!')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):
    '''
    Return n!

    Args:
        n (numerical value): must be an integer.
    Returns:
        numerical value: the n_th factorial.

    Examples:
        >>> factorial(4)
        24
        >>> fibonacci(1)
        1
    '''
    if (n < 0 or (type(n) != int)):
        raise ValueError('"n" must be a non-negative integer!')
    elif (n == 0 or n == 1):
        return 1
    return factorial(n-1)*n

def reverse(word):
    '''
    Return word in reverse!

    Args:
        word (string value): the word that must be reversed.
    Returns:
        string: word in reverse!

    Examples:
        >>> reverse('hello')
        'olleh'
        >>> reverse('madam')
        'madam'
    '''
    reversed_word = ''
    for i in (range(len(word))):
        reversed_word += word[-(1+i)]
    return reversed_word
