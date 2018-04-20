# -*- coding: utf-8 -*-
import time


class TP3005P(object):
    """
    Product Page:
    http://tekpower.us/tp3005pmanual.html

    User Manual:
    http://tekpower.us/downloadable/download/sample/sample_id/40/

    Remote Control Guide:
    http://tekpower.us/downloadable/download/sample/sample_id/41/
    """

    on = False

    def __init__(self, serial_connection):
        self.serial_connection = serial_connection

    def _write_line(self, command):
        self.serial_connection.reset_input_buffer()
        string = '{}\n'.format(command).encode('utf-8')
        self.serial_connection.write(string)

    def _read_line(self):
        pass

    def update_connection(self, serial_connection):
        self.serial_connection = serial_connection

    def identify(self):
        """
        Acquires the identity of the attached device.

        Command format: *IDN?\n
        Description: Returns the TEK3005P identification.
        Example: *IDN?\n
        """
        time.sleep(0.05)
        command = b'*IDN?\\r\\n'
        self.serial_connection.write(command)
        value = self.serial_connection.readline().decode('utf8')
        return value

    def status(self):
        """
        Gets the current status of the attached device.

        Command format: STATUS?\n
        Description: Returns the TEK3005P status.
        Contents 2 bits in the following format
        Bit Item Description
        1 OUTPUT flag ON,0 OUTPUT flag OFF.
        1 “OCP” flag ON,0 “OCP” flag OFF.
        """
        time.sleep(0.05)
        command = b'STATUS?\\r\\n'
        self.serial_connection.write(command)
        line = self.serial_connection.readline()
        instrument_status = int(line.decode('utf8'))
        return instrument_status

    def output(self, state=False):
        """
        Turns the output on or off.

        OUTPUT<Boolean>\n
        Description: Turns on or off the output.
        Boolean: 0 OFF, 1 ON
        Example: OUTPUT1\n
        """
        if state and self.on:
            # Check to see what state it is in first
            return

        time.sleep(0.05)
        if out_on >= 1:
            command = b'OUTPUT1:\\r\\n'
        else:
            command = b'OUTPUT0\\r\\n'
        self.serial_connection.write(command)
        time.sleep(0.05)

    def current(self):
        """
        Acquires the output current on the attached device. 

        Command format: IOUT1?\n
        Description: Returns the actual output current.
        Example: IOUT1?\n
        """
        time.sleep(0.05)
        command = b'IOUT1?\\r\\n'
        ser1.write(command)
        line = self.serial_connection.readline()
        amps = float(line.decode('utf8'))
        return amps

    def voltage(self):
        """
        Acquires the output voltage on the attached device.

        Command format: VOUT1?\n
        Description: Returns the actual output voltage
        Example: VOUT1?\n
        """
        time.sleep(0.05)
        command = b'VOUT1?\\r\\n'
        self.serial_connection.write(command)
        line = ser1.readline()
        volts = float(line.decode('utf8'))
        return volts

    @property
    def voltage_setpoint(self):
        """
        Acquires the Voltage Setpoint on the attached device.

        Command format: VSET1?\n
        Description: Returns the output voltage setting.
        Example: VSET1?\n
        """
        time.sleep(0.05)
        command = b'VSET1?\\r\\n'
        self.serial_connection.write(command)
        line = self.serial_connection.readline()
        volts = float(line.decode('utf8'))
        return volts

    @voltage_setpoint.setter
    def voltage_setpoint(self, value):
        """
        Assigns the Voltage Setpoint on the attached device.

        Command format: VSET1:<Data>\n
        1. VSET1: Command header
        2. : separator
        3. Data: Value
        4. \n: End mark
        Example: VSET1:05.00\n
                 VSET1:30.00\n
        """
        command = b'VSET1:'                      #b'VSET1:07.00\\r\\n'
        command = command + format(volts, "=05.2F").encode('ascii')
        command = command + b'\\r\\n'
        self.serial_connection.write(command)

    @property
    def current_setpoint(self):
        """
        Acquires the Current Setpoint on the attaced device.

        Command format: ISET1?\n
        Description: Returns the output current setting.
        Example: ISET1?\n
        """
        time.sleep(0.05)
        command = b'IOUT1?\\r\\n'
        self.serial_connection.write(command)
        line = self.serial_connection.readline()
        amps = float(line.decode('utf8'))
        return amps

    @current_setpoint.setter
    def current_setpoint(self, value):
        """
        Assigns the Current Setpoint on the attached device.

        Command format: ISET1:<Data>\n
        1.ISET1: Command header
        2.: separator
        3.Data: Value
        4.\n: End mark
        Example: ISET1:0.005\n
                 ISET1:5.000\n
        """
        time.sleep(0.05)
        command = b'ISET1:'                      #b'ISET1:2.500\\r\\n'
        command = command + format(amps, "=05.3F").encode('ascii')
        command = command + b'\\r\\n'
        self.serial_connection.write(command)

