# test_esbuildstratos.py
"""
Tests for EsbuildStratos module.
"""

import unittest
from esbuildstratos import EsbuildStratos

class TestEsbuildStratos(unittest.TestCase):
    """Test cases for EsbuildStratos class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EsbuildStratos()
        self.assertIsInstance(instance, EsbuildStratos)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EsbuildStratos()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
