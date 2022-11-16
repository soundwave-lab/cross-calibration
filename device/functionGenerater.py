# APPLy?
# "SIN +5.0000000000000E+03,+3.0000000000000E+00,-2.5000000000000E+00"

import pyvisa


class FunctionGenerater:
    rm_ = pyvisa.ResourceManager()

    def __init__(self, interface):  # 接続先を指定
        self._func = self.rm_.open_resource(interface)

    def change_frequency(self, f): #f Hzに変更
        self._func.write('FREQuency '+ str(f))
