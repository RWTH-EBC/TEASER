#!/usr/bin/env python

""" casadi_neural_network.py: Classes to translate Sequential Keras Models to casadi Functions. """
from typing import Union

from keras import models, layers, Sequential
from casadi import *
from abc import ABC, abstractmethod


class Layer(ABC):
    """
    Single layer of an artificial neural network.
    """

    def __init__(self, layer: layers.Layer):

        self.config: dict = layer.get_config()

        # name
        if 'name' in self.config:
            self.name: str = self.config['name']

        # units
        if 'units' in self.config:
            self.units: int = self.config['units']

        # activation function
        if 'activation' in self.config:
            self.activation: Function = self.get_activation(layer.get_config()['activation'])

        # input / output shape
        self.input_shape = layer.input_shape[1:]
        self.output_shape = layer.output_shape[1:]

        # update the dimensions to two dimensions
        self.update_dimensions()

        # symbolic input layer
        self.input_layer = MX.sym('input_layer', self.input_shape[0], self.input_shape[1])

    def __str__(self):
        attr = list()
        if hasattr(self, 'units'):
            attr.append(f'units={self.units}')

        if hasattr(self, ''):
            attr.append(f'activation{self.activation}')

        return f'{self.__class__.__name__}({", ".join(attr)})'

    def __repr__(self):

        attr = list()
        if hasattr(self, 'units'):
            attr.append(f'units={self.units}')

        if hasattr(self, ''):
            attr.append(f'activation{self.activation}')

        return f'{self.__class__.__name__}({", ".join(attr)})'

    def summary(self):

        ret = ''

        if hasattr(self, 'units'):
            ret += f'\tunits:\t\t\t\t{self.units}\n'
        if hasattr(self, 'activation'):
            ret += f'\tactivation:\t\t\t{self.activation.__str__()}\n'
        if hasattr(self, 'recurrent_activation'):
            ret += f'\trec_activation:\t\t{self.recurrent_activation.__str__()}\n'
        ret += f'\tinput_shape:\t\t{self.input_shape}\n'
        ret += f'\toutput_shape:\t\t{self.output_shape}\n'

        return ret

    def update_dimensions(self):
        """
        CasADi does only work with two dimensional arrays. So the dimensions must be updated.
        """

        if len(self.input_shape) == 1:
            self.input_shape = (1, self.input_shape[0])
        elif len(self.input_shape) == 2:
            self.input_shape = (self.input_shape[0], self.input_shape[1])
        else:
            raise ValueError("Please check input dimensions.")

        if len(self.output_shape) == 1:
            self.output_shape = (1, self.output_shape[0])
        elif len(self.output_shape) == 2:
            self.output_shape = (self.output_shape[0], self.output_shape[1])
        else:
            raise ValueError("Please check output dimensions.")

    @staticmethod
    def get_activation(function: str) -> Function:
        blank = MX.sym('blank')

        if function == 'sigmoid':
            return Function(function, [blank], [1 / (1 + exp(-blank))])

        elif function == 'tanh':
            return Function(function, [blank], [tanh(blank)])

        elif function == 'relu':
            return Function(function, [blank], [fmax(0, blank)])

        elif function == 'exponential':
            return Function(function, [blank], [exp(blank)])

        elif function == 'softplus':
            return Function(function, [blank], [log(1 + exp(blank))])

        elif function == 'gaussian':
            return Function(function, [blank], [exp(-blank ** 2)])

        elif function == 'linear':
            return Function(function, [blank], [blank])

        else:
            raise ValueError(f'Unknown activation function: "{function}"')

    @abstractmethod
    def forward(self, input):
        ...

    @abstractmethod
    def to_keras_layer(self):
        ...


class Dense(Layer):
    """
    Fully connected layer.
    """

    def __init__(self, layer: layers.Dense):

        super(Dense, self).__init__(layer)

        # weights and biases
        self.weights, self.biases = layer.get_weights()

        # check input dimension
        if self.input_shape[1] != self.weights.shape[0]:
            raise ValueError(f'Please check the input dimensions of this layer. Layer with error: {self.name}')

    def forward(self, input):

        # forward pass
        f = self.activation(input @ self.weights + self.biases.reshape(1, self.biases.shape[0]))

        return f

    def inspect(self):

        print('Weights')
        print(self.weights)
        print('Biases')
        print(self.biases)

    def to_keras_layer(self) -> layers.Layer:
        return layers.Dense(units=self.units, weights=(self.weights, self.biases), input_shape=self.input_shape)


class Flatten(Layer):

    def __init__(self, layer: layers.Flatten):

        super(Flatten, self).__init__(layer)

    def forward(self, input):

        # flattens the input
        f = input[0, :]
        for row in range(1, input.shape[0]):
            f = horzcat(f, input[row, :])

        return f

    def to_keras_layer(self):

        return layers.Flatten()


class BatchNormalising(Layer):
    """
    Batch Normalizing layer. Make sure the axis setting is set to two.
    """

    def __init__(self, layer: layers.BatchNormalization):

        super(BatchNormalising, self).__init__(layer)

        self.weights = layer.get_weights()

        # weights and biases
        self.gamma = np.vstack([layer.get_weights()[0]] * self.input_shape[0])
        self.beta = np.vstack([layer.get_weights()[1]] * self.input_shape[0])
        self.mean = np.vstack([layer.get_weights()[2]] * self.input_shape[0])
        self.var = np.vstack([layer.get_weights()[3]] * self.input_shape[0])
        self.epsilon = layer.get_config()['epsilon']

        # check Dimensions
        if self.input_shape != self.gamma.shape:
            axis = self.config['axis'][0]
            raise ValueError(f'Dimension mismatch. Normalized axis: {axis}')

        # symbolic input layer
        self.input_layer = MX.sym('input_layer', self.input_shape[0], self.input_shape[1])

    def forward(self, input):

        # forward pass
        f = (input - self.mean) / (sqrt(self.var + self.epsilon)) * self.gamma + self.beta

        return f

    def inspect(self):

        print('gamma:')
        print(self.gamma)
        print('beta:')
        print(self.beta)
        print('mean:')
        print(self.mean)
        print('var:')
        print(self.var)
        print('epsilon:')
        print(self.epsilon)

    def to_keras_layer(self):

        return layers.BatchNormalization(weights=self.weights, epsilon=self.epsilon)


class LSTM(Layer):
    """
    Long Short Term Memory cell.
    """

    def __init__(self, layer: layers.LSTM):

        super(LSTM, self).__init__(layer)

        # recurrent activation
        self.recurrent_activation = self.get_activation(layer.get_config()['recurrent_activation'])

        # load weights and biases
        W = layer.get_weights()[0]
        U = layer.get_weights()[1]
        b = layer.get_weights()[2]

        # weights (kernel)
        self.W_i = W[:, :self.units]
        self.W_f = W[:, self.units: self.units * 2]
        self.W_c = W[:, self.units * 2: self.units * 3]
        self.W_o = W[:, self.units * 3:]

        # weights (recurrent kernel)
        self.U_i = U[:, :self.units]
        self.U_f = U[:, self.units: self.units * 2]
        self.U_c = U[:, self.units * 2: self.units * 3]
        self.U_o = U[:, self.units * 3:]

        # biases
        self.b_i = np.expand_dims(b[:self.units], axis=0)
        self.b_f = np.expand_dims(b[self.units: self.units * 2], axis=0)
        self.b_c = np.expand_dims(b[self.units * 2: self.units * 3], axis=0)
        self.b_o = np.expand_dims(b[self.units * 3:], axis=0)

        # initial memory and output
        self.h_0 = np.zeros((1, self.units))
        self.c_0 = np.zeros((1, self.units))

    def forward(self, input):

        # check input shape
        if input.shape != self.input_shape:
            print('Dimension mismatch!')

        # initial
        c = self.c_0
        h = self.h_0

        # number of time steps
        steps = self.input_shape[0]

        # forward pass
        for i in range(steps):

            # input for the current step
            x = input[i, :]

            # calculate memory(c) and output(h)
            c, h = self.step(x, c, h)

        # here the output has to be transposed, because of the dense layer implementation
        return h

    def step(self, x_t, c_prev, h_prev):

        # gates
        i_t = self.recurrent_activation(x_t @ self.W_i + h_prev @ self.U_i + self.b_i)
        f_t = self.recurrent_activation(x_t @ self.W_f + h_prev @ self.U_f + self.b_f)
        o_t = self.recurrent_activation(x_t @ self.W_o + h_prev @ self.U_o + self.b_o)
        c_t = self.activation(x_t @ self.W_c + h_prev @ self.U_c + self.b_c)

        # memory and output
        c_next = f_t * c_prev + i_t * c_t
        h_next = o_t * self.activation(c_next)

        return c_next, h_next

    def to_keras_layer(self):
        raise NotImplementedError("LSTM does not support this function.")


class Rescaling(Layer):

    def __init__(self, layer: layers.Rescaling):
        super(Rescaling, self).__init__(layer)

        # weights and biases
        self.offset = layer.offset
        self.scale = layer.scale

    def forward(self, input):

        # forward pass
        f = input * self.scale + self.offset

        return f

    def inspect(self):

        print('offset:')
        print(self.offset)
        print('scale:')
        print(self.scale)

    def to_keras_layer(self):
        return layers.Rescaling(offset=self.offset, scale=self.scale)


class CasadiNeuralNetwork:
    """
    Generic implementations of sequential Keras models in CasADi.
    """

    def __init__(self, model: models):
        """
        Supported layers:
            - Dense (Fully connected layer)
            - Flatten (Reduces the input dimension to 1)
            - BatchNormalizing (Normalization)
            - LSTM (Recurrent Cell)
        :param model: Sequential Keras Model
        """

        # list with all layers
        self.layers = []

        # forward function
        self._predict = None

        # construct from keras model
        self.construct(model)

    def __str__(self):
        return f'CasadiNeuralNetwork({", ".join(self.layers)})'

    def __repr__(self):
        return f'CasadiNeuralNetwork({", ".join(self.layers)})'

    def summary(self):

        ret = '\n--------------------- Casadi Neural Network ---------------------\n\n'

        for layer in self.layers:
            ret += f'{layer.__class__.__name__}\n'
            ret += f'{layer.__str__()}\n'

        ret += '--------------------- Casadi Neural Network ---------------------\n'

        return ret

    @property
    def input_shape(self):
        return self.layers[0].input_shape

    @property
    def output_shape(self):
        return self.layers[-1].output_shape

    def predict(self, input_values: Union[np.ndarray, list, MX, DM]):

        if isinstance(input_values, np.ndarray):

            if input_values.ndim == 1:
                # reshape to (1, n)

                return float(self._predict(np.reshape(a=input_values, newshape=(1, -1))))
            else:

                # only one sample at a time
                if input_values.shape[0] != 1:
                    raise ValueError()

                return float(self._predict(input_values))

        return self._predict(input_values)

    def construct(self, model: models):

        # Add layers one by
        for layer in model.layers:

            # get the name of the layer
            name = layer.get_config()['name']

            # recreate the matching layer
            if 'dense' in name:
                self.add_layer(Dense(layer))
            elif 'flatten' in name:
                self.add_layer(Flatten(layer))
            elif 'batch_normalization' in name:
                self.add_layer(BatchNormalising(layer))
            elif 'lstm' in name:
                self.add_layer(LSTM(layer))
            elif 'rescaling' in name:
                self.add_layer(Rescaling(layer))
            else:
                raise NotImplementedError(f'Type "{name}" is not supported.')

        # update the predict function
        self.update_forward()

    def update_forward(self):

        # create symbolic input layer
        input_layer = self.layers[0].input_layer

        # initialize
        f = input_layer

        # pass forward through all layers
        for layer in self.layers:
            f = layer.forward(f)

        # create the prediction function
        self._predict = Function('forward', [input_layer], [f])

    def add_layer(self, layer):

        # append layer
        self.layers.append(layer)

    def inspect(self):
        for layer in self.layers:
            layer.inspect()

    def to_sequential(self) -> Sequential:

        model = Sequential()

        for layer in self.layers:
            layer_to_add = layer.to_keras_layer()
            print(layer_to_add)
            model.add(layer_to_add)

        return model

