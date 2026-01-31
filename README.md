# Deutch's-Algorithm-Simulator
A python script using the IBM Qiskit module demonstrating how a quantum computer can be used to determine if a function is a constant or variable in only 1 call.

Imagine you had to determine, from one of 4 functions - NOT (flip input bit), IDENTITY (keep input bit constant), CONTANT 1 (return 1) and CONSTANT 0 (return 0) - whether the function was a constant (CONSTANT 0/1) or variable (NOT and IDENTITY). You would need to try the function at least twice. For example:

-Input a 0 , and f(0) = 1 . We can determine that the function could be either CONSTANT 1 , or NOT, but we cannot determine which, and thus cannot conclude whether the function is constant or variable
-Input a 1, and f(1) = 0 . Only now can we determine that the function is variable (NOT). This is the case for all 4 of the functions.


However, David Deutsch and developed an algorithm that can determine whether the function is constant or variable in 1 query, using quantum computing. Using a series of gates (mathematically reperesented by martices), the properties of each function can be manipulated such that after inputting 2 qubits in to Deutsch's algorithm, one of the qubits will always return 0 if the function is variable or 1 if the function is constant
