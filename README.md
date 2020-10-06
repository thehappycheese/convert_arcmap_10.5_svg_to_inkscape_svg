# Convert ArcMap 10.5 svg to Inkscape svg

A snippet for converting SVGs created by the 'Export Map' command in ArcMap 10.5 to SVGs that have working layers in Inkscape.

All it does is add the inkscape and sodipodi namespaces to the root <svg/> element and the attribute inkscape:groupmode="layer" to all top level <g/> elements.

It is designed so that you can drag and drop svg files onto the .py file. If this doesnt work you will need to invoke the script from the command line:

```bat
python convert.py %pathtosvgfile%
```
