from collections import deque
import string


def _map_keys() -> dict:
    """ Map keypad numbers to ascii characters

    Returns:
        dict: Maps key number to a list of characters
    """

    FOUR_CHARS = {7, 9}
    key_map = {'0': [" "], '1': []} # Hard code special keys
    start, stop = 0, 3 # Set the initial slice indexes

    def _inc_slice_index(n):
        """ Increment the start:stop slicing indexes by n """
        nonlocal start, stop
        start += n
        stop += n

    for i in range(len(key_map), len(string.digits)):
        key = str(i)
        if i in FOUR_CHARS:
            key_map[key] = list(string.ascii_lowercase[start:stop + 1])
            _inc_slice_index(4)
        else:
            key_map[key] = list(string.ascii_lowercase[start:stop])
            _inc_slice_index(3)

    return key_map


def _create_string(seq) -> str:
    """ Create a string from a list of integers. The integer maps to a 
    possible list of chars.  The frequency (length of sequence) determines
    the index of the character to use.  
    For example: [4, 4, 4], length 3, maps
    to the character 'i'; the 3rd character in the list.

    Args:
        sequence (list[[str]]): Eg: ['2','2'],['0'], ['2']]

    Returns:
        str: A string from the sequence of key presses.
    """

    # Get a key mapping.
    keymap = _map_keys()

    # Build the string from the key press sequence.
    str_seq = ""
    for freq in seq:
        str_seq += keymap[freq[0]][len(freq) - 1]
    return str_seq


def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    >>> keypad_string("#")
    Traceback (most recent call last):
    AssertionError: Invalid Key: Acceptable keys 0123456789
    '''

    MAX_KEYPRESS_COUNT = 3  # Max number of times a key can be pressed
    IGNORE_KEYS = {'1'}     # Set of keys that do nothing and will be ignored.

    if not keys:
        return ''

    keys_q = deque(keys)
    seq, buf, count = [], [], 0

    while(keys_q):
        key_pressed = keys_q.popleft()  # popleft=O(1) vs pop(0)=O(n)
        assert key_pressed in string.digits, "Invalid Key: Acceptable keys " + string.digits

        # Ignore certain keys, and service the next key press
        if key_pressed in IGNORE_KEYS: continue

        count += 1
        # Append the pressed key to the buffer.  If the key has been pressed 3 times, the max
        # sequence has been reached, and must be appened to the sequence list.
        if (not buf or buf and key_pressed == buf[0]) and count < MAX_KEYPRESS_COUNT:
            buf.append(key_pressed)
        else:
            seq.append(buf)
            buf = []
            buf.append(key_pressed)
            count = 0

    # Append the buffer if it contains valid key presses.
    if buf: seq.append(buf)
    return _create_string(seq)
