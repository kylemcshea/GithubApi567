# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from githubApi import grabRepoList

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class testGithubApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testApi(self):
        self.assertEqual(grabRepoList('kylemcshea'), ['breezMusic has 11 commits', 'CS-115 has 2 commits', 'demo-grow has 1 commits', 'ExpressIntro has 1 commits', 'GAITERS has 12 commits', 'GAITERS_Dashboard has 5 commits', 'GithubApi567 has 3 commits', 'Hangman_Learning_Bio has 30 commits', 'Homework3_SSW_345 has 2 commits', 'homework_3 has 1 commits', 'insta-scraper has 2 commits', 'Jackson_Portfolio has 7 commits',
                         'kylemcshea.github.io has 12 commits', 'learnGitBranching has 30 commits', 'ModsWithJava has 1 commits', 'Multiplayer-Pac-Man has 1 commits', 'portfolio has 30 commits', 'portfolio-page has 2 commits', 'practice-react has 1 commits', 'react-js-tutorials has 30 commits', 'react-product-card has 30 commits', 'React-QuizComponent has 30 commits', 'SSW--567 has 19 commits', 'Triangle567 has 7 commits'], 'kylemcshea does not work')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
