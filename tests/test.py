from mypackage import recursion
from mypackage import sorting

def test_sum_array():
    """
    making sure sum_array works correctly
    """
    assert recursion.sum_array([1,2,3,4]) == 10, 'incorrect'
    assert recursion.sum_array([4,-2,0,2.5]) == 4.5, 'incorrect'
    assert recursion.sum_array([0,0]) == 0, 'incorrect'

def test_fibonacci():
    """
    making sure fibonacci works correctly
    """
    assert recursion.fibonacci(4) == 3, 'incorrect'
    assert recursion.fibonacci(12) == 144, 'incorrect'

def test_factorial():
    """
    making sure factorial works correctly
    """
    assert recursion.factorial(4) == 24, 'incorrect'
    assert recursion.factorial(1) == 1, 'incorrect'

def test_reverse():
    """
    making sure reverse works correctly
    """
    assert recursion.reverse('hello') == 'olleh', 'incorrect'
    assert recursion.reverse('madam') == 'madam', 'incorrect'

def test_bubble_sort():
    '''making sure bubble_sort works correctly'''
    assert sorting.bubble_sort([3,6,2,78]) == [2,3,6,78], 'incorrect'
    assert sorting.bubble_sort(['r','a','f']) == ['a','f','r'], 'incorrect'

def test_merge_sort():
    '''making sure merge_sort works correctly'''
    assert sorting.merge_sort([3,6,2,78]) == [2,3,6,78], 'incorrect'
    assert sorting.merge_sort(['r','a','f']) == ['a','f','r'], 'incorrect'

def test_quick_sort():
    '''making sure quick_sort works correctly'''
    assert sorting.quick_sort([3,6,2,78]) == [2,3,6,78], 'incorrect'
    assert sorting.quick_sort(['r','a','f']) == ['a','f','r'], 'incorrect'
