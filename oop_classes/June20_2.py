# 🧩 Problem: Library Queue Manager - Part 1
# ------------------------------------------
# Create a class called Patron.
#
# Requirements:
# - Each Patron has:
#     - name (str)
#     - membership_id (int)
#
# - Implement:
#     - __init__ to initialize the Patron
#     - __repr__ to return: Patron(name='Danny', membership_id=101)
#
# Example:
# p = Patron("Danny", 101)
# print(p)  # Output: Patron(name='Danny', membership_id=101)

# 🧩 Problem: Library Queue Manager - Part 2
# ------------------------------------------
# Create a class called LibraryQueue to manage a FIFO queue of Patron objects.
#
# Requirements:
# - Method: add_patron(patron: Patron) -> Adds a Patron to the end of the queue
# - Method: serve_patron() -> Removes and returns the first Patron in the queue
# - Method: __len__() -> Returns the number of Patrons currently in the queue
# - Method: __repr__() -> Returns string like:
#     LibraryQueue([Patron(name='Danny', membership_id=101), Patron(name='Alo', membership_id=102)])
#
# Example:
# queue = LibraryQueue()
# queue.add_patron(Patron("Danny", 101))
# queue.add_patron(Patron("Alo", 102))
# assert len(queue) == 2
# served = queue.serve_patron()
# assert served.name == "Danny"
# assert len(queue) == 1

# 🧩 Problem: Library Queue Manager - Part 3
# ------------------------------------------
# Extend the Patron class to track book requests.
#
# Requirements:
# - Each Patron can request multiple books.
# - Add a method: request_book(title: str) -> adds a book title to the Patron’s list
# - Add a method: cancel_request(title: str) -> removes the book if it exists
# - Add a method: get_requested_books() -> returns a list of requested book titles
#
# Notes:
# - Maintain insertion order of book requests.
# - Prevent duplicate book titles from being added.
#
# Example:
# p = Patron("Danny", 101)
# p.request_book("The Hobbit")
# p.request_book("Dune")
# p.request_book("The Hobbit")  # should not duplicate
# assert p.get_requested_books() == ["The Hobbit", "Dune"]
# p.cancel_request("The Hobbit")
# assert p.get_requested_books() == ["Dune"]

from typing import List

class Patron:
    def __init__(self, name: str, membership_id: int) -> None:
        self.name = name.title()
        self.membership_id = membership_id
        self._book_requests: List[str] = []

    def request_book(self, title: str) -> None:
        if title not in self._book_requests:
            self._book_requests.append(title)

    def cancel_request(self, title: str) -> None:
        if title in self._book_requests:
            self._book_requests.remove(title)

    def get_requested_books(self) -> List[str]:
        return self._book_requests.copy()

    def __repr__(self) -> str:
        return f"Patron(name='{self.name}', membership_id={self.membership_id})"

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Patron)
            and self.name == other.name
            and self.membership_id == other.membership_id
        )

class LibraryQueue:
    def __init__(self) -> None:
        self.queue = []

    def add_patron(self, patron: Patron) -> None:
        if any(p.membership_id == patron.membership_id for p in self.queue):
            raise ValueError("Error! Patron Already in Queue!")
        self.queue.append(patron)

    def serve_patron(self) -> Patron:
        if not self.queue:
            raise ValueError("Error! Queue Empty!")
        return self.queue.pop(0)

    def __len__(self) -> int:
        return len(self.queue)

    def __repr__(self) -> str:
        return f"LibraryQueue({self.queue})"

if __name__ == '__main__':
    danny = Patron("Danny", 101)
    assert repr(danny) == "Patron(name='Danny', membership_id=101)"

    queue = LibraryQueue()
    queue.add_patron(danny)
    queue.add_patron(Patron("Alo", 102))
    queue.add_patron(Patron("Joji", 103))

    assert len(queue) == 3
    served = queue.serve_patron()
    assert served == Patron("Danny", 101)

    queue.serve_patron()
    queue.serve_patron()
    assert len(queue) == 0

    try:
        queue.serve_patron()
    except Exception as e:
        assert str(e) == "Error! Queue Empty!"

    # Part 3 test cases
    p = Patron("Danny", 101)
    p.request_book("The Hobbit")
    p.request_book("Dune")
    p.request_book("The Hobbit")  # Should not duplicate
    assert p.get_requested_books() == ["The Hobbit", "Dune"]
    p.cancel_request("The Hobbit")
    assert p.get_requested_books() == ["Dune"]
