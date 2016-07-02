#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_atws
----------------------------------

Tests for `atws` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner
import atws
from atws import create_picklist_module

query_test_output='''<?xml version="1.0" ?>
<queryxml>
    <entity>Ticket</entity>
    <query>
        <condition>
            <field>
                Status
                <expression op="NotEqual">5</expression>
            </field>
        </condition>
        <condition>
            <condition operator="OR">
                <field>
                    IssueType
                    <expression op="GreaterThan">345</expression>
                </field>
            </condition>
        </condition>
    </query>
</queryxml>
'''


class TestAtws(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_zone_lookup_failure(self):
        try:
            _ = atws.connect(username='failed@toresolve.com',
                              password='notright')
        except ValueError as e:
            assert 'failed@toresolve.com failed to resolve to a zone' in str(e) 
    
    
    def test_001_query_building_output(self):
        query = atws.Query('Ticket')
        query.WHERE('Status', query.NotEqual, 5)
        query.open_bracket()
        query.OR('IssueType', query.GreaterThan, 345)
        query_output = query.pretty_print()
        assert query_test_output == query_output
        
        
    def test_command_line_interface(self):
        runner = CliRunner()
        #         result = runner.invoke(create_picklist_module.main)
        #         assert result.exit_code == 0
        #         assert 'atws.create_picklist_module.main' in result.output
        help_result = runner.invoke(create_picklist_module.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output


if __name__ == '__main__':
    sys.exit(unittest.main())