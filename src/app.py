import streamlit as st
import numpy as np
import math


st.header('Entradas')
entradas = st.slider("Entradas",1, 10)
  
x = []

for i in range(entradas):
 x.append(i)
 x[i] = st.number_input(f"entrada{i}")
 st.text(f"x = {x}") 

st.header('Pesos')
pesos = []

for i in range(entradas):
 pesos.append(i)
 pesos[i] = st.number_input(f"pesos{i}")
 st.text(f"pesos = {pesos} ")

st.subheader("Sesgo")
bias = st.number_input("Introduce el valor del sesgo")

st.subheader("Función de activación")
func_option = st.selectbox(
        'Elige la función de activación',
        ('Sigmoide', 'ReLU', 'Tangente hiperbólica'))
function = {'Sigmoide': 'sigmoid', 'ReLU': 'relu', 'Tangente hiperbólica': 'tanh'}

class Neuron:
  def __init__(self, weights, bias, function):
    self.w = weights
    self.b = bias
    self.function = function
    self.y = 0
  def run(self, input_data):
    x = np.array(input_data)
    w = np.array(self.w)

    if x.size != w.size:
       print('los vectores no son iguales')
    else:
      b = self.b
      self.y = float(np.dot(x, w) + b)

    if self.function == 'relu':
      return self.__relu(self.y)
    elif self.function == 'sigmoid':
     return self.__sigmoid(self.y)
    elif self.function == 'tanh':
      return self.__tanh(self.y)

  def changeBias(self, bias):
    self.b = bias
  
  def __relu(self, y):
    return 0 if y < 0 else y
  
  def __sigmoid(self, y):
    return 1 / (1 + math.e ** -y)
  
  def __tanh(self, y):
    return math.tanh(y)

if st.button("Calcular la salida"):
    Neurona = Neuron(weights=pesos, bias=bias, function=function[func_option])
    st.text(f"La salida de la neurona es {Neurona.run(input_data=x)}")