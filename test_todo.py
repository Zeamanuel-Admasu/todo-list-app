import unittest
from todo import ToDoList  # Import the To-Do List class

class TestToDoList(unittest.TestCase):

    def setUp(self):
        """Initialize a ToDoList instance before each test"""
        self.todo = ToDoList()
        self.todo.add_task("Buy groceries")
        self.todo.add_task("Walk the dog")

    def test_add_task(self):
        """Test if a task is correctly added to the list"""
        self.todo.add_task("Read a book")
        self.assertEqual(len(self.todo.tasks), 3)
        self.assertEqual(self.todo.tasks[2]["task"], "Read a book")

    def test_mark_completed_valid_task(self):
        """Test marking a valid task as completed"""
        self.todo.mark_completed(0)
        self.assertTrue(self.todo.tasks[0]["completed"])

    def test_mark_completed_invalid_index(self):
        """Test attempting to mark an out-of-bounds task index as completed"""
        with self.assertRaises(IndexError):
            self.todo.mark_completed(10)

    def test_mark_already_completed_task(self):
        """Test marking a task that is already completed"""
        self.todo.mark_completed(0)
        self.todo.mark_completed(0)  # Mark it again
        self.assertTrue(self.todo.tasks[0]["completed"])  # Ensure it's still marked

    def test_delete_task(self):
        """Test deleting a task"""
        self.todo.delete_task(1)
        self.assertEqual(len(self.todo.tasks), 1)
        self.assertEqual(self.todo.tasks[0]["task"], "Buy groceries")

    def test_delete_invalid_task(self):
        """Test deleting a task with an invalid index"""
        with self.assertRaises(IndexError):
            self.todo.delete_task(10)

if __name__ == '__main__':
    unittest.main()
