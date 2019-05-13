vertexShader = """
    uniform mat4 MVP;

    void main() {
        gl_Position = MVP * vec4(vec3(gl_Vertex), 1.0);
    }
"""

fragmentShader = """
    uniform vec4 fragmentColor;

    void main() {
        gl_FragColor = fragmentColor;   
    }
"""