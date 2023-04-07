import pickle


with open('pratos.pkl', 'rb') as file:
    novoprato = pickle.load(file)


print(novoprato)