import os

INPUT_MAX_LEN = 30 # may be dynamic
WORD_MIN_COUNT = 10

DICT_SIZE = 4696 # need to be dynamic

RNN_SIZE = 512
RNN_LAYER = 2
LSTM_KEEPPROB = 0.8
SCHEDULE_RATE = 0.0

LEARNING_RATE = 1e-3
LEARNING_RATE_DECAY_RATE = 0.5
LEARNING_RATE_DECAY_STEPS = 100000

MAX_GRADIENT_NORM = 5.0
BATCH_SIZE = 256
EPOCH = 30
LOAD_MODEL = False
BUILD_DICT = not LOAD_MODEL
RESHUFFLE = not LOAD_MODEL
VALID_MODEL = True

PRINT_ITERATION = 100
MODEL_SAVE_PATH = 'model4'

BEAM_WIDTH = 10
#


