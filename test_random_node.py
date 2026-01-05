# AI Disclosure: The first version of this test suite was drafted by AI, but it was manually edited and checked for correctness

import unittest
import os
import shutil
import json
from random_node import RandomFileSelector


class TestRandomFileSelector(unittest.TestCase):

    # --- SETUP & TEARDOWN ---
    @classmethod
    def setUpClass(cls):
        """Runs ONCE before all tests. Creates our test files."""
        cls.test_dir = "test_data_temp"
        if not os.path.exists(cls.test_dir):
            os.makedirs(cls.test_dir)

        # 1. Create VALID Files
        cls.valid_txt = os.path.join(cls.test_dir, "valid.txt")
        with open(cls.valid_txt, "w") as f:
            f.write("Line 1\nLine 2\nLine 3")

        cls.valid_csv = os.path.join(cls.test_dir, "valid.csv")
        with open(cls.valid_csv, "w") as f:
            f.write("Col1,Col2\nValA,ValB\nValC,ValD")

        cls.valid_json_list = os.path.join(cls.test_dir, "valid_list.json")
        with open(cls.valid_json_list, "w") as f:
            json.dump(["Item A", "Item B", "Item C"], f)

        cls.valid_json_dict = os.path.join(cls.test_dir, "valid_dict.json")
        with open(cls.valid_json_dict, "w") as f:
            json.dump({"key1": "Value A", "key2": "Value B"}, f)

        # 2. Create INVALID / TRICKY Files
        cls.empty_txt = os.path.join(cls.test_dir, "empty.txt")
        with open(cls.empty_txt, "w") as f:
            pass  # Create empty file

        cls.bad_json = os.path.join(cls.test_dir, "bad.json")
        with open(cls.bad_json, "w") as f:
            f.write("{ this is not valid json }")

        cls.wrong_ext = os.path.join(cls.test_dir, "image.png")
        with open(cls.wrong_ext, "w") as f:
            f.write("im technically text but named png")

        # Initialize the Node
        cls.node = RandomFileSelector()

    @classmethod
    def tearDownClass(cls):
        """Runs ONCE after all tests. Cleans up the mess."""
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    # --- THE TESTS ---

    def test_txt_selection(self):
        """Test if it picks a line from a text file."""
        # Run node with seed 1
        result = self.node.get_random_item(self.valid_txt, seed=1)[0]
        self.assertIn(result, ["Line 1", "Line 2", "Line 3"])

        # Test Determinism: Seed 1 should ALWAYS return the same line
        result_again = self.node.get_random_item(self.valid_txt, seed=1)[0]
        self.assertEqual(result, result_again, "Same seed did not produce same result!")

    def test_json_list(self):
        """Test valid JSON list."""
        result = self.node.get_random_item(self.valid_json_list, seed=42)[0]
        self.assertIn(result, ["Item A", "Item B", "Item C"])

    def test_json_dict(self):
        """Test valid JSON dict (should pick values)."""
        result = self.node.get_random_item(self.valid_json_dict, seed=42)[0]
        self.assertIn(result, ["Value A", "Value B"])

    def test_csv_parsing(self):
        """Test CSV parsing."""
        result = self.node.get_random_item(self.valid_csv, seed=10)[0]
        # Depending on your logic, it usually grabs "Col1,Col2" or "ValA,ValB"
        # Checking if result is a non-empty string is a good start
        self.assertTrue(len(result) > 0)
        self.assertIsInstance(result, str)

    def test_missing_file(self):
        """Should fail gracefully if file doesn't exist."""
        result = self.node.get_random_item("ghost_file.txt", seed=0)[0]
        self.assertTrue(result.startswith("Error: File not found"), f"Got: {result}")

    def test_empty_file(self):
        """Should fail gracefully if file is empty."""
        result = self.node.get_random_item(self.empty_txt, seed=0)[0]
        self.assertTrue(result.startswith("Error: File is empty"), f"Got: {result}")

    def test_bad_json(self):
        """Should fail gracefully if JSON is malformed."""
        result = self.node.get_random_item(self.bad_json, seed=0)[0]
        self.assertTrue(result.startswith("Error parsing file"), f"Got: {result}")

    def test_wrong_extension(self):
        """Should fail if we feed it a PNG or unknown type."""
        result = self.node.get_random_item(self.wrong_ext, seed=0)[0]
        self.assertTrue(result.startswith("Error: Unsupported file extension"), f"Got: {result}")


if __name__ == '__main__':
    unittest.main()