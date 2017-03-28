from paraview.simple import *
import time

t0 = time.time()

paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
reader = XMLPartitionedUnstructuredGridReader(FileName=['/home/fabidi89/Data_Thesis/50Million/50million_8files/50million.pvtu'])
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

loading_time = time.time() - t0
print "Time to load = ", loading_time


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

# get camera animation track for the view
cameraAnimationCue1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
keyFrame4246 = CameraKeyFrame()
keyFrame4246.Position = [-3.4814001321792603, 0.6225000098347664, 3.4388452450005023]
keyFrame4246.FocalPoint = [-3.4814001321792603, 0.6225000098347664, -0.7520500225946307]
keyFrame4246.ParallelScale = 1.0846835112836455
keyFrame4246.PositionPathPoints = [-3.4814001321792603, 0.6225000098347664, 2.974700091406703, -1.2908713761899837, 0.6225000098347664, 2.2629541534212207, 0.06294984834541362, 0.6225000098347664, 0.39957909642055434, 0.06294984834541362, 0.6225000098347664, -1.9036791416098144, -1.2908713761899837, 0.6225000098347664, -3.7670541986104804, -3.4814001321792594, 0.6225000098347664, -4.478800136595963, -5.671928888168535, 0.6225000098347664, -3.767054198610481, -7.025750112703932, 0.6225000098347664, -1.9036791416098156, -7.025750112703932, 0.6225000098347664, 0.39957909642055167, -5.6719288881685355, 0.6225000098347664, 2.2629541534212163]
keyFrame4246.FocalPathPoints = [-3.4814001321792603, 0.6225000098347664, -0.7520500225946307]
keyFrame4246.ClosedPositionPath = 1

# create a key frame
keyFrame4247 = CameraKeyFrame()
keyFrame4247.KeyTime = 1.0
keyFrame4247.Position = [-3.4814001321792603, 0.6225000098347664, 3.4388452450005023]
keyFrame4247.FocalPoint = [-3.4814001321792603, 0.6225000098347664, -0.7520500225946307]
keyFrame4247.ParallelScale = 1.0846835112836455

# initialize the animation track
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.KeyFrames = [keyFrame4246, keyFrame4247]

# get animation scene
animationScene1 = GetAnimationScene()

# Properties modified on animationScene1
animationScene1.NumberOfFrames = 1000

t1 = time.time()

animationScene1.Play()

# current camera placement for renderView1
renderView1.CameraPosition = [-3.4367075935776494, -1.799804353653681, 2.9747000914067003]
renderView1.CameraFocalPoint = [-3.48140013217926, 0.622500009834766, -0.752050022594631]
renderView1.CameraViewUp = [0.7312863783951185, -0.6750910641619742, -0.09732567935753168]
renderView1.CameraParallelScale = 1.08468

# current camera placement for renderView1
renderView1.CameraPosition = [-3.4367075935776494, -1.799804353653681, 2.9747000914067003]
renderView1.CameraFocalPoint = [-3.48140013217926, 0.622500009834766, -0.752050022594631]
renderView1.CameraViewUp = [0.7312863783951185, -0.6750910641619742, -0.09732567935753168]
renderView1.CameraParallelScale = 1.08468


render_time = time.time() - t1
print "Animation complete in ", render_time, " seconds"

print "Frame rate = ", float(1000)/float(render_time)

# save animation images/movie
WriteAnimation('/home/fabidi89/git/Thesis/ParaView/8Files/traversal/Animation/frame.png', Magnification=1, FrameRate=15.0, Compression=True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-3.4367075935776494, -1.799804353653681, 2.9747000914067003]
renderView1.CameraFocalPoint = [-3.48140013217926, 0.622500009834766, -0.752050022594631]
renderView1.CameraViewUp = [0.7312863783951185, -0.6750910641619742, -0.09732567935753168]
renderView1.CameraParallelScale = 1.08468

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
