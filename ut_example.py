#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
import subprocess

__author__ = 'Pavel Svatos'
__email__  = 'pavel.svatos666@gmail.com' 


IP_FRANKENSTEIN_PLC = '192.168.1.1'
SSH_PORT = '22'


class Testfunc(unittest.TestCase):
    
    def call_cmd(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        stdout, __ = p.communicate()
        return stdout.decode('utf-8')

    def test_ssh_port_FRANKENSTEIN_PLC(self):
        cmd = f'nc -zv {IP_FRANKENSTEIN_PLC} {SSH_PORT} -w 1'
        out = self.call_cmd(cmd)
        self.assertTrue('[tcp/ssh] succeeded' in out, 'SSH connection refused!')
        print('\nTest output: SSH connection allowed!')        
        
if __name__ == '__main__':
    unittest.main()
