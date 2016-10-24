# Citatr
SPA that converts legal case citations between adopted formats

## Instructions
1. Copy/paste the Westlaw case citation into the box above.
2. Enter the pages referenced into the Pages text box.
3. Click 'Convert Citation' to generate Bluebook citation.
4. Copy the generated Bluebook citation. Done!

## Application
Citatr was built on the Python microframework Flask. Begin the server with the command:
`python run.py`

Input citation is received as string input and passed to the server via Ajax. The server runs the input through the conversion alorithm and returns the final citation as a json object. The application displays the final citation with no CSS styling so users can copy/paste the raw text easily.

The conversion algorithm is located in [citatr/converter_pkg/converter.py](citatr/converter_pkg/converter.py).
