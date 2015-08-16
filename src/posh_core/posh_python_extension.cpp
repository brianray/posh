#include <Python.h>
#include "posh.h"

static PyObject *
get_answer(PyObject *self, PyObject *args)
{
    return Py_BuildValue("i", 42);
}

static PyObject *
preflight_rule(PyObject *self, PyObject *args)
{
   char *rule;
   if (!PyArg_ParseTuple(args, "s", &rule)) {
      return NULL;
   }
   return Py_BuildValue("s", posh_prefligt_rule(rule));
}

static PyMethodDef Methods[] = {
    {"get_answer",  get_answer, METH_VARARGS, "The meaning of life."},
    {"prefligt_rule", preflight_rule, METH_VARARGS, "Preflight syntax rule"},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initcore(void) {
  (void) Py_InitModule("core", Methods);
}