#include <python.h>
#include <stdio.h>
/**
 * print_python_list - prints the information of a python list
 *
 * @p: pointer to a python object
 *
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int i;
	PyListObject *obj = (PyListObject *) p;

	size = PyList_Size(p);

	printf("[*]Size of the Python List = %d\n", size);
	printf("[*]Allocated = %d\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", PY_TYPE(obj->on_item[i]->tp_name));
	}
}
