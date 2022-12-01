import rectangles as rect


def test_from_points():
    assert str(rect.Rectangle.from_points(rect.Point(
        1, 2), rect.Point(3, 4))) == '[(1, 2), (3, 4)]'
    assert str(rect.Rectangle.from_points(rect.Point(
        3, 4), rect.Point(1, 2))) == '[(3, 4), (1, 2)]'
    assert str(rect.Rectangle.from_points(rect.Point(
        1, 2), rect.Point(1, 2))) == '[(1, 2), (1, 2)]'


def test_properties():
    r = rect.Rectangle(1, 2, 3, 4)
    assert r.top == 4
    assert r.bottom == 2
    assert r.left == 1
    assert r.right == 3
    assert r.width == 2
    assert r.height == 2
    assert r.top_left == rect.Point(1, 4)
    assert r.top_right == rect.Point(3, 4)
    assert r.bottom_left == rect.Point(1, 2)
    assert r.bottom_right == rect.Point(3, 2)
    assert r.center == rect.Point(2, 3)
