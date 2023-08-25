from counter import Counter
import pytest


def test_counter_defaults():
    counter = Counter()
    assert counter.counter_name == "counter"
    assert counter.max_count == 20
    assert counter.loose_type == False
    assert counter.enable_reverse == False
    assert counter.count == 0


def test_counter_init():
    counter = Counter(name="New Counter", max_count=100, loose_type=True, enable_reverse=True)
    assert counter.counter_name == "New Counter"
    assert counter.max_count == 100
    assert counter.loose_type == True
    assert counter.enable_reverse == True
    assert counter.count == 0


def test_counter_loose_disabled():
    counter = Counter(name="Loose Counter", max_count=100, loose_type=False, enable_reverse=False)
    for _ in range(0, 10):
        counter.increment()
    assert counter.count == 10
    with pytest.raises(TypeError, match="reverse counter is disabled"):
        counter.decrement()
    counter.reset()
    assert counter.count == 0
    for _ in range(0, 10000):
        counter.increment()
    assert counter.count == 100


def test_counter_loose_enabled():
    counter = Counter(name="Loose Counter", max_count=100, loose_type=True, enable_reverse=False)
    for _ in range(0, 10):
        counter.increment()
    assert counter.count == 10
    with pytest.raises(TypeError, match="reverse counter is disabled"):
        counter.decrement()

    for _ in range(0, 10000):
        counter.increment()
    assert counter.count == 10010


def test_counter_reverse_enabled():
    counter = Counter(name="Loose Counter", max_count=100, loose_type=False, enable_reverse=True)
    for _ in range(0, 10):
        counter.increment()
    assert counter.count == 10

    counter.decrement()
    assert counter.count == 9

    for _ in range(0, 1000):
        counter.decrement()
    assert counter.count == 0


def test_counter_reverse_loose_enabled():
    counter = Counter(name="Loose Counter", max_count=100, loose_type=True, enable_reverse=True)
    for _ in range(0, 10):
        counter.increment()
    assert counter.count == 10

    counter.decrement()
    assert counter.count == 9

    counter.reset()
    assert counter.count == 0

    for _ in range(1, 1000):
        counter.decrement()
    assert counter.count == 0

    for _ in range(0, 1000):
        counter.increment()

    assert counter.count == 1000

    for _ in range(1, 2000):
        counter.decrement()
    assert counter.count == 0


