/*
 * File: 102-python.c
 * written by: 0xAdaugo
 */

#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	// print string object information header
	printf("[.] string object info\n");

	// Check if the object is a valid string object
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}


	//Get the length of the string
	length = ((PyASCIIObject *)(p))->length;

	//Check if the string is compact ASCII or Unicode
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	//Print the length of the string
	printf("  length: %ld\n", length);

	// Print the wide character representation of the string
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}

