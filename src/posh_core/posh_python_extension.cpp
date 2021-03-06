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
   return Py_BuildValue("b", posh_preflight_rule(rule));
}

static PyObject *
train(PyObject *self, PyObject *args)
{
   char *system_name;
   char *args_list;
   if (!PyArg_ParseTuple(args, "ss", &system_name, &args_list)) {
      return NULL;
   }
   return Py_BuildValue("ss", posh_train(system_name, args_list));
}


static PyMethodDef Methods[] = {
    {"get_answer",  get_answer, METH_VARARGS, "The meaning of life."},
    {"prefligt_rule", preflight_rule, METH_VARARGS, "Preflight syntax rule"},
    {"train", train, METH_VARARGS, "Train a system"},
    
    {NULL, NULL, 0, NULL}
};

#ifdef python2

PyMODINIT_FUNC
initcore(void) {
  (void) Py_InitModule("core", Methods);
}

#else

static struct PyModuleDef cModPyDem =
{
    PyModuleDef_HEAD_INIT,
    "core", /* name of module */
    "POSH Syntax Parser",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    Methods
};

PyMODINIT_FUNC 
PyInit_cModPyDem(void)
{
    return PyModule_Create(&cModPyDem);
}

#endif