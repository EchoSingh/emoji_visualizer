import unittest
from emoji_visualizer.visualizer import visualize_emojis

class TestVisualizer(unittest.TestCase):

    def test_visualize_emojis(self):
        try:
            visualize_emojis()
        except Exception as e:
            self.fail(f"visualize_emojis() raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()
