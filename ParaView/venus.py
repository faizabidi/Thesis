from paraview.simple import *
import time
import datetime

t0 = time.time()
print "Start time = ", datetime.datetime.now().time()

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML MultiBlock Data Reader'
example_20vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.0.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2100vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.100.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2120vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.120.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2140vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.140.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2160vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.160.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2180vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.180.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_220vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.20.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2200vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.200.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2220vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.220.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2240vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.240.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2260vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.260.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2280vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.280.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2300vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.300.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2320vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.320.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2340vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.340.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2360vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.360.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2380vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.380.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_240vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.40.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2400vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.400.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2420vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.420.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2440vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.440.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2460vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.460.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2480vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.480.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2500vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.500.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2520vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.520.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2540vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.540.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2560vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.560.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2580vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.580.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_260vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.60.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_2600vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.600.vtm'])

# create a new 'XML MultiBlock Data Reader'
example_280vtm = XMLMultiBlockDataReader(FileName=['/home/faiz89/Data_Thesis/Data_Thesis/example_2/example_2.80.vtm'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [879, 550]

# show data in view
example_2220vtmDisplay = Show(example_2220vtm, renderView1)

# trace defaults for the display properties.
example_2220vtmDisplay.Representation = 'Surface'
example_2220vtmDisplay.ColorArrayName = ['POINTS', '']
example_2220vtmDisplay.OSPRayScaleArray = 'temperature'
example_2220vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2220vtmDisplay.SelectOrientationVectors = 'velocity'
example_2220vtmDisplay.ScaleFactor = 0.2
example_2220vtmDisplay.SelectScaleArray = 'temperature'
example_2220vtmDisplay.GlyphType = 'Arrow'
example_2220vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# reset view to fit data
renderView1.ResetCamera()

# show data in view
example_20vtmDisplay = Show(example_20vtm, renderView1)
# trace defaults for the display properties.
example_20vtmDisplay.Representation = 'Surface'
example_20vtmDisplay.ColorArrayName = ['POINTS', '']
example_20vtmDisplay.OSPRayScaleArray = 'temperature'
example_20vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_20vtmDisplay.SelectOrientationVectors = 'velocity'
example_20vtmDisplay.ScaleFactor = 0.2
example_20vtmDisplay.SelectScaleArray = 'temperature'
example_20vtmDisplay.GlyphType = 'Arrow'
example_20vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2240vtmDisplay = Show(example_2240vtm, renderView1)
# trace defaults for the display properties.
example_2240vtmDisplay.Representation = 'Surface'
example_2240vtmDisplay.ColorArrayName = ['POINTS', '']
example_2240vtmDisplay.OSPRayScaleArray = 'temperature'
example_2240vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2240vtmDisplay.SelectOrientationVectors = 'velocity'
example_2240vtmDisplay.ScaleFactor = 0.2
example_2240vtmDisplay.SelectScaleArray = 'temperature'
example_2240vtmDisplay.GlyphType = 'Arrow'
example_2240vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2360vtmDisplay = Show(example_2360vtm, renderView1)
# trace defaults for the display properties.
example_2360vtmDisplay.Representation = 'Surface'
example_2360vtmDisplay.ColorArrayName = ['POINTS', '']
example_2360vtmDisplay.OSPRayScaleArray = 'temperature'
example_2360vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2360vtmDisplay.SelectOrientationVectors = 'velocity'
example_2360vtmDisplay.ScaleFactor = 0.2
example_2360vtmDisplay.SelectScaleArray = 'temperature'
example_2360vtmDisplay.GlyphType = 'Arrow'
example_2360vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2260vtmDisplay = Show(example_2260vtm, renderView1)
# trace defaults for the display properties.
example_2260vtmDisplay.Representation = 'Surface'
example_2260vtmDisplay.ColorArrayName = ['POINTS', '']
example_2260vtmDisplay.OSPRayScaleArray = 'temperature'
example_2260vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2260vtmDisplay.SelectOrientationVectors = 'velocity'
example_2260vtmDisplay.ScaleFactor = 0.2
example_2260vtmDisplay.SelectScaleArray = 'temperature'
example_2260vtmDisplay.GlyphType = 'Arrow'
example_2260vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2380vtmDisplay = Show(example_2380vtm, renderView1)
# trace defaults for the display properties.
example_2380vtmDisplay.Representation = 'Surface'
example_2380vtmDisplay.ColorArrayName = ['POINTS', '']
example_2380vtmDisplay.OSPRayScaleArray = 'temperature'
example_2380vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2380vtmDisplay.SelectOrientationVectors = 'velocity'
example_2380vtmDisplay.ScaleFactor = 0.2
example_2380vtmDisplay.SelectScaleArray = 'temperature'
example_2380vtmDisplay.GlyphType = 'Arrow'
example_2380vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2280vtmDisplay = Show(example_2280vtm, renderView1)
# trace defaults for the display properties.
example_2280vtmDisplay.Representation = 'Surface'
example_2280vtmDisplay.ColorArrayName = ['POINTS', '']
example_2280vtmDisplay.OSPRayScaleArray = 'temperature'
example_2280vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2280vtmDisplay.SelectOrientationVectors = 'velocity'
example_2280vtmDisplay.ScaleFactor = 0.2
example_2280vtmDisplay.SelectScaleArray = 'temperature'
example_2280vtmDisplay.GlyphType = 'Arrow'
example_2280vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_240vtmDisplay = Show(example_240vtm, renderView1)
# trace defaults for the display properties.
example_240vtmDisplay.Representation = 'Surface'
example_240vtmDisplay.ColorArrayName = ['POINTS', '']
example_240vtmDisplay.OSPRayScaleArray = 'temperature'
example_240vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_240vtmDisplay.SelectOrientationVectors = 'velocity'
example_240vtmDisplay.ScaleFactor = 0.2
example_240vtmDisplay.SelectScaleArray = 'temperature'
example_240vtmDisplay.GlyphType = 'Arrow'
example_240vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2320vtmDisplay = Show(example_2320vtm, renderView1)
# trace defaults for the display properties.
example_2320vtmDisplay.Representation = 'Surface'
example_2320vtmDisplay.ColorArrayName = ['POINTS', '']
example_2320vtmDisplay.OSPRayScaleArray = 'temperature'
example_2320vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2320vtmDisplay.SelectOrientationVectors = 'velocity'
example_2320vtmDisplay.ScaleFactor = 0.2
example_2320vtmDisplay.SelectScaleArray = 'temperature'
example_2320vtmDisplay.GlyphType = 'Arrow'
example_2320vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2300vtmDisplay = Show(example_2300vtm, renderView1)
# trace defaults for the display properties.
example_2300vtmDisplay.Representation = 'Surface'
example_2300vtmDisplay.ColorArrayName = ['POINTS', '']
example_2300vtmDisplay.OSPRayScaleArray = 'temperature'
example_2300vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2300vtmDisplay.SelectOrientationVectors = 'velocity'
example_2300vtmDisplay.ScaleFactor = 0.2
example_2300vtmDisplay.SelectScaleArray = 'temperature'
example_2300vtmDisplay.GlyphType = 'Arrow'
example_2300vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2400vtmDisplay = Show(example_2400vtm, renderView1)
# trace defaults for the display properties.
example_2400vtmDisplay.Representation = 'Surface'
example_2400vtmDisplay.ColorArrayName = ['POINTS', '']
example_2400vtmDisplay.OSPRayScaleArray = 'temperature'
example_2400vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2400vtmDisplay.SelectOrientationVectors = 'velocity'
example_2400vtmDisplay.ScaleFactor = 0.2
example_2400vtmDisplay.SelectScaleArray = 'temperature'
example_2400vtmDisplay.GlyphType = 'Arrow'
example_2400vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2340vtmDisplay = Show(example_2340vtm, renderView1)
# trace defaults for the display properties.
example_2340vtmDisplay.Representation = 'Surface'
example_2340vtmDisplay.ColorArrayName = ['POINTS', '']
example_2340vtmDisplay.OSPRayScaleArray = 'temperature'
example_2340vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2340vtmDisplay.SelectOrientationVectors = 'velocity'
example_2340vtmDisplay.ScaleFactor = 0.2
example_2340vtmDisplay.SelectScaleArray = 'temperature'
example_2340vtmDisplay.GlyphType = 'Arrow'
example_2340vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2420vtmDisplay = Show(example_2420vtm, renderView1)
# trace defaults for the display properties.
example_2420vtmDisplay.Representation = 'Surface'
example_2420vtmDisplay.ColorArrayName = ['POINTS', '']
example_2420vtmDisplay.OSPRayScaleArray = 'temperature'
example_2420vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2420vtmDisplay.SelectOrientationVectors = 'velocity'
example_2420vtmDisplay.ScaleFactor = 0.2
example_2420vtmDisplay.SelectScaleArray = 'temperature'
example_2420vtmDisplay.GlyphType = 'Arrow'
example_2420vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2440vtmDisplay = Show(example_2440vtm, renderView1)
# trace defaults for the display properties.
example_2440vtmDisplay.Representation = 'Surface'
example_2440vtmDisplay.ColorArrayName = ['POINTS', '']
example_2440vtmDisplay.OSPRayScaleArray = 'temperature'
example_2440vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2440vtmDisplay.SelectOrientationVectors = 'velocity'
example_2440vtmDisplay.ScaleFactor = 0.2
example_2440vtmDisplay.SelectScaleArray = 'temperature'
example_2440vtmDisplay.GlyphType = 'Arrow'
example_2440vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2520vtmDisplay = Show(example_2520vtm, renderView1)
# trace defaults for the display properties.
example_2520vtmDisplay.Representation = 'Surface'
example_2520vtmDisplay.ColorArrayName = ['POINTS', '']
example_2520vtmDisplay.OSPRayScaleArray = 'temperature'
example_2520vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2520vtmDisplay.SelectOrientationVectors = 'velocity'
example_2520vtmDisplay.ScaleFactor = 0.2
example_2520vtmDisplay.SelectScaleArray = 'temperature'
example_2520vtmDisplay.GlyphType = 'Arrow'
example_2520vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2540vtmDisplay = Show(example_2540vtm, renderView1)
# trace defaults for the display properties.
example_2540vtmDisplay.Representation = 'Surface'
example_2540vtmDisplay.ColorArrayName = ['POINTS', '']
example_2540vtmDisplay.OSPRayScaleArray = 'temperature'
example_2540vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2540vtmDisplay.SelectOrientationVectors = 'velocity'
example_2540vtmDisplay.ScaleFactor = 0.2
example_2540vtmDisplay.SelectScaleArray = 'temperature'
example_2540vtmDisplay.GlyphType = 'Arrow'
example_2540vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2460vtmDisplay = Show(example_2460vtm, renderView1)
# trace defaults for the display properties.
example_2460vtmDisplay.Representation = 'Surface'
example_2460vtmDisplay.ColorArrayName = ['POINTS', '']
example_2460vtmDisplay.OSPRayScaleArray = 'temperature'
example_2460vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2460vtmDisplay.SelectOrientationVectors = 'velocity'
example_2460vtmDisplay.ScaleFactor = 0.2
example_2460vtmDisplay.SelectScaleArray = 'temperature'
example_2460vtmDisplay.GlyphType = 'Arrow'
example_2460vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2560vtmDisplay = Show(example_2560vtm, renderView1)
# trace defaults for the display properties.
example_2560vtmDisplay.Representation = 'Surface'
example_2560vtmDisplay.ColorArrayName = ['POINTS', '']
example_2560vtmDisplay.OSPRayScaleArray = 'temperature'
example_2560vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2560vtmDisplay.SelectOrientationVectors = 'velocity'
example_2560vtmDisplay.ScaleFactor = 0.2
example_2560vtmDisplay.SelectScaleArray = 'temperature'
example_2560vtmDisplay.GlyphType = 'Arrow'
example_2560vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2480vtmDisplay = Show(example_2480vtm, renderView1)
# trace defaults for the display properties.
example_2480vtmDisplay.Representation = 'Surface'
example_2480vtmDisplay.ColorArrayName = ['POINTS', '']
example_2480vtmDisplay.OSPRayScaleArray = 'temperature'
example_2480vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2480vtmDisplay.SelectOrientationVectors = 'velocity'
example_2480vtmDisplay.ScaleFactor = 0.2
example_2480vtmDisplay.SelectScaleArray = 'temperature'
example_2480vtmDisplay.GlyphType = 'Arrow'
example_2480vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2580vtmDisplay = Show(example_2580vtm, renderView1)
# trace defaults for the display properties.
example_2580vtmDisplay.Representation = 'Surface'
example_2580vtmDisplay.ColorArrayName = ['POINTS', '']
example_2580vtmDisplay.OSPRayScaleArray = 'temperature'
example_2580vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2580vtmDisplay.SelectOrientationVectors = 'velocity'
example_2580vtmDisplay.ScaleFactor = 0.2
example_2580vtmDisplay.SelectScaleArray = 'temperature'
example_2580vtmDisplay.GlyphType = 'Arrow'
example_2580vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2500vtmDisplay = Show(example_2500vtm, renderView1)
# trace defaults for the display properties.
example_2500vtmDisplay.Representation = 'Surface'
example_2500vtmDisplay.ColorArrayName = ['POINTS', '']
example_2500vtmDisplay.OSPRayScaleArray = 'temperature'
example_2500vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2500vtmDisplay.SelectOrientationVectors = 'velocity'
example_2500vtmDisplay.ScaleFactor = 0.2
example_2500vtmDisplay.SelectScaleArray = 'temperature'
example_2500vtmDisplay.GlyphType = 'Arrow'
example_2500vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2600vtmDisplay = Show(example_2600vtm, renderView1)
# trace defaults for the display properties.
example_2600vtmDisplay.Representation = 'Surface'
example_2600vtmDisplay.ColorArrayName = ['POINTS', '']
example_2600vtmDisplay.OSPRayScaleArray = 'temperature'
example_2600vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2600vtmDisplay.SelectOrientationVectors = 'velocity'
example_2600vtmDisplay.ScaleFactor = 0.2
example_2600vtmDisplay.SelectScaleArray = 'temperature'
example_2600vtmDisplay.GlyphType = 'Arrow'
example_2600vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_280vtmDisplay = Show(example_280vtm, renderView1)
# trace defaults for the display properties.
example_280vtmDisplay.Representation = 'Surface'
example_280vtmDisplay.ColorArrayName = ['POINTS', '']
example_280vtmDisplay.OSPRayScaleArray = 'temperature'
example_280vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_280vtmDisplay.SelectOrientationVectors = 'velocity'
example_280vtmDisplay.ScaleFactor = 0.2
example_280vtmDisplay.SelectScaleArray = 'temperature'
example_280vtmDisplay.GlyphType = 'Arrow'
example_280vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_260vtmDisplay = Show(example_260vtm, renderView1)
# trace defaults for the display properties.
example_260vtmDisplay.Representation = 'Surface'
example_260vtmDisplay.ColorArrayName = ['POINTS', '']
example_260vtmDisplay.OSPRayScaleArray = 'temperature'
example_260vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_260vtmDisplay.SelectOrientationVectors = 'velocity'
example_260vtmDisplay.ScaleFactor = 0.2
example_260vtmDisplay.SelectScaleArray = 'temperature'
example_260vtmDisplay.GlyphType = 'Arrow'
example_260vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2140vtmDisplay = Show(example_2140vtm, renderView1)
# trace defaults for the display properties.
example_2140vtmDisplay.Representation = 'Surface'
example_2140vtmDisplay.ColorArrayName = ['POINTS', '']
example_2140vtmDisplay.OSPRayScaleArray = 'temperature'
example_2140vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2140vtmDisplay.SelectOrientationVectors = 'velocity'
example_2140vtmDisplay.ScaleFactor = 0.2
example_2140vtmDisplay.SelectScaleArray = 'temperature'
example_2140vtmDisplay.GlyphType = 'Arrow'
example_2140vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2160vtmDisplay = Show(example_2160vtm, renderView1)
# trace defaults for the display properties.
example_2160vtmDisplay.Representation = 'Surface'
example_2160vtmDisplay.ColorArrayName = ['POINTS', '']
example_2160vtmDisplay.OSPRayScaleArray = 'temperature'
example_2160vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2160vtmDisplay.SelectOrientationVectors = 'velocity'
example_2160vtmDisplay.ScaleFactor = 0.2
example_2160vtmDisplay.SelectScaleArray = 'temperature'
example_2160vtmDisplay.GlyphType = 'Arrow'
example_2160vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2180vtmDisplay = Show(example_2180vtm, renderView1)
# trace defaults for the display properties.
example_2180vtmDisplay.Representation = 'Surface'
example_2180vtmDisplay.ColorArrayName = ['POINTS', '']
example_2180vtmDisplay.OSPRayScaleArray = 'temperature'
example_2180vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2180vtmDisplay.SelectOrientationVectors = 'velocity'
example_2180vtmDisplay.ScaleFactor = 0.2
example_2180vtmDisplay.SelectScaleArray = 'temperature'
example_2180vtmDisplay.GlyphType = 'Arrow'
example_2180vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_220vtmDisplay = Show(example_220vtm, renderView1)
# trace defaults for the display properties.
example_220vtmDisplay.Representation = 'Surface'
example_220vtmDisplay.ColorArrayName = ['POINTS', '']
example_220vtmDisplay.OSPRayScaleArray = 'temperature'
example_220vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_220vtmDisplay.SelectOrientationVectors = 'velocity'
example_220vtmDisplay.ScaleFactor = 0.2
example_220vtmDisplay.SelectScaleArray = 'temperature'
example_220vtmDisplay.GlyphType = 'Arrow'
example_220vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2200vtmDisplay = Show(example_2200vtm, renderView1)
# trace defaults for the display properties.
example_2200vtmDisplay.Representation = 'Surface'
example_2200vtmDisplay.ColorArrayName = ['POINTS', '']
example_2200vtmDisplay.OSPRayScaleArray = 'temperature'
example_2200vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2200vtmDisplay.SelectOrientationVectors = 'velocity'
example_2200vtmDisplay.ScaleFactor = 0.2
example_2200vtmDisplay.SelectScaleArray = 'temperature'
example_2200vtmDisplay.GlyphType = 'Arrow'
example_2200vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2100vtmDisplay = Show(example_2100vtm, renderView1)
# trace defaults for the display properties.
example_2100vtmDisplay.Representation = 'Surface'
example_2100vtmDisplay.ColorArrayName = ['POINTS', '']
example_2100vtmDisplay.OSPRayScaleArray = 'temperature'
example_2100vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2100vtmDisplay.SelectOrientationVectors = 'velocity'
example_2100vtmDisplay.ScaleFactor = 0.2
example_2100vtmDisplay.SelectScaleArray = 'temperature'
example_2100vtmDisplay.GlyphType = 'Arrow'
example_2100vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# show data in view
example_2120vtmDisplay = Show(example_2120vtm, renderView1)
# trace defaults for the display properties.
example_2120vtmDisplay.Representation = 'Surface'
example_2120vtmDisplay.ColorArrayName = ['POINTS', '']
example_2120vtmDisplay.OSPRayScaleArray = 'temperature'
example_2120vtmDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
example_2120vtmDisplay.SelectOrientationVectors = 'velocity'
example_2120vtmDisplay.ScaleFactor = 0.2
example_2120vtmDisplay.SelectScaleArray = 'temperature'
example_2120vtmDisplay.GlyphType = 'Arrow'
example_2120vtmDisplay.ScalarOpacityUnitDistance = 0.02364166797032518

# set scalar coloring
ColorBy(example_2220vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2220vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_20vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_20vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2240vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2240vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2360vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2360vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2260vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2260vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2380vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2380vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2280vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2280vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_240vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_240vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2320vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2320vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2300vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2300vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2400vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2400vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2340vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2340vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2420vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2420vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2440vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2440vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2520vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2520vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2540vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2540vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2460vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2460vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2560vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2560vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2480vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2480vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2580vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2580vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2500vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2500vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2600vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2600vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_280vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_280vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_260vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_260vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2140vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2140vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2160vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2160vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2180vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2180vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_220vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_220vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2200vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2200vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2100vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2100vtmDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(example_2120vtmDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
example_2120vtmDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# set active source
SetActiveSource(example_20vtm)

loading_time = time.time() - t0
print "Time to load = ", loading_time

t1 = time.time()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

render_time = time.time() - t1
print "Render time = ", render_time, " seconds."
print "Frame rate = ", float(10)/float(render_time)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 6.6920463990129]
renderView1.CameraParallelScale = 1.7320290587742815

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
