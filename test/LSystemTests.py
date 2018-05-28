#!/usr/bin/env python
"""
Tests for LSystem
"""

import unittest
import sys
sys.path.append('../LSystem')
from src import LSystemObject


class TestLSystemObject(unittest.TestCase):
    """
    Walkthrough of first few generations of Lindenmayer's original L-system to check LSystemObject
    """

    lsystem = LSystemObject.LSystemObject()

    def test_variable_methods(self):
        self.lsystem.addVar('x')
        self.lsystem.addVar('y')
        self.lsystem.addVar('z')
        actual = self.lsystem.getVars()
        expected = ['x', 'y', 'z']
        self.assertEqual(actual, expected)

        self.lsystem.deleteVar(1)
        actual = self.lsystem.getVars()
        expected = ['x', 'z']
        self.assertEqual(actual, expected)

    def test_constant_methods(self):
        self.lsystem.addConst('A')
        self.lsystem.addConst('B')
        self.lsystem.addConst('C')
        actual = self.lsystem.getConsts()
        expected = ['A', 'B', 'C']
        self.assertEqual(actual, expected)

        self.lsystem.deleteConst(1)
        actual = self.lsystem.getConsts()
        expected = ['A', 'C']
        self.assertEqual(actual, expected)

    def test_rule_methods(self):
        self.lsystem.addRule('x', 'xy')
        self.lsystem.addRule('y', 'x')
        self.lsystem.addRule('z', 'z')
        self.lsystem.deleteRule('z')
        expected = {'x', 'y'}
        actual = set(self.lsystem.getRules().keys())
        self.assertEqual(actual, expected)

    def test_start_state_methods(self):
        self.assertEqual(self.lsystem.getStart(), "")
        self.lsystem.addStart('y')
        self.lsystem.deleteStart()
        self.lsystem.addStart('x')
        self.assertEqual(self.lsystem.getStart(), 'x')


if __name__ == '__main__':
    unittest.main()
