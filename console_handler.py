from enum import Enum
import logging
import sys

class ConsoleHandler():
    # Start string with these
    BLACK_COLOR = '\033[90m'
    RED_COLOR = '\033[91m'
    GREEN_COLOR = '\033[92m'
    YELLOW_COLOR = '\033[93m'
    BLUE_COLOR = '\033[94m'
    MAGENTA_COLOR = '\033[95m'
    CYAN_COLOR = '\033[96m'
    WHITE_COLOR = '\033[97m'
    # End string with this
    END_COLOR = '\033[0m'
    
    def __init__(self, console: sys.TextIO) -> None:

        self.root = logging.getLogger()
        self.root.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler(console)
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.root.addHandler(self.handler)
        
        self.console = console
        
        self.showInfo = True
        self.showErrors = True
        self.showSuccess = True
        self.showDefault = True
        self.showExceptionInfo = True
        self.showExceptionErrors = True
        #self.showExceptionSuccess = True
        #self.showExceptionDefault = True
    
    def info(self, text: str = 'INFO'):
        if self.showInfo:
            print(self.YELLOW_COLOR + text + self.END_COLOR)
    
    def error(self, text: str = 'ERROR'):
        if self.showInfo:
            print(self.RED_COLOR + text + self.END_COLOR)
    
    def success(self, text: str = 'SUCCESS'):
        if self.showInfo:
            print(self.GREEN_COLOR + text + self.END_COLOR)
    
    def default(self, text: str = 'DEFAULT'):
        if self.showInfo:
            print(self.BLACK_COLOR + text + self.END_COLOR)
    
    
    def raiseException(self, exception: Enum, isInfo: bool = False,  prefix: str = '', sufix: str = ''):
        """
        A public function to raise an exception using the
        private function ( _error ) or ( _info )

        Args:
            exception (ParamikoSSHError: Enum): The type of error to have occurred
            isInfo (bool = False): Whether to display with an info tag or not
        """
        if isInfo:
            self._info(exception, prefix, sufix)
        else:
            self._error(exception, prefix, sufix)
    
    
    def _info(self, e: Enum,  prefix: str = '', sufix: str = ''):
        """
        ~~~~~~~~~~  PRIVATE FUNCTION  ~~~~~~~~~~
        Evaluate errors that have occurred but with a info tag

        Args:
            e (Enum): The type of error to have occurred with a name and value
        """
        #self.close()
        if self.showExceptionInfo:
            print(self.YELLOW_COLOR + f'{prefix}INFO: ({e.value}) -> {e.name}{sufix}' + self.END_COLOR)
        
    
    def _error(self, e: Enum,  prefix: str = '', sufix: str = ''):
        """
        ~~~~~~~~~~  PRIVATE FUNCTION  ~~~~~~~~~~
        Evaluate errors that have occurred

        Args:
            e (Enum): The type of error to have occurred with a name and value
        """
        if self.showExceptionErrors:
            print(self.RED_COLOR + f'{prefix}ERROR: ({e.value}) -> {e.name}{sufix}' + self.END_COLOR)
    