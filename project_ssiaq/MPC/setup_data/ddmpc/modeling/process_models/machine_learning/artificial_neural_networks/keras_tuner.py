#!/usr/bin/env python

""" keras_tuner.py: Procedurally builds sequential Keras models based on a given structure. """


import random
import re

from keras.layers import Dense, BatchNormalization, Rescaling
from keras import Sequential


class TunerLayer:

    def __init__(self, optional: bool = True):

        self.optional = optional

    def build_keras_layer(self):
        raise NotImplementedError()


class TunerDense(TunerLayer):

    def __init__(self, units: tuple = None, activations: tuple = None, optional: bool = False):
        """
        :param units: Tuple with the number of neurons the layer can have. Default = (8, 16,)
        :param activations: Tuple with activation functions to pick from. Default = ('sigmoid',)
        :param optional: Is the layer optional?
        """
        super().__init__(optional=optional)

        # default of 8 or 16 neurons
        if units is None:
            units = (8, 16,)

        # default activation is sigmoid
        if activations is None:
            activations = ('sigmoid',)

        self.units = units
        self.activations = activations

    def build_keras_layer(self):

        units = random.choice(self.units)
        activation = random.choice(self.activations)

        return Dense(units=units, activation=activation)


class TunerBatchNormalizing(TunerLayer):

    def __init__(self, axis: int = 1, optional: bool = False):

        super().__init__(optional=optional)

        self.axis = axis

    def build_keras_layer(self):

        return BatchNormalization(axis=self.axis)


class TunerRescaling(TunerLayer):

    def __init__(self, scale: float, offset: float, optional: bool = False):

        super().__init__(optional=optional)

        self.scale = scale
        self.offset = offset

    def build_keras_layer(self):

        return Rescaling(scale=self.scale, offset=self.offset)


class TunerModel:
    """
    Blueprint for a Sequential Keras model.
    Layers can be made optional by setting optional to True.
    """

    def __init__(
            self,
            *layers: TunerLayer,
            name: str,
            optimizer: str = 'adam',
            loss: str = 'mse',
    ):

        self.layers = layers
        self.optimizer = optimizer
        self.loss = loss

        # check if the name is valid
        assert re.match("^[A-Za-z0-9_-]*$", name), f'Please make sure you set a valid TunerModel name not {name}.' \
                                                   'Allowed characters: A-Z, a-z, 0-9, _, -'
        self.name = name

    def __str__(self):
        return f'TunerModel(name={self.name}, ' \
               f'optimizer={self.optimizer}, ' \
               f'loss={self.loss}, ' \
               f'max_layers={self.max_layers}, ' \
               f'min_layers={self.min_layers})'

    def __repr__(self):
        return f'TunerModel(name={self.name}))'

    @property
    def max_layers(self):
        return len(self.layers)

    @property
    def min_layers(self):
        return len([layer for layer in self.layers if layer.optional == False])

    def build_sequential(self, name: str = None) -> Sequential:

        # create random ann id
        ann_id = random.randint(1000, 9999)

        # ann name
        if name is None:
            name = f'{self.name}_{ann_id}'

        # create sequential keras model
        keras_model = Sequential(name=name)

        # iterate over every layer
        for layer in self.layers:

            # check if the layer is optional and maybe skip it
            if layer.optional and random.getrandbits(1):
                continue

            # add layer
            keras_model.add(layer.build_keras_layer())

        # output layer
        keras_model.add(Dense(units=1, activation='linear'))

        # compile the model
        keras_model.compile(optimizer=self.optimizer, loss=self.loss)


        return keras_model


if __name__ == '__main__':

    tuner_model = TunerModel(
        TunerBatchNormalizing(axis=1),
        TunerDense(units=(8, 16)),
        name='SimpleDense',
        optimizer='adam',
        loss='mse',
    )

    print(tuner_model)

    seq = tuner_model.build_sequential()

    print(seq.name)
