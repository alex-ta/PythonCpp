1) To enable C compilation you have to setup distutils.
2) On Windows set the compiler to mscv
C:\Users\Alex\Anaconda3\Lib\distutils\distutils.cfg 
[build]
compiler=msvc

[build_ext]
compiler=msvc
[https://stackoverflow.com/questions/24683305/python-cant-install-packages-typeerror-unorderable-types-nonetype-str]
3)Create a C file following this guid (3.*)
[https://stackoverflow.com/questions/38155988/building-python-c-extension/38163356]

#include <Python.h>

static PyObject* say_hello(PyObject* self, PyObject* args)
{
    const char* name;

    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;

    printf("Hello %s!\n", name);

    Py_RETURN_NONE;
}

static PyMethodDef HelloMethods[] =
{
     {"say_hello", say_hello, METH_VARARGS, "Greet somebody."},
     {NULL, NULL, 0, NULL}
};

static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "hello", /* module name */
    NULL, /* module documentation, may be NULL */
    -1,
    HelloMethods /* the methods array */
};

PyMODINIT_FUNC PyInit_hello(void)
{
    return PyModule_Create(&hellomodule);
}

saved under hello.c

4)Compiling the C file with a setup file in python
create a setup file:
from distutils.core import setup, Extension

setup(name = "hello", version = "1.0",
  ext_modules = [
    Extension("hello", ["hello.c"])
    ]
)

compile it
python setup install

https://docs.python.org/2/distutils/builtdist.html

5)Run the module
python
>> import hello
>> hello.say_hello("a")
