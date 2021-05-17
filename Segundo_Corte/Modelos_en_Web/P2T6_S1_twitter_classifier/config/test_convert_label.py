print('------------TEST 01------------')
label = {-1:'Sin sentimiento', 0:'Neutro', 1:'Positivo', 2:'Negativo'}
y = -1
proba = 0.5
print(label[y])


print('------------TEST 02------------')
prediction = 'Neutro'
print('Hola Mundo')
inv_label = {'Sin sentimiento':1, 'Neutro':0, 'Positivo':1, 'Negativo':2}
print(inv_label)
y = inv_label[prediction]
'''
if feedback != 'Aprobado':
    y = prediction
'''
print(y)
