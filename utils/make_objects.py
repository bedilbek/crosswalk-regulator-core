def make_objects(data):
    object_list = list()
    from analyzer.classes.objects import Car, Person
    selector = dict(
        person=Person,
        car=Car,
    )
    for datum in data:
        object_class = selector.get(datum[0], None)
        if object_class is None:
            continue
        object_list.append(object_class(datum[1], datum[2]))

    return object_list
