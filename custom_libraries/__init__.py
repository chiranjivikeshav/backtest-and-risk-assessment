# custom_libraries/__init__.py
# from custom_libraries.layers import layers  # This line is crucial
from .layers import DenseLayer, DropoutLayer

__all__ = ['DenseLayer', 'DropoutLayer']