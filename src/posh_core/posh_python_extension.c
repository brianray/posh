#include <Python.h>

static PyObject *
get_answer(PyObject *self, PyObject *args)
{
    return Py_BuildValue("i", 42);
}

static PyMethodDef Methods[] = {
    {"get_answer",  get_answer, METH_VARARGS, "The meaning of life."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initcore(void) {
  (void) Py_InitModule("core", Methods);
}