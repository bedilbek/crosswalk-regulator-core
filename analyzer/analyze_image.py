from .classes.analyze import analyze


def analyze_image(object_list):
    from settings import region
    cars_list = analyze(object_list, region)
    return bool(len(cars_list))
