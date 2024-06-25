# Homework 0
## Environment Setup

On linux, we need the OpenGL library. Since original [GLUT](https://www.opengl.org/resources/libraries/glut/) has been discontinued for 20 years, we use FreeGLUT as they suggest:

```bash
sudo apt install freeglut3-dev
ls /usr/include/GL  # test it out if we installed it correctly
```

However, you will find that the [Starter code (GZ)](https://ocw.mit.edu/courses/6-837-computer-graphics-fall-2012/resources/zero-tar/) is not complete, that is because the library is on MIT's workstation (which we do not have access to). Hence, also download [Starter code for VC++ 2010 (ZIP)](https://ocw.mit.edu/courses/6-837-computer-graphics-fall-2012/resources/zero/) because it contains the library `vecmath`. Now we have the source code, we just needs to compile it. Thus, I did some modification of the makefile:
```make
LIBSRCS   = $(wildcard vecmath/*.cpp)
LIBOBJS   = $(LIBSRCS:.cpp=.o)
LIB       = lib/libvecmath.a

all: $(LIB) $(SRCS) $(PROG)

$(LIB): $(LIBOBJS)
	@mkdir -p lib
	ar rcs $(LIB) $(LIBOBJS)

clean:
	rm $(OBJS) $(PROG) $(LIB) $(LIBOBJS)
	@rmdir lib
```
Adding or swapping out the corresponding enables you to build the library at your computer for just running `make`.

## Bonus
### Vertex Array
Reference: [http://www.songho.ca/opengl/gl_vertexarray.html]

Vertex array is basically declearing an array of vertices and tell OpenGL to render it.

To declare it, use
```cpp
glVertexPointer(3, GL_FLOAT, 0, drawv.data());
glNormalPointer(GL_FLOAT, 0, drawn.data());
```
`glVertexPointer` takes dimension, type, stride (which is the additional spacing bewteen entries), and the array pointer. `glNormalPointer` on the other hand don't take dimension (I guess that is because normal vectors always have the same dimension as vertices). 

The taken data are coordinates and normal vectors, which should match index by index, that is because OpenGL vertices are formed by coordinates, normal, and other attributes. Hence, to pass these data, we have to treat same coords but different normal as different vertices.

In the homework, do not call it in `loadInput` as OpenGL has not be initialized yet, so these calls will be meaningless.

Regardless of using vertex array or VBO, the rendering code is changed to:
```cpp
glEnableClientState(GL_VERTEX_ARRAY);
glEnableClientState(GL_NORMAL_ARRAY);
glDrawElements(GL_TRIANGLES, drawf.size(), GL_UNSIGNED_INT, 0);
glDisableClientState(GL_VERTEX_ARRAY);
glDisableClientState(GL_NORMAL_ARRAY);
```
Which means we enable the vertex and normal attributes, and then render, and finally disable them.


### VBO (Vertex Buffer Object)
Reference: [https://stackoverflow.com/questions/41360736/gldrawelements-not-drawing], [http://www.songho.ca/opengl/gl_vbo.html]

VBO is the shorthand of vertex buffer object. Basically, it is a buffer holding the desired objects. The advantage is that the buffer only needs to be passed once to the GPU in order to render all frames, thus yielding better performance. To declare a VBO, we can use
```cpp
glGenBuffers(1, &vbov);
```
To generate one VBO with id stored at `vbov`. Passing higher count and pointer to array can initialize multiple at the same time. These buffer has to be binded for certain usages:
```cpp
glBindBuffer(GL_ARRAY_BUFFER, vbov);
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboi);
```
And then, initialized.