"""
🧩 Exercise: Social Network Friend Recommendations - Part 1
==========================================================

You're building a social network feature that recommends friends based on mutual connections.
This exercise focuses on implementing a graph data structure and basic traversal algorithms.

Given a social network represented as a graph where:
- Each person is a node (vertex)
- Each friendship is an edge
- We want to find people who are "friends of friends" (2 degrees of separation)

Your task is to implement a FriendGraph class with methods to:
1. Add friendships between people
2. Find all friends of a given person
3. Find all friends-of-friends (excluding direct friends)

Example:
Alice is friends with Bob and Charlie
Bob is friends with David and Eve
Charlie is friends with Frank

Alice's friends: [Bob, Charlie]
Alice's friends-of-friends: [David, Eve, Frank] (excluding Bob and Charlie)

Class: FriendGraph
Methods:
- add_friendship(person1: str, person2: str) -> None
- get_friends(person: str) -> List[str]
- get_friends_of_friends(person: str) -> List[str]
"""

from typing import List, Set, Dict
from collections import defaultdict


class FriendGraph:
    def __init__(self):
        self.friendships: Dict[str, Set[str]] = defaultdict(set)

    def add_friendship(self, person1: str, person2: str) -> None:
        """
        Add a bidirectional friendship between two people.
        If Alice is friends with Bob, then Bob is also friends with Alice.
        """
        # TODO: Implement this method
        # Remember: friendships are bidirectional!
        pass

    def get_friends(self, person: str) -> List[str]:
        """
        Return a list of direct friends for the given person.
        Return empty list if person has no friends or doesn't exist.
        """
        # TODO: Implement this method
        pass

    def get_friends_of_friends(self, person: str) -> List[str]:
        """
        Return a list of friends-of-friends (2 degrees of separation).
        Exclude direct friends and the person themselves.
        """
        # TODO: Implement this method
        # Hint: For each direct friend, get their friends, then remove duplicates and direct friends
        pass


def test_friend_graph():
    """Test the FriendGraph implementation with the example scenario."""
    print("🧪 Testing FriendGraph Implementation")
    print("=" * 50)

    # Create graph and add friendships
    graph = FriendGraph()

    # Alice is friends with Bob and Charlie
    graph.add_friendship("Alice", "Bob")
    graph.add_friendship("Alice", "Charlie")

    # Bob is friends with David and Eve
    graph.add_friendship("Bob", "David")
    graph.add_friendship("Bob", "Eve")

    # Charlie is friends with Frank
    graph.add_friendship("Charlie", "Frank")

    # Test Alice's connections
    print(f"Alice's direct friends: {graph.get_friends('Alice')}")
    print(f"Alice's friends-of-friends: {graph.get_friends_of_friends('Alice')}")

    # Test Bob's connections
    print(f"\nBob's direct friends: {graph.get_friends('Bob')}")
    print(f"Bob's friends-of-friends: {graph.get_friends_of_friends('Bob')}")

    # Test someone with no friends
    print(f"\nEve's direct friends: {graph.get_friends('Eve')}")
    print(f"Eve's friends-of-friends: {graph.get_friends_of_friends('Eve')}")

    # Verify expected results
    assert set(graph.get_friends("Alice")) == {"Bob", "Charlie"}
    assert set(graph.get_friends_of_friends("Alice")) == {"David", "Eve", "Frank"}
    assert set(graph.get_friends("Bob")) == {"Alice", "David", "Eve"}
    assert set(graph.get_friends_of_friends("Bob")) == {"Charlie", "Frank"}

    print("\n✅ All tests passed!")


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    print("\n🧪 Testing Edge Cases")
    print("=" * 30)

    graph = FriendGraph()

    # Test person with no friends
    assert graph.get_friends("Nobody") == []
    assert graph.get_friends_of_friends("Nobody") == []

    # Test self-friendship (should be handled gracefully)
    graph.add_friendship("Alice", "Alice")
    assert "Alice" not in graph.get_friends("Alice")

    # Test isolated person
    graph.add_friendship("Bob", "Charlie")
    assert graph.get_friends_of_friends("Alice") == []

    print("✅ Edge case tests passed!")


if __name__ == "__main__":
    test_friend_graph()
    test_edge_cases()

    print("\n🎯 Challenge Questions:")
    print("1. How would you modify the code to handle weighted friendships?")
    print("2. How could you find the shortest path between two people?")
    print("3. What if you wanted to find people with the most mutual friends?")
