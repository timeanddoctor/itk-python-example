'''
 Author: QIN Shuo
 Date:   2015/11/10
 This is a example file for vtk
 Description:
   This file demostrate how to get the position of a 
   picked point.
'''


import vtk


drawing = vtk.vtkImageCanvasSource2D()
drawing.SetScalarTypeToUnsignedChar()
drawing.SetNumberOfScalarComponents(3)
drawing.SetExtent(0,20,0,50,0,0)
drawing.FillBox(0,20,0,50)


drawing.SetDrawColor(255,0,0,0)
drawing.DrawCircle(9,10,5)
drawing.Update()

actor = vtk.vtkImageActor()
actor.GetMapper().SetInput(drawing.GetOutput())
actor.InterpolateOff();

renderer = vtk.vtkRenderer()
renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer)

renderWinInteractor = vtk.vtkRenderWindowInteractor()
renderWinInteractor.SetRenderWindow(renderWin)

renderer.AddActor(actor)
renderer.SetBackground(1,1,1)

renderer.GradientBackgroundOn()
renderer.SetBackground2(0,0,1)

renderWin.Render()

def keyPressCallBack(obj,event):
    global renderWinInteractor
    global renderer
    coor = renderWinInteractor.GetEventPosition()
    print "coordinate is ", coor
    renderWinInteractor.GetPicker().Pick(renderWinInteractor.GetEventPosition()[0],renderWinInteractor.GetEventPosition()[1],0,renderer)
    picked = renderWinInteractor.GetPicker().GetPickPosition()
    print "position is ",picked


# create a null interactorstyle to disable default rotation
class MyStyle(vtk.vtkInteractorStyleImage):
    def __init__(self):
        pass
style = MyStyle()
renderWinInteractor.SetInteractorStyle(style)

renderWinInteractor.AddObserver(vtk.vtkCommand.LeftButtonPressEvent,keyPressCallBack)

renderWinInteractor.Start()


