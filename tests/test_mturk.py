#! /usr/bin/env python
# -*- coding: utf-8 -*-
# S.D.G

"""Test use of Mechanical Turk API"""

# Imports
import os
import unittest
from unittest import skip
from unittest.mock import Mock, mock_open
from turkmarker.aws.mturk import AWSMTurk


class TestMturkAPI(unittest.TestCase):


    def test_connect(self):
        """Test connection to mturk API"""
        self.assertTrue(1)
