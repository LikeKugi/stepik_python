from typing import Optional

num: Optional[int] = None
word: Optional[str] = None

from typing import Any

value: Any
value = 10
print(value)
value = [1, 2, 3]
print(value)
value = {'hi': 'привет'}
print(value)

from typing import List

words: List[str] = ["hello", "world"]
print(words)

from typing import Set, FrozenSet

words: Set[str] = {"hello", "world"}
numbers: FrozenSet[int] = frozenset([1, 2, 2, 1])
print(words)
print(numbers)

from typing import Tuple

words: Tuple[str, int] = ("hello", 300)
print(words)
