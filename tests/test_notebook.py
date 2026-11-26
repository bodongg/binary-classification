import ast
from collections import Counter
import csv
from io import StringIO
import json
from pathlib import Path
import unittest


class NotebookTests(unittest.TestCase):
    def test_embedded_dataset(self):
        path = Path(__file__).resolve().parents[1] / "Binary_Classification.ipynb"
        notebook = json.loads(path.read_text(encoding="utf-8-sig"))
        fixtures = []
        for cell in notebook["cells"]:
            if cell["cell_type"] != "code":
                continue
            tree = ast.parse("".join(cell["source"]))
            fixtures.extend(
                node.value for node in ast.walk(tree)
                if isinstance(node, ast.Constant) and isinstance(node.value, str)
                and node.value.startswith("Customer_ID,Visits_Last_28_Days,")
            )
        self.assertEqual(len(fixtures), 1)
        reader = csv.DictReader(StringIO(fixtures[0]))
        self.assertEqual(reader.fieldnames, [
            "Customer_ID", "Visits_Last_28_Days", "Cart_Visits_Last_28_Days",
            "Avg_Session_Minutes", "Purchased_Next_7_Days",
        ])
        rows = list(reader)
        self.assertEqual(len(rows), 504)
        unique = {tuple(row.values()) for row in rows}
        self.assertEqual(len(unique), 500)
        self.assertEqual(len({row[0] for row in unique}), 500)
        self.assertEqual(Counter(row[-1] for row in unique), {"0": 400, "1": 100})


if __name__ == "__main__":
    unittest.main()
