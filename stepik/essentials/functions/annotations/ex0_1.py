num: int | None = None
word: str | None = None

words: list[str] = ["hello", "world"]

def foo(bar: dict[str | int, str | None]) -> bool:
   return True