from typing import Any, Optional


class Queue:
    """A simple queue implementation using Python lists."""

    def __init__(self) -> None:
        """Initializes an empty queue."""
        self.queue: list[Any] = []
        self.now: int = 0

    def add(self, obj: Any) -> None:
        """Adds an object to the end of the queue.

        Args:
        ----
            obj (Any): The object to add to the queue.

        """
        self.queue.append(obj)

    def next(self) -> Optional[Any]:
        """Moves to the next item in the queue and returns it.

        Returns
        -------
            Optional[Any]: The next item in the queue if available, otherwise None.

        """
        return self._move(1)

    def previous(self) -> Optional[Any]:
        """Moves to the previous item in the queue and returns it.

        Returns
        -------
            Optional[Any]: The previous item in the queue if available, otherwise None.

        """
        return self._move(-1)

    def _move(self, step: int) -> Optional[Any]:
        """Helper method to move the queue position by a specified step.

        Args:
        ----
            step (int): The step to move in the queue. Positive for next, negative for previous.

        Returns:
        -------
            Optional[Any]: The item at the new position if within bounds, otherwise None.

        """
        new_position = self.now + step
        if 0 <= new_position < len(self.queue):
            self.now = new_position
            return self.queue[self.now]
        return None

    def source(self, previous: bool = False) -> Optional[Any]:
        """Returns the item after (default) or before the current item.

        Args:
        ----
            previous (bool, optional): If True, returns the item before the current item, otherwise after (default: False).

        Returns:
        -------
            Optional[Any]: The item after (default) or before the current item if available, otherwise None.

        """
        if self.is_empty():
            return None
        if previous:
            if self.now > 0:
                return self.queue[self.now - 1]
            else:
                return None
        elif self.now + 1 < len(self.queue):
            return self.queue[self.now + 1]
        else:
            return None

    def current_item(self) -> Optional[Any]:
        """Returns the current item in the queue.

        Returns
        -------
            Optional[Any]: The current item in the queue if available, otherwise None.

        """
        if not self.is_empty():
            return self.queue[self.now]
        return None

    def is_empty(self) -> bool:
        """Checks if the queue is empty.

        Returns
        -------
            bool: True if the queue is empty, False otherwise.

        """
        return len(self.queue) == 0

    def clear(self) -> None:
        """Clears the queue."""
        self.queue = []
        self.now = 0
