import numpy as np
from qiskit import *
import matplotlib.pyplot as plt

# Creating a quantum circuit based on the conditions
def dj_oracle(case, n):
    oracle_qc = QuantumCircuit(n + 1)
    if case == 'balanced':
        for qubit in range(n):
            oracle_qc.cx(qubit, n)
    if case == 'constant':
        output = np.random.randint(2)
        if output == 1:
            oracle_qc.x(n)
    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = 'Oracle'
    return oracle_gate

def dj_algorithm(n, case='random'):
    dj_circuit = QuantumCircuit(n + 1, n)
    # Setting up the input register
    for qubit in range(n):
        dj_circuit.h(qubit)
    dj_circuit.x(n)
    dj_circuit.h(n)
    if case == 'random':
        random = np.random.randint(2)
        if random == 0:
            case = 'constant'
        else:
            case = 'balanced'
    oracle = dj_oracle(case, n)
    dj_circuit.append(oracle, range(n + 1))
    for i in range(n):
        dj_circuit.h(i)
    dj_circuit.measure(range(n), range(n))
    return dj_circuit

n = 4
dj_circuit = dj_algorithm(n)
dj_circuit.draw('mpl', filename='Deutsch-Jozsa_Algorithm.png')



