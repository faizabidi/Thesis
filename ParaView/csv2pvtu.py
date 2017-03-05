import sys
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

script, FILENAME = sys.argv

# create a new 'CSV Reader'
reader = CSVReader(FileName=[FILENAME])

# Properties modified on reader
reader.HaveHeaders = 0
reader.FieldDelimiterCharacters = ' '

# Create a new 'SpreadSheet View'
spreadSheetView2 = CreateView('SpreadSheetView')
spreadSheetView2.ColumnToSort = ''
spreadSheetView2.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView2.ViewSize = [400, 400]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(4, spreadSheetView2)

# show data in view
readerDisplay = Show(reader, spreadSheetView2)
# trace defaults for the display properties.
readerDisplay.FieldAssociation = 'Row Data'
readerDisplay.CompositeDataSetIndex = [0]

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=reader)
tableToPoints1.XColumn = 'Field 0'
tableToPoints1.YColumn = 'Field 0'
tableToPoints1.ZColumn = 'Field 0'

# Properties modified on tableToPoints1
tableToPoints1.YColumn = 'Field 1'
tableToPoints1.ZColumn = 'Field 2'

# show data in view
tableToPoints1Display = Show(tableToPoints1, spreadSheetView2)
# trace defaults for the display properties.
tableToPoints1Display.CompositeDataSetIndex = [0]

# hide data in view
Hide(reader, spreadSheetView2)

# create a new 'Glyph'
glyph1 = Glyph(Input=tableToPoints1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'Field 3']
glyph1.Vectors = ['POINTS', 'None']
glyph1.ScaleFactor = 0.75536
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1.GlyphType
#glyph1.GlyphType.GlyphType = 'Vertex'

# Properties modified on glyph1
glyph1.GlyphType = '2D Glyph'

# Properties modified on glyph1.GlyphType
glyph1.GlyphType.GlyphType = 'Vertex'

# show data in view
glyph1Display = Show(glyph1, spreadSheetView2)
# trace defaults for the display properties.
glyph1Display.CompositeDataSetIndex = [0]

# create a new 'Glyph'
glyph2 = Glyph(Input=glyph1,
    GlyphType='Arrow')
glyph2.Scalars = ['POINTS', 'Field 3']
glyph2.Vectors = ['POINTS', 'None']
glyph2.ScaleFactor = 0.7527699947357178
glyph2.GlyphTransform = 'Transform2'

# set active source
SetActiveSource(glyph1)

# destroy glyph2
Delete(glyph2)
del glyph2

# create a new 'D3'
d31 = D3(Input=glyph1)

# show data in view
d31Display = Show(d31, spreadSheetView2)
# trace defaults for the display properties.
d31Display.CompositeDataSetIndex = [0]

# hide data in view
Hide(glyph1, spreadSheetView2)

# save data
SaveData('%s.pvtu' %FILENAME, proxy=d31, DataMode='Ascii')

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
