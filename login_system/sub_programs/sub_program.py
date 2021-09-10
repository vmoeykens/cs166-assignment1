"""
This is the abstract class that all sub-programs will inherit. It defines the minimum implementation
for a sub-program.
"""
import abc

from ..access_policy import AccessPolicy


class SubProgram(abc.ABC):
    access_policy: AccessPolicy = None

    @abc.abstractmethod
    def run_program(self):
        pass