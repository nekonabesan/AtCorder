CC = g++
CFLAGS =

TARGET = main
SRCS = main.cpp
OBJS = $(SRCS:.cpp=.o)

INCDIR = 

LIBDIR =

LIBS =

$(TARGET): $(OBJS)
	$(CC) -o $@ $^ $(LIBDIR) $(LIBS)

$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) $(INCDIR) -c $(SRCS)

all: clean $(OBJS) $(TARGET)

clean:
	-rm -f $(OBJS) $(TARGET) *.d

