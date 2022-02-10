"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        enq_value = self.queue.append(elem)
        return enq_value

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """

        return_value = self.queue[1]
        del self.queue[1]
        return return_value

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        return_value = self.queue[ind]

        return return_value

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        return None
