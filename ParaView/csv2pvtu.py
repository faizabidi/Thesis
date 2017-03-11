import sys
from paraview.simple import *

# Take argument as filename to be converted
script, FILENAME = sys.argv

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'CSV Reader'
reader = CSVReader(FileName=[FILENAME])

# Properties modified on reader
reader.HaveHeaders = 0
reader.FieldDelimiterCharacters = ' '

# get active view
#spreadSheetView2 = GetActiveViewOrCreate('SpreadSheetView')
# uncomment following to set a specific view size
# spreadSheetView2.ViewSize = [400, 400]

# show data in view
#readerDisplay = Show(reader, spreadSheetView2)
# trace defaults for the display properties.
#readerDisplay.FieldAssociation = 'Row Data'
#readerDisplay.CompositeDataSetIndex = [0]

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=reader)
tableToPoints1.XColumn = 'Field 0'
tableToPoints1.YColumn = 'Field 0'
tableToPoints1.ZColumn = 'Field 0'

# Properties modified on tableToPoints1
tableToPoints1.YColumn = 'Field 1'
tableToPoints1.ZColumn = 'Field 2'

# show data in view
#tableToPoints1Display = Show(tableToPoints1, spreadSheetView2)
# trace defaults for the display properties.
#tableToPoints1Display.CompositeDataSetIndex = [0]

# hide data in view
#Hide(reader, spreadSheetView2)

# create a new 'Glyph'
glyph1 = Glyph(Input=tableToPoints1,
    GlyphType='2D Glyph')
glyph1.GlyphType.GlyphType = 'Vertex'
glyph1.GlyphMode = 'All Points'
glyph1.Scalars = ['POINTS', 'Field 3']
glyph1.Vectors = ['POINTS', 'None']
glyph1.ScaleFactor = 0.75536
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1.GlyphType
glyph1.GlyphType.GlyphType = 'Vertex'

# Properties modified on glyph1
#glyph1.GlyphType = '2D Glyph'
#glyph1.GlyphMode = 'All Points'

# Properties modified on glyph1.GlyphType
#glyph1.GlyphType.GlyphType = 'Vertex'

# show data in view
#glyph1Display = Show(glyph1, spreadSheetView2)
# trace defaults for the display properties.
#glyph1Display.CompositeDataSetIndex = [0]

# create a new 'D3'
d31 = D3(Input=glyph1)

# show data in view
#d31Display = Show(d31, spreadSheetView2)
# trace defaults for the display properties.
#d31Display.CompositeDataSetIndex = [0]

# hide data in view
#Hide(glyph1, spreadSheetView2)

# save data
SaveData('%s.pvtu' %FILENAME, proxy=d31, DataMode='Ascii')

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

