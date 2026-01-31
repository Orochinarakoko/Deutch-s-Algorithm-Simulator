from qiskit import *
from qiskit_aer import *
import random

qc = QuantumCircuit(2,2) # initalise the algorithm with 2 qubits and 1 classical bits

qc.x(1) # set the state of the 2nd qubit to 0|0> + 1|1>
qc.h(0)
qc.h(1)


func = random.randint(1,4)

if func == 1: # constant 0 function - flip 2nd qubit from |1> to |0>

    print("CONSTANT ZERO FUNCTION")

elif func ==2: # constant 1 function - no need to flip 2nd qubit

    print("CONSTANT ONE FUNCTION")
    qc.x(1)

elif func == 3: # identity function - entangle the 2nd qubit with the 1st such that 1st qubit = 2nd qubit when read out

    print("IDENTITY FUNCTION")

    qc.cx(0,1)
else: # not function - entangle 1st qubit with 2nd qubit such that qubit 2 = NOT(qubit 1) when read out from memory

    print("NOT FUNCTION")


    qc.cx(0,1)
    qc.x(1)

qc.h(0)

qc.measure([0,1],[0,1]) # measure qbit 2 store to cbit 1



simulator = Aer.get_backend('qasm_simulator')

optqc = transpile(qc,simulator)

test = simulator.run(optqc , shots = 100)

result = test.result()

print(result.get_counts())
