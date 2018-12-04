from .classes.analyze import analyze


def analyze_image(object_list, region, image=None):
    cars_list, initialized_line = analyze(object_list, region)
    if image is not None:
        for line in initialized_line:
            line.draw_line(image)
    return bool(len(cars_list)), image
