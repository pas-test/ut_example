#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import unittest
import subprocess

# unimportant comment
IP_FRANKENSTEIN_PLC = '192.168.15.19'
SSH_PORT = '22'


class Testfunc(unittest.TestCase):

    def call_cmd(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        stdout, __ = p.communicate()
        return stdout.decode('utf-8')

    def test_ping_FRANKENSTEIN_PLC(self):
        cmd = f'ping {IP_FRANKENSTEIN_PLC} -c 1 -W 1'
        out = self.call_cmd(cmd)
        self.assertTrue('1 received' in out, 'Frankenstein is down!')
        print('\nTest output: Frankenstein is alive!')

    def test_ssh_port_FRANKENSTEIN_PLC(self):
        cmd = f'nc -zv {IP_FRANKENSTEIN_PLC} {SSH_PORT} -w 1'
        out = self.call_cmd(cmd)
        self.assertTrue('[tcp/ssh] succeeded' in out, 'SSH connection refused!')
        print('\nTest output: SSH connection allowed!')

if __name__ == '__main__':
    unittest.main()
