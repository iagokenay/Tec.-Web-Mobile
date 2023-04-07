import pickle

pratos = [1, 2, 3]


with open('pratos.pkl', 'wb') as file:
    pickle.dump(pratos, file)