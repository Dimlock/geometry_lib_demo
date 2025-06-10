import geometry.factories as factories
import geometry.shapes as shapes


def calculate_radius(*args) -> float:
    if len(args) == 1:
        creator: factories.FigureCreator = factories.CircleCreator(args[0])
    else:
        creator: factories.FigureCreator = factories.TriangleCreator(*args)
    figure: shapes.Figure = creator.create_figure()
    return figure.area()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
