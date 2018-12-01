def make_object(data):
    from .classes.objects import Car, Person
    selector = dict(
        person=Person,
        car=Car,
    )
    for datum in data:
        pass
