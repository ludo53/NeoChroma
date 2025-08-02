# test_neochroma.py
"""
Tests for NeoChroma module.
"""

import unittest
from neochroma import NeoChroma

class TestNeoChroma(unittest.TestCase):
    """Test cases for NeoChroma class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeoChroma()
        self.assertIsInstance(instance, NeoChroma)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeoChroma()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
