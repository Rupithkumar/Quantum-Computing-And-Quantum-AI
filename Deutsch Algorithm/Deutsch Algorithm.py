from qiskit import *
import matplotlib.pyplot as plt

#crating a circuit with 2 qubits and 1 classical qubit
qc=QuantumCircuit(2,1)
qc.x(1)
qc.h([0,1])
qc.cx(0,1)
qc.h(0)
#Measure the value
qc.measure(0,0)
#draw the circuit diagram created
qc.draw('mpl',filename='Result')