#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
test1pvtu = XMLPartitionedUnstructuredGridReader(FileName=['/home/faiz89/Paraview-D3/test1.pvtu'])
test1pvtu.CellArrayStatus = ['vtkOriginalCellIds', 'vtkGhostLevels']
test1pvtu.PointArrayStatus = ['Field 3', 'vtkGhostLevels', '___D3___GlobalNodeIds']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1205, 806]

# show data in view
test1pvtuDisplay = Show(test1pvtu, renderView1)
# trace defaults for the display properties.
test1pvtuDisplay.ColorArrayName = [None, '']
test1pvtuDisplay.OSPRayScaleArray = 'Field 3'
test1pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
test1pvtuDisplay.SelectOrientationVectors = 'Field 3'
test1pvtuDisplay.ScaleFactor = 0.14907
test1pvtuDisplay.SelectScaleArray = 'Field 3'
test1pvtuDisplay.GlyphType = 'Arrow'
test1pvtuDisplay.ScalarOpacityUnitDistance = 1.084683438842873
test1pvtuDisplay.GaussianRadius = 0.074535
test1pvtuDisplay.SetScaleArray = ['POINTS', 'Field 3']
test1pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
test1pvtuDisplay.OpacityArray = ['POINTS', 'Field 3']
test1pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# get camera animation track for the view
cameraAnimationCue1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
keyFrame4271 = CameraKeyFrame()
keyFrame4271.Position = [-3.4814, 0.6225, 3.438844987705481]
keyFrame4271.FocalPoint = [-3.4814, 0.6225, -0.75205]
keyFrame4271.ParallelScale = 1.084683438842873
keyFrame4271.PositionPathPoints = [-3.4814, 0.6225, 3.4388399999999995, -0.22446676158959544, 0.6225, 1.8853625336468531, 0.6179089984392991, 0.6225, -1.6233850259312392, -1.57877575454653, 0.6225, -4.486160332155789, -5.18598853009994, 0.6225, -4.5806185229798, -7.529488886136594, 0.6225, -1.836732147929704, -6.871901231556025, 0.6225, 1.7112933359800029]
keyFrame4271.FocalPathPoints = [-3.4814, 0.6225, -0.75205]
keyFrame4271.ClosedPositionPath = 1

# create a key frame
keyFrame4272 = CameraKeyFrame()
keyFrame4272.KeyTime = 1.0
keyFrame4272.Position = [-3.4814, 0.6225, 3.438844987705481]
keyFrame4272.FocalPoint = [-3.4814, 0.6225, -0.75205]
keyFrame4272.ParallelScale = 1.084683438842873

# initialize the animation track
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.KeyFrames = [keyFrame4271, keyFrame4272]

# get animation scene
animationScene1 = GetAnimationScene()

# Properties modified on animationScene1
animationScene1.NumberOfFrames = 1000

animationScene1.Play()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-3.481400000000002, 0.6225, 3.438839999999999]
renderView1.CameraFocalPoint = [-3.4814, 0.6225, -0.75205]
renderView1.CameraParallelScale = 1.084683438842873

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).