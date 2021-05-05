
from pyrpl import Pyrpl




class MyRedpitaya:
    def __init__(self, host: str = "192.168.1.222"):
        """
        instantiates the object p = Pyrpl that opens a connection to the red Pitaya and choose the configuration.
        when you install package Pyrpl and instantiate the class Pyrpl, a window will open and ask you to enter on
        bottom the RP's IP address. The with the arg "config" it will keep your config in the file "global_config"
        and will use it every time. you do not need to change something.
        Parameters
        ----------
        host : IP address of the red Pitaya
        """
        self.host: str = host
        try:
            self.p = Pyrpl(config="global_config")
        except:
            print("error could't connect to redpitaya")

        # value that calibrate the value entered in the Signal Views
        # it is depending on the amplifier you're using.
        self.voltage_calibration: float = 1.2888608208696757 / 11.7

    def set_ramp(self, output: int = 2, frequency: int = 1, amplitude: float = 0.8, offset: float = 0):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='halframp', frequency=frequency, amplitude=amplitude*self.voltage_calibration, offset=offset,
                  trigger_source='immediately')

    def set_sine(self, output: int = None, frequency: int = 1, amplitude: float = 1):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='sin', frequency=frequency, amplitude=amplitude*self.voltage_calibration,
                  trigger_source='immediately')

    def set_square(self, output: int = None, frequency: int = 1, amplitude: float = 1, offset: float = 0,
                   duty_cycle: int = 50):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='square', frequency=frequency, amplitude=amplitude*self.voltage_calibration,
                  offset=offset, symmetry=duty_cycle, trigger_source='immediately')

    def set_dc_offset(self, output: int = None, offset: float = 0.1):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='dc', offset=offset*voltage_calibration)

    def set_pulse(self, output: int = None, frequency: int = 1, amplitude: float = 1, offset: float = 0):
        r = self.p.rp
        asg = r.asg0
        if output == 1:
            asg.output_direct = 'out1'
        else:
            asg.output_direct = 'out2'
        asg.setup(waveform='square', frequency=frequency, amplitude=self.voltage_calibration*amplitude, offset=offset,
                  trigger_source='immediately')


