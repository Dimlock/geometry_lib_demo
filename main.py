import geometry.factories as factories


def calculate_radius(*args) -> float:
    if len(args) == 1:
        creator = factories.CircleCreator(args[0])
    else:
        creator = factories.TriangleCreator(*args)
    figure = creator.create_figure()
    return figure.area()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
