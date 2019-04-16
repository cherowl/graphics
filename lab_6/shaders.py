vertexShader = """
    uniform mat4 modelMatrix;

    varying vec4 vertex_color;
    
    void main(){
        gl_Position = modelMatrix * gl_ModelViewProjectionMatrix * gl_Vertex;
        vertex_color = gl_Color;
    }
"""


fragmentShader = """
    //varying vec4 vertex_color;
    void main() {
        gl_FragColor = vec4(1,0,0,1); //vertex_color;
}"""