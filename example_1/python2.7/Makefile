PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)

# location of the Boost Python include files and library

BOOST_INC = /usr/include
BOOST_LIB = /usr/lib

# compile mesh classes
TARGET = hello_ext

$(TARGET).so: $(TARGET).o
	g++ -shared -Wl,--export-dynamic $(TARGET).o -L $(BOOST_LIB) -l boost_python -L /usr/lib/python$(PYTHON_VERSION)/config -l python$(PYTHON_VERSION) -o $(TARGET).so

$(TARGET).o: $(TARGET).c
	g++ -I $(PYTHON_INCLUDE) -I $(BOOST_INC) -fPIC -c $(TARGET).c
