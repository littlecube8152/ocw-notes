INCFLAGS  = -I /usr/include/GL
INCFLAGS += -I ./include/vecmath

LINKFLAGS  = -lglut -lGL -lGLU
LINKFLAGS += -L lib -lvecmath

CFLAGS    = -O2
CC        = g++
SRCS      = main.cpp
OBJS      = $(SRCS:.cpp=.o)
PROG      = a0

LIBSRCS   = $(wildcard vecmath/*.cpp)
LIBOBJS   = $(LIBSRCS:.cpp=.o)
LIB       = lib/libvecmath.a

all: $(LIB) $(SRCS) $(PROG)

$(PROG): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $@ $(INCFLAGS) $(LINKFLAGS)

.cpp.o:
	$(CC) $(CFLAGS) $< -c -o $@ $(INCFLAGS)

depend:
	makedepend $(INCFLAGS) -Y $(SRCS)

$(LIB): $(LIBOBJS)
	@mkdir -p lib
	ar rcs $(LIB) $(LIBOBJS)

clean:
	rm $(OBJS) $(PROG) $(LIB) $(LIBOBJS)
	@rmdir lib