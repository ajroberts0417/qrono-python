import qrono


def test_build_qrono_object_from_dict():
    my_dict = {
        'a': 1,
        'b': [{
            'c': 2,
        }, 3],
        'd': {
            'e': 4,
            'f': 5,
        },
    }

    my_obj = qrono.QronoObject.from_dict(my_dict)

    assert(my_obj.a == 1)
    assert(my_obj.b[0].c == 2)
    assert(my_obj.b[1] == 3)
    assert(my_obj.d.e == 4)
    assert(my_obj.d.f == 5)
