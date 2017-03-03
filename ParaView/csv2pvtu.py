#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# set active view
SetActiveView(None)

CreateLayout('Layout #1')

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1205, 806]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 0
renderView1.Background = [0.32, 0.34, 0.43]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(0, renderView1)

# create a new 'CSV Reader'
a10linescsv = CSVReader(FileName=['/home/faiz89/10lines.csv'])

# Properties modified on a10linescsv
a10linescsv.HaveHeaders = 0
a10linescsv.FieldDelimiterCharacters = ' '

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# place view in the layout
layout1.AssignView(2, spreadSheetView1)

# show data in view
a10linescsvDisplay = Show(a10linescsv, spreadSheetView1)
# trace defaults for the display properties.
a10linescsvDisplay.FieldAssociation = 'Row Data'
a10linescsvDisplay.CompositeDataSetIndex = [0]

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=a10linescsv)
tableToPoints1.XColumn = 'Field 0'
tableToPoints1.YColumn = 'Field 0'
tableToPoints1.ZColumn = 'Field 0'

# Properties modified on tableToPoints1
tableToPoints1.YColumn = 'Field 1'
tableToPoints1.ZColumn = 'Field 2'

# show data in view
tableToPoints1Display = Show(tableToPoints1, spreadSheetView1)
# trace defaults for the display properties.
tableToPoints1Display.CompositeDataSetIndex = [0]

# hide data in view
Hide(a10linescsv, spreadSheetView1)

# create a new 'Glyph'
glyph1 = Glyph(Input=tableToPoints1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'Field 3']
glyph1.Vectors = ['POINTS', 'None']
glyph1.ScaleFactor = 0.14907
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1.GlyphType
glyph1.GlyphType.GlyphType = 'Vertex'

# Properties modified on glyph1
glyph1.GlyphType = '2D Glyph'

# Properties modified on glyph1.GlyphType
glyph1.GlyphType.GlyphType = 'Vertex'

# show data in view
glyph1Display = Show(glyph1, spreadSheetView1)
# trace defaults for the display properties.
glyph1Display.CompositeDataSetIndex = [0]

# create a new 'D3'
d31 = D3(Input=glyph1)

# show data in view
d31Display = Show(d31, spreadSheetView1)
# trace defaults for the display properties.
d31Display.CompositeDataSetIndex = [0]

# hide data in view
Hide(glyph1, spreadSheetView1)

# save data
SaveData('/home/faiz89/test4.pvtu', proxy=d31, DataMode='Binary')

#### saving camera placements for all active views

# current camera placement for renderView1

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).