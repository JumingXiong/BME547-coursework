def test_line():
    from line import line
    input_point1 = (1,2)
    input_point2 = (2,4)
    input_x = 3
    answer = line(input_point1,input_point2,input_x)
    expected = 6
    assert answer == expected