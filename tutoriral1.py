from ggame import App
myapp = App()
myapp.run()
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset


red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)


thinline = LineStyle(1,black)

Ellipse = EllipseAsset(1000, 2000, thinline, blue)
Sprite(Ellipse)
Ellipse = EllipseAsset(400, 1000, thinline, blue)
Sprite(Ellipse)


myapp = App()
myapp.run()