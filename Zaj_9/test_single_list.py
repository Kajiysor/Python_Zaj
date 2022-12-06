import unittest
from single_list import *


class TestSingleList(unittest.TestCase):
    def test_insert_head(self):
        lista = SingleList()
        lista.insert_head(Node(1))
        lista.insert_head(Node(2))
        lista.insert_head(Node(3))

        self.assertEqual(lista.head.data, 3)
        self.assertEqual(lista.head.next.data, 2)
        self.assertEqual(lista.head.next.next.data, 1)
        self.assertEqual(lista.tail.data, 1)
        self.assertEqual(lista.tail.next, None)
        self.assertEqual(lista.length, 3)

    def test_insert_tail(self):
        lista = SingleList()
        lista.insert_tail(Node(1))
        lista.insert_tail(Node(2))
        lista.insert_tail(Node(3))

        self.assertEqual(lista.head.data, 1)
        self.assertEqual(lista.head.next.data, 2)
        self.assertEqual(lista.head.next.next.data, 3)
        self.assertEqual(lista.tail.data, 3)
        self.assertEqual(lista.tail.next, None)
        self.assertEqual(lista.length, 3)

    def test_remove_head(self):
        lista = SingleList()
        lista.insert_head(Node(1))
        lista.insert_head(Node(2))
        lista.insert_head(Node(3))

        self.assertEqual(lista.remove_head().data, 3)
        self.assertEqual(lista.length, 2)
        self.assertEqual(lista.remove_head().data, 2)
        self.assertEqual(lista.length, 1)
        self.assertEqual(lista.remove_head().data, 1)
        self.assertEqual(lista.head, None)
        self.assertEqual(lista.tail, None)
        self.assertEqual(lista.length, 0)
        with self.assertRaises(ValueError):
            lista.remove_head()

    def test_remove_tail(self):
        lista = SingleList()
        lista.insert_head(Node(1))
        lista.insert_head(Node(2))
        lista.insert_head(Node(3))

        self.assertEqual(lista.remove_tail().data, 1)
        self.assertEqual(lista.length, 2)
        self.assertEqual(lista.remove_tail().data, 2)
        self.assertEqual(lista.length, 1)
        self.assertEqual(lista.remove_tail().data, 3)
        self.assertEqual(lista.head, None)
        self.assertEqual(lista.tail, None)
        self.assertEqual(lista.length, 0)
        with self.assertRaises(ValueError):
            lista.remove_tail()

    def test_join(self):
        lista1 = SingleList()
        lista1.insert_head(Node(1))
        lista1.insert_head(Node(2))
        lista1.insert_head(Node(3))

        lista2 = SingleList()
        lista2.insert_head(Node(4))
        lista2.insert_head(Node(5))
        lista2.insert_head(Node(6))

        lista1.join(lista2)

        self.assertEqual(lista1.head.data, 3)
        self.assertEqual(lista1.head.next.data, 2)
        self.assertEqual(lista1.head.next.next.data, 1)
        self.assertEqual(lista1.tail.data, 4)
        self.assertEqual(lista1.tail.next, None)
        self.assertEqual(lista1.length, 6)
        self.assertEqual(lista2.head, None)
        self.assertEqual(lista2.tail, None)
        self.assertEqual(lista2.length, 0)
