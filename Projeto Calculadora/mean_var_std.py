import numpy as np

def calculate(lista):
    # Verifica se a lista contém 9 números
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converte a lista em uma matriz 3x3 usando Numpy
    array = np.array(lista).reshape(3, 3)
    
    # Calcula os valores para linhas, colunas e matriz achatada
    calculos = {
        'mean': [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array).tolist()],
        'variance': [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array).tolist()],
        'standard deviation': [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array).tolist()],
        'max': [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array).tolist()],
        'min': [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array).tolist()],
        'sum': [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array).tolist()]
    }

    return calculos