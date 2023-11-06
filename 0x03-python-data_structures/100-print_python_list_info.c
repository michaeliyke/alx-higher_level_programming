#include "lists.h"
#include "Python.h"

void hello()
{
	printf("\n\n Hello from C Programming\n\n");
}

/**
 * print_python_list_info - prints info about a python List type
 * @p: the input list
 *
 * Return: void
 * NOTE: This function is to be called from python.
 * For that to work, we should compile it with the following command:
 * gcc -shared -fPIC -o mylib.so -I /usr/include/python3.8 ...
 * ... 100-ptint_python_list_info.c
 * Above creates the DLL file mylib.so which is to be loaded and used in python
 * through the ctype library. Before attempting this, ensure to install below:
 * sudo apt-get install python3-dev - you must already have python3 installed
 * before running above command. Python code below
 *
 * import ctypes
 * lib = ctypes.CDLL("./mylib.so")
 * lib.printlist.argtypes = [ctypes.py_object]
 * l = ["One", "Two", "Three", "Four"]
 * lib.printlist(l)
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list; /* Base of all python objects, to be casted */
	Py_ssize_t i;	    /* Just the regular ssize_t which is signed long int */

	list = (PyListObject *)p;
	printf(
	    "[*] Size of the Python %s = %ld\n",
	    list->ob_base.ob_base.ob_type->tp_name,
	    list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < list->ob_base.ob_size; i++)
	{
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	}
}
