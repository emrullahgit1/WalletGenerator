# test_walletgenerator.py
"""
Tests for WalletGenerator module.
"""

import unittest
from walletgenerator import WalletGenerator

class TestWalletGenerator(unittest.TestCase):
    """Test cases for WalletGenerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletGenerator()
        self.assertIsInstance(instance, WalletGenerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletGenerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
