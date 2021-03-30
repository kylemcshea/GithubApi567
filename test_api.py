from unittest import mock
import githubApi


def use_simple_function():
    result = githubApi.main('kylemcshea')
    print(result)


@mock.patch('githubApi.main')
def mock_simple_function(mock_simple_func):
    result = githubApi.main('kylemcshea')
    print(result)


mock_simple_function()
