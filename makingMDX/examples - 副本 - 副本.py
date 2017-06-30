# -*- coding: utf8 -*-

from __future__ import unicode_literals, print_function, absolute_import, division

# This file contains examples of how to use the different features of the writemdict library.
# Run it with "python examples.py". It will create various .mdx files in the example_output/
# directory.

from writemdict import MDictWriter, encrypt_key
from ripemd128 import ripemd128
import io

asd=(
'<script>$(document).bind("startmyfunc", function() {\r\n'
#+'  alert("heihei");\r\n'
+'  startmy();\r\n'
+'});</script>\r\n'
+'    <!-- Fragment shader program -->\r\n'
+'    <script id="shader-fs" type="x-shader/x-fragment">\r\n'
+'      varying highp vec2 vTextureCoord;\r\n'
+'      varying highp vec3 vLighting;\r\n'
+'      uniform sampler2D uSampler;\r\n'
+'      void main(void) {\r\n'
+'      highp vec4 texelColor = texture2D(uSampler, vec2(vTextureCoord.s, vTextureCoord.t));\r\n'
+'      gl_FragColor = vec4(texelColor.rgb * vLighting, texelColor.a);\r\n'
+'      }\r\n'
+'    </script>\r\n'
+'    \r\n'
+'    <!-- Vertex shader program -->\r\n'
+'    <script id="shader-vs" type="x-shader/x-vertex">\r\n'
+'      attribute highp vec3 aVertexNormal;\r\n'
+'      attribute highp vec3 aVertexPosition;\r\n'
+'      attribute highp vec2 aTextureCoord;\r\n'
+'      uniform highp mat4 uNormalMatrix;\r\n'
+'      uniform highp mat4 uMVMatrix;\r\n'
+'      uniform highp mat4 uPMatrix;\r\n'
+'      varying highp vec2 vTextureCoord;\r\n'
+'      varying highp vec3 vLighting;\r\n'
+'      void main(void) {\r\n'
+'        gl_Position = uPMatrix * uMVMatrix * vec4(aVertexPosition, 1.0);\r\n'
+'        vTextureCoord = aTextureCoord;\r\n'
+'        highp vec3 ambientLight = vec3(0.6, 0.6, 0.6);\r\n'
+'        highp vec3 directionalLightColor = vec3(0.5, 0.5, 0.75);\r\n'
+'        highp vec3 directionalVector = vec3(0.85, 0.8, 0.75);\r\n'
+'        highp vec4 transformedNormal = uNormalMatrix * vec4(aVertexNormal, 1.0);\r\n'
+'        highp float directional = max(dot(transformedNormal.xyz, directionalVector), 0.0);\r\n'
+'        vLighting = ambientLight + (directionalLightColor * directional);\r\n'
+'      }\r\n'
+'    </script>'
+'<div onload="startmy()">'
#+'<button type="button" onclick="startmy()">Click Me!</button>'
+'<canvas id="glcanvas" width="640" height="480" >'
+'  asdasd'
+'</canvas>'
+'</div>'
+'<div id="the-div">Content</div>'
+'<script>$(document).trigger("startmyfunc");</script>')


# This is the dictionary we will use.
d = {
    "alpha":asd,
    "beta":"Letter <b>beta</b>",
    "gamma":"Capital version is Γ &lt;"}

### Example 4: Uses the Big5 encoding.
outfile = open("example_output/big5.mdx", "wb")
writer = MDictWriter(d, 
                     "Big5 dictionary",
                     "This is a test for the \"Big5\" encoding.",
                     encoding="big5")
writer.write(outfile)
outfile.close()







