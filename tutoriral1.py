from ggame import App
myapp = App()
myapp.run()
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
polygon = PolygonAsset([(100,150), (300,20), (1,2), (1000,200), (3451,752)], thinline, blue)
rectangle = RectangleAsset(100000,200000, thinline, red)


# Now display a rectangle
Sprite(polygon)
Sprite(rectangle)
myapp = App()
myapp.run()
