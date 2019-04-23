from pont import Pont
from sokszog import Sokszog
from haromszog import Haromszog
from formbuilder import *

class Program:
    def __init__(self):
        pass

    def close(self, event):
        foablak.Destroy()

    def openNevjegy(self, event):
        nevjegy.Show()

    def frissites(self, event):
        foablak.canvas.Refresh()

    def rajzol(self, event):
        ax, ay = foablak.coordAX.GetValue(), foablak.coordAY.GetValue()
        bx, by = foablak.coordBX.GetValue(), foablak.coordBY.GetValue()
        cx, cy = foablak.coordCX.GetValue(), foablak.coordCY.GetValue()
        a = Pont(ax, ay)
        b = Pont(bx, by)
        c = Pont(cx, cy)
        triangle.setCsomopontok((a, b, c))
        try:
            foablak.kerulet.SetValue(str(int(round(triangle.getKerulet() * 100))/100))
            foablak.terulet.SetValue(str(int(round(triangle.getTerulet() * 100))/100))

        except TypeError as err:
            foablak.m_statusBar1.PushStatusText("Hiba! Nem megfelelő a szám típusa. Üzenet: " + err.args[0])

        except ValueError as err:
            foablak.m_statusBar1.PushStatusText("Hiba! Nem megfelelő számérték. Üzenet: " + err.args[0])
        abcx = [1, ax, bx, cx]
        abcy = [1, ay, by, cy]
        abcx.sort()
        abcy.sort()
        maxx = (abcx[3] - abcx[0]) / 2
        maxy = (abcy[3] - abcy[0]) / 2
        origoX = 366
        origoY = 233
        if(maxx == 0):
            maxx = 1
        if(maxy == 0):
            maxy = 1
        scalex = int(origoX / maxx)
        if(scalex == 0):
            scalex = int(origoX * 10 / maxx) / 10
        if(scalex == 0):
            scalex = int(origoX * 50 / maxx) / 50
        scaley = int(origoY / maxy)
        if(scaley == 0):
            scaley = int(origoY * 10 / maxy) / 10
        if(scaley == 0):
            scaley = int(origoY * 50 / maxy) / 50
        if(scalex < scaley):
            scale = scalex
        else:
            scale = scaley
        scale *= 0.8
        origoX -= (abcx[3] + abcx[0]) / 2 * scale
        origoY -= (abcy[3] + abcy[0]) / 2 * scale
        ax *= scale
        ay *= scale
        bx *= scale
        by *= scale
        cx *= scale
        cy *= scale
        ax += origoX
        ay += origoY
        bx += origoX
        by += origoY
        cx += origoX
        cy += origoY
        ay = 466 - ay
        by = 466 - by
        cy = 466 - cy
        self.dc = wx.PaintDC(foablak.canvas)
        self.gc = wx.GraphicsContext.Create(self.dc)
        if(self.gc):
            self.gc.SetPen(wx.GREEN_PEN)
            path = self.gc.CreatePath()
            path.MoveToPoint(origoX, 0)
            path.AddLineToPoint(origoX, 466)
            path.MoveToPoint(0, 466 - origoY)
            path.AddLineToPoint(722, 466 - origoY)
            self.gc.StrokePath(path)
            self.gc.SetPen(wx.BLUE_PEN)
            path = self.gc.CreatePath()
            path.MoveToPoint(ax, ay)
            path.AddLineToPoint(bx, by)
            path.AddLineToPoint(cx, cy)
            path.AddLineToPoint(ax, ay)
            path.CloseSubpath()
            self.gc.StrokePath(path)

program = Program()
app = wx.App()
foablak = FoAblak(None)
ax, ay = foablak.coordAX.GetValue(), foablak.coordAY.GetValue()
bx, by = foablak.coordBX.GetValue(), foablak.coordBY.GetValue()
cx, cy = foablak.coordCX.GetValue(), foablak.coordCY.GetValue()
a = Pont(ax, ay)
b = Pont(bx, by)
c = Pont(cx, cy)
triangle = Haromszog((a, b, c))
nevjegy = NevjegyAblak(foablak)
foablak.m_statusBar1.SetStatusText("Ez egy példa")
foablak.Bind(wx.EVT_CLOSE, program.close)
foablak.Bind(wx.EVT_MENU, program.close, id = foablak.menuClose.GetId())
foablak.Bind(wx.EVT_MENU, program.openNevjegy, id = foablak.menuNevjegy.GetId())
foablak.gomb.Bind(wx.EVT_BUTTON, program.close)
foablak.canvas.Bind(wx.EVT_PAINT, program.rajzol)
foablak.coordAX.Bind(wx.EVT_SPINCTRL, program.frissites)
foablak.coordAY.Bind(wx.EVT_SPINCTRL, program.frissites)
foablak.coordBX.Bind(wx.EVT_SPINCTRL, program.frissites)
foablak.coordBY.Bind(wx.EVT_SPINCTRL, program.frissites)
foablak.coordCX.Bind(wx.EVT_SPINCTRL, program.frissites)
foablak.coordCY.Bind(wx.EVT_SPINCTRL, program.frissites)
foablak.Show(True)
app.MainLoop()
