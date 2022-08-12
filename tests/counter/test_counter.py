from src.counter import count_ocurrences

path = 'src/jobs.csv'
word = ["Python", "Javascript"]


def test_counter():
    word_count = count_ocurrences(path, "Python")
    assert word_count == 1639
