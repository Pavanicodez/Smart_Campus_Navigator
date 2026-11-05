import sys
from pathlib import Path
import unittest

BACKEND_PATH= Path(__file__).resolve().parents[1] / "backend"
sys.path.insert(0,str(BACKEND_PATH))

from algorithms import bfs, ucs, astar


class TestCampusAlgorithms(unittest.TestCase):

    def setUp(self):
        self.graph = {
            "A": {"B": 5, "C": 1},
            "B": {"A": 5, "C": 1, "D": 1},
            "C": {"A": 1, "B": 1, "D": 10},
            "D": {"B": 1, "C": 10}
        }

    def test_bfs_finds_path(self):
        result = bfs("A", "D", self.graph)
        self.assertIsNotNone(result)
        self.assertEqual(result["path"][0], "A")
        self.assertEqual(result["path"][-1], "D")

    def test_ucs_finds_minimum_cost(self):
        result = ucs("A", "D", self.graph)
        self.assertEqual(result["distance"], 3)

    def test_astar_finds_minimum_cost(self):
        result = astar("A", "D", self.graph)
        self.assertEqual(result["distance"], 3)

    def test_ucs_and_astar_cost_match(self):
        ucs_result = ucs("A", "D", self.graph)
        astar_result = astar("A", "D", self.graph)
        self.assertEqual(
            ucs_result["distance"],
            astar_result["distance"]
        )


if __name__ == "__main__":
    unittest.main()