from ds.stack import Stack
import pytest


@pytest.fixture
def stack():
    return Stack()


def test_constructor(stack):
    assert isinstance(stack, Stack)
    assert len(stack) == 0


def test_push(stack):
    PUSH_TOTAL = 10
    for i in range(PUSH_TOTAL):
        stack.push(i)
    assert len(stack) == PUSH_TOTAL


def test_pop(stack):
    ITEM_COUNT = 5
    for i in range(ITEM_COUNT):
        stack.push(i)
    assert len(stack) == ITEM_COUNT

    for i in range(ITEM_COUNT):
        assert stack.pop() == ITEM_COUNT-1-i
    
    # Try popping an empty stack
    assert len(stack) == 0
    assert stack.pop() is None
