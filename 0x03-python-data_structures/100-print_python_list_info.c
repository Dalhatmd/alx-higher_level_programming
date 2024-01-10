#include <python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	if (p && PyList_Check(p))
	{
		PyListObject *listobj = (PyListObject *) p;
		printf("[*] Size of the Python Liist = %d\n", PyList_Size(p));
		printf("[*] Size allocated = %d\n", listobj->ob_base.ob_size);
	}
}
