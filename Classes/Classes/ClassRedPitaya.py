
from pyrpl import Pyrpl


class MyRedpitaya:
    def __init__(self, host: str = "192.168.1.222"):
        self.host: str = host
        try:
            self.p = Pyrpl()
            print('connected to redpitaya')
        except:
            print("error could't connect to redpitaya")

    def set_ramp(self, output: int = 2, frequency: int = 1, amplitude: float = 0.8, offset: float = 0):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='halframp', frequency=frequency, amplitude=amplitude/11.7, offset=offset,
                  trigger_source='immediately')

    def set_sine(self, output: int = None, frequency: int = 1, amplitude: float = 1):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='sin', frequency=frequency, amplitude=amplitude/11.7, trigger_source='immediately')

    def set_square(self, output: int = None, frequency: int = 1, amplitude: float = 1, offset: float = 0,
                   duty_cycle: int = 50):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='square', frequency=frequency, amplitude=amplitude/11.7, offset=offset, symmetry=duty_cycle,
                  trigger_source='immediately')

    def set_dc_offset(self, output: int = None, offset: float = 0.1):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='dc', offset=offset/11.7)

    def set_pulse(self, output: int = None, frequency: int = 1, amplitude: float = 1, offset: float = 0):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='square', frequency=frequency, amplitude=amplitude, offset=offset,
                  trigger_source='immediately')


