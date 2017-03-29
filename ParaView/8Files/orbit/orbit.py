from paraview.simple import *
import time
import datetime 

t0 = time.time()

print "Start time = ", datetime.datetime.now().time()

paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
reader = XMLPartitionedUnstructuredGridReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/1Lakh/1Lakh_8files/1lakh.pvtu'])
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

loading_time = time.time() - t0
print "Time to load = ", loading_time

# get camera animation track for the view
cameraAnimationCue1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
keyFrame4244 = CameraKeyFrame()
keyFrame4244.Position = [-3.4814001321792603, 0.6225000098347664, 3.4388452450005023]
keyFrame4244.FocalPoint = [-3.4814001321792603, 0.6225000098347664, -0.7520500225946307]
keyFrame4244.ParallelScale = 1.0846835112836455
keyFrame4244.PositionPathPoints = [-3.4814, 0.6225, 3.43885, -0.2244589901299805, 0.6225, 1.885368826850764, 0.617918779915307, 0.6225, -1.6233871050481472, -1.5787712146415325, 0.6225, -4.486169242221031, -5.185992597466371, 0.6225, -4.580627658434377, -7.5294985453948575, 0.6225, -1.836734736120155, -6.871909321725969, 0.6225, 1.7112992138325263]
keyFrame4244.FocalPathPoints = [-3.4814, 0.6225, -0.75205]
keyFrame4244.ClosedPositionPath = 1

# create a key frame
keyFrame4245 = CameraKeyFrame()
keyFrame4245.KeyTime = 1.0
keyFrame4245.Position = [-3.4814001321792603, 0.6225000098347664, 3.4388452450005023]
keyFrame4245.FocalPoint = [-3.4814001321792603, 0.6225000098347664, -0.7520500225946307]
keyFrame4245.ParallelScale = 1.0846835112836455

# initialize the animation track
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.KeyFrames = [keyFrame4244, keyFrame4245]

# get animation scene
animationScene1 = GetAnimationScene()

# Properties modified on animationScene1
animationScene1.NumberOfFrames = 1000

t1 = time.time()

animationScene1.Play()

# current camera placement for renderView1
renderView1.CameraPosition = [-3.481399999999997, 0.6225, 3.4388500000000004]
renderView1.CameraFocalPoint = [-3.4814, 0.6225, -0.75205]
renderView1.CameraParallelScale = 1.0846835112836455

# current camera placement for renderView1
renderView1.CameraPosition = [-3.481399999999997, 0.6225, 3.4388500000000004]
renderView1.CameraFocalPoint = [-3.4814, 0.6225, -0.75205]
renderView1.CameraParallelScale = 1.0846835112836455

render_time = time.time() - t1
print "Animation complete in ", render_time, " seconds"

print "Frame rate = ", float(1000)/float(render_time)

# save animation images/movie
WriteAnimation('/home/faiz89/Data_Thesis/Data_Thesis/1Lakh/1Lakh_8files/Animation/frame.png', Magnification=1, FrameRate=15.0, Compression=True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-3.481399999999997, 0.6225, 3.4388500000000004]
renderView1.CameraFocalPoint = [-3.4814, 0.6225, -0.75205]
renderView1.CameraParallelScale = 1.0846835112836455

print "End time = ", datetime.datetime.now().time()

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
