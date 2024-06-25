#define GL_GLEXT_PROTOTYPES
#include <GL/gl.h>
#include <GL/glut.h>
#include <cmath>
#include <chrono>
#include <iostream>
#include <sstream>
#include <numeric>
#include <vector>
#include <vecmath.h>
using namespace std;
using namespace std::chrono;

#define BUF_SIZE 256

// Globals

// This is the list of points (3D vectors)
vector<Vector3f> vecv;

// This is the list of normals (also 3D vectors)
vector<Vector3f> vecn;

// This is the list of faces (indices into vecv and vecn)
vector<vector<unsigned> > vecf;


// You will need more global variables to implement color and position changes
// Index for choosing colors, effect takes 0.5 second
int colorIndex = 0;
GLfloat originColor[4] = {.0f, .0f, .0f, .0f}, curColor[4];
const auto dT = 2ms, transT = 500ms;
auto startT = system_clock::now();
auto targetT = startT;

// State and angle for spinning perspectives
bool viewSpinning = false;
bool lightSpinning = false;
double dtheta = 1.0f, viewTheta = 0.0f, lightTheta = 0.0f, mtheta = sqrt(2);

// Data for VBOs
vector<Vector3f> drawv;
vector<Vector3f> drawn;
vector<unsigned> drawf;
GLuint vbov, vbon, vboi;

// Lighting coordinate
GLfloat baseLt0pos[] = {1.0f, 1.0f, 5.0f, 1.0f};

// These are convenience functions which allow us to call OpenGL 
// methods on Vec3d objects
inline void glVertex(const Vector3f &a) 
{ glVertex3fv(a); }

inline void glNormal(const Vector3f &a) 
{ glNormal3fv(a); }

// This function is called whenever a "Normal" key press is received.
void keyboardFunc( unsigned char key, int x, int y )
{
    switch ( key )
    {
    case 27: // Escape key
        exit(0);
        break;
    case 'c':
        // add code to change color here
        for (int i = 0; i < 4; i++)
            originColor[i] = curColor[i];
		colorIndex = (colorIndex + 1) % 4;
        targetT = chrono::high_resolution_clock::now() + transT;
        break;
    case 'r':
        viewSpinning = !viewSpinning;
        break;
    case 't':
        lightSpinning = !lightSpinning;
        break;
    case '+':
        if (dtheta < 20)
            dtheta *= mtheta;
        break;
    case '-':
        if (dtheta > 0.2)
            dtheta /= mtheta;
        break;
    default:
        cout << "Unhandled key press " << key << "." << endl;        
    }

	// this will refresh the screen so that the user sees the color change
    glutPostRedisplay();
}

// This function is called whenever a "Special" key press is received.
// Right now, it's handling the arrow keys.
void specialFunc( int key, int x, int y )
{
    switch ( key )
    {
    case GLUT_KEY_UP:
        // add code to change light position
        baseLt0pos[1] += 0.5f;
		break;
    case GLUT_KEY_DOWN:
        // add code to change light position
        baseLt0pos[1] -= 0.5f;
		break;
    case GLUT_KEY_LEFT:
        // add code to change light position
        baseLt0pos[0] -= 0.5f;
		break;
    case GLUT_KEY_RIGHT:
        // add code to change light position
        baseLt0pos[0] += 0.5f;
		break;
    }

	// this will refresh the screen so that the user sees the light position
    glutPostRedisplay();
}

// This function is responsible for displaying the object.
void drawScene(void)
{
    int i;

    // Clear the rendering window
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    // Rotate the image
    glMatrixMode( GL_MODELVIEW );  // Current matrix affects objects positions
    glLoadIdentity();              // Initialize to the identity

    // Position the camera at [0,0,5], looking at [0,0,0],
    // with [0,1,0] as the up direction.
    gluLookAt(5.0 * sin(viewTheta), 0.0, 5.0 * cos(viewTheta),
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0);

    // Set material properties of object

	// Here are some colors you might use - feel free to add more
    GLfloat diffColors[4][4] = { {0.5, 0.5, 0.9, 1.0},
                                 {0.9, 0.5, 0.5, 1.0},
                                 {0.5, 0.9, 0.3, 1.0},
                                 {0.3, 0.8, 0.9, 1.0} };    

    double t = duration_cast<duration<long double, nano>>(chrono::high_resolution_clock::now() - (targetT - transT)) / transT;
    t = min(t, 1.0);
    double x = -2.0 * t * t * t + 3 * t * t;
    for (int i = 0; i < 4; i++)
        curColor[i] = originColor[i] * (1 - x) + diffColors[colorIndex][i] * x;  
    
	// Here we use the first color entry as the diffuse color
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, curColor);

	// Define specular color and shininess
    GLfloat specColor[] = {1.0, 1.0, 1.0, 1.0};
    GLfloat shininess[] = {100.0};

	// Note that the specular color and shininess can stay constant
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specColor);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shininess);
  
    // Set light properties

    // Light color (RGBA)
    GLfloat Lt0diff[] = {1.0,1.0,1.0,1.0};
    // Light position
	GLfloat Lt0pos[] = {baseLt0pos[0] * cos(lightTheta) + baseLt0pos[2] * sin(lightTheta), 
                        baseLt0pos[1], 
                        baseLt0pos[0] * -sin(lightTheta) + baseLt0pos[2] * cos(lightTheta),
                        baseLt0pos[3]};

    glLightfv(GL_LIGHT0, GL_DIFFUSE, Lt0diff);
    glLightfv(GL_LIGHT0, GL_POSITION, Lt0pos);

	// This GLUT method draws a teapot.  You should replace
	// it with code which draws the object you loaded.
	// glutSolidTeapot(1.0);
    // for (auto face : vecf)
    // {
    //     glBegin(GL_TRIANGLES);
    //     glNormal3fv(vecn[face[1]]);
    //     glVertex3fv(vecv[face[0]]);
    //     glNormal3fv(vecn[face[3]]);
    //     glVertex3fv(vecv[face[2]]);
    //     glNormal3fv(vecn[face[5]]);
    //     glVertex3fv(vecv[face[4]]);
    //     glEnd();
    // }

    // draw
    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_NORMAL_ARRAY);
    glDrawElements(GL_TRIANGLES, drawf.size(), GL_UNSIGNED_INT, 0);
    glDisableClientState(GL_VERTEX_ARRAY);
    glDisableClientState(GL_NORMAL_ARRAY);

    // Dump the image to the screen.
    glutSwapBuffers();
}

// Initialize OpenGL's rendering modes
void initRendering()
{
    glEnable(GL_DEPTH_TEST);   // Depth testing must be turned on
    glEnable(GL_LIGHTING);     // Enable lighting calculations
    glEnable(GL_LIGHT0);       // Turn on light #0.

    glGenBuffers(1, &vbov);
    glGenBuffers(1, &vboi);
    glBindBuffer(GL_ARRAY_BUFFER, vbov);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboi);
    glBufferData(GL_ARRAY_BUFFER, sizeof(Vector3f) * (drawv.size() + drawn.size()), 0, GL_STATIC_DRAW);
    unsigned offset = 0;
    glBufferSubData(GL_ARRAY_BUFFER, offset, sizeof(Vector3f) * drawv.size(), drawv.data());
    glVertexPointer(3, GL_FLOAT, 0, (void*)0);
    offset += sizeof(Vector3f) * drawv.size();
    glBufferSubData(GL_ARRAY_BUFFER, offset, sizeof(Vector3f) * drawn.size(), drawn.data());
    glNormalPointer(GL_FLOAT, 0, (void*)offset);
    offset += sizeof(Vector3f) * drawn.size();
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(unsigned) * drawf.size(), drawf.data(), GL_STATIC_DRAW);

    // glVertexPointer(3, GL_FLOAT, 0, drawv.data());
    // glNormalPointer(GL_FLOAT, 0, drawn.data());
}

// Called when the window is resized
// w, h - width and height of the window in pixels.
void reshapeFunc(int w, int h)
{
    // Always use the largest square viewport possible
    if (w > h) {
        glViewport((w - h) / 2, 0, h, h);
    } else {
        glViewport(0, (h - w) / 2, w, w);
    }

    // Set up a perspective view, with square aspect ratio
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    // 50 degree fov, uniform aspect ratio, near = 1, far = 100
    gluPerspective(50.0, 1.0, 1.0, 100.0);
}

void loadInput()
{
    // prepend for the ease of 1-indexed entries
	vecv.resize(1);
    vecn.resize(1);
    vecf.clear();

    char buf[BUF_SIZE];
    while (cin.getline(buf, BUF_SIZE))
    {
        stringstream ss(buf);
        string command;
        ss >> command;
        if (command == "v")
        {
            Vector3f v;
            ss >> v[0] >> v[1] >> v[2];
            vecv.emplace_back(v);
        }
        else if(command == "vn")
        {
            Vector3f v;
            ss >> v[0] >> v[1] >> v[2];
            vecn.emplace_back(v);
        }
        else if(command == "f")
        {
            vector<unsigned> face(6);
            char slash;
            unsigned ignore;
            ss >> face[0] >> slash >> ignore >> slash >> face[1]  >>
                  face[2] >> slash >> ignore >> slash >> face[3]  >>
                  face[4] >> slash >> ignore >> slash >> face[5] ;
            vecf.emplace_back(face);
        }
    }
    
    for (auto face : vecf)
    {
        drawn.emplace_back(vecn[face[1]]);
        drawv.emplace_back(vecv[face[0]]);
        drawn.emplace_back(vecn[face[3]]);
        drawv.emplace_back(vecv[face[2]]);
        drawn.emplace_back(vecn[face[5]]);
        drawv.emplace_back(vecv[face[4]]);
    }
    drawf.resize(3 * vecf.size());
    iota(drawf.begin(), drawf.end(), 0);
}


void refresh(int what)
{
    static auto begin = system_clock::now();
    static int sumLatency = 0;
    static int expCount = 0;

    glutTimerFunc(dT / 1ms, refresh, 0);
    auto end = system_clock::now();
    if (viewSpinning)
    {    
        viewTheta += ((end - begin) / 1.0s) * dtheta;
    }
    if (lightSpinning)
    {
        lightTheta += ((end - begin) / 1.0s) * dtheta;
    }
    begin = end;
    
    // auto measureBegin = system_clock::now();
    glutPostRedisplay();
    // auto measureEnd = system_clock::now();
    // sumLatency += duration_cast<nanoseconds>(measureEnd - measureBegin).count();
    // expCount++;
    // if (expCount % 100 == 0)
    //     std::cout << "Display latency: " << sumLatency / expCount << "ns" << std::endl;
}

// Main routine.
// Set up OpenGL, define the callbacks and start the main loop
int main( int argc, char** argv )
{
    loadInput();

    glutInit(&argc,argv);

    // We're going to animate it, so double buffer 
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH );

    // Initial parameters for window position and size
    glutInitWindowPosition( 60, 60 );
    glutInitWindowSize( 360, 360 );
    glutCreateWindow("Assignment 0");

    // Initialize OpenGL parameters.
    initRendering();

    // Set up callback functions for key presses
    glutKeyboardFunc(keyboardFunc); // Handles "normal" ascii symbols
    glutSpecialFunc(specialFunc);   // Handles "special" keyboard keys
    glutTimerFunc(0, refresh, 0);

     // Set up the callback function for resizing windows
    glutReshapeFunc( reshapeFunc );

    // Call this whenever window needs redrawing
    glutDisplayFunc( drawScene );

    // Start the main loop.  glutMainLoop never returns.
    glutMainLoop( );

    return 0;	// This line is never reached.
}
