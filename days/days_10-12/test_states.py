from unittest.mock import patch

import pytest

from states import (get_every_nth_state, 
                    get_state_abbrev, 
                    get_longest_state, 
                    combine_state_names_and_abbreviations,
                    NOT_FOUND)

def test_get_every_nth_state(states, n):
    expected = ['Massachusetts', 'Missouri', 'Hawaii',
                'Vermont', 'Delaware']
    assert list(get_every_nth_state(n=10)) == expected
    expected = ['Missouri', 'Vermont']
    assert list(get_every_nth_state(n=20)) == expected