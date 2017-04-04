from paraview.simple import *
import time
import datetime 

t0 = time.time()

print "Start time = ", datetime.datetime.now().time()

paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
reader = XMLPartitionedUnstructuredGridReader(FileName=['/home/fabidi89/Data_Thesis/50Million/50_100/50_100_million.pvtu'])
reader.CellArrayStatus = ['vtkOriginalCellIds', 'vtkGhostType']
reader.PointArrayStatus = ['Field 3', 'vtkGhostType', '___D3___GlobalNodeIds']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [879, 550]

# get color transfer function/color map for 'Field3'
field3LUT = GetColorTransferFunction('Field3')

# show data in view
readerDisplay = Show(reader, renderView1)

# trace defaults for the display properties.
readerDisplay.ColorArrayName = ['POINTS', 'Field 3']
readerDisplay.LookupTable = field3LUT
readerDisplay.OSPRayScaleArray = 'Field 3'
readerDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
readerDisplay.SelectOrientationVectors = 'Field 3'
readerDisplay.ScaleFactor = 0.14907000456005334
readerDisplay.SelectScaleArray = 'Field 3'
readerDisplay.GlyphType = 'Arrow'
readerDisplay.ScalarOpacityUnitDistance = 1.0069309747956139
readerDisplay.GaussianRadius = 0.07453500228002667
readerDisplay.SetScaleArray = ['POINTS', 'Field 3']
readerDisplay.ScaleTransferFunction = 'PiecewiseFunction'
readerDisplay.OpacityArray = ['POINTS', 'Field 3']
readerDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
readerDisplay.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'Field3'
field3PWF = GetOpacityTransferFunction('Field3')

# current camera placement for renderView1
renderView1.CameraPosition = [-3.481399999999997, 0.6225, 3.4388500000000004]
renderView1.CameraFocalPoint = [-3.4814, 0.6225, -0.75205]
renderView1.CameraParallelScale = 1.0846835112836455

loading_time = time.time() - t0
print "Time to load = ", loading_time

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
