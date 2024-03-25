#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_attributes(self):
        state = State()

        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
