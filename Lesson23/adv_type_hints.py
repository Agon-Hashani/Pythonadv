from typing import  Optional, List, Union, Any

def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonymous"

print(get_name("John"))

def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value(123))


def process_anything(value: Any) -> str:
    return f"Processed {value}"

print(process_anything(123.1231))


def sum_list(numbers: List[int]) -> int:
    return sum(numbers)


number: List[int] = [1, 2, 3]
result: int = sum_list(number)
print(result)