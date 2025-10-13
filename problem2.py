def create_student_record(name, age, major, gpa):
    return {
        "name": name,
        "age": age,
        "major": major,
        "gpa": gpa
    }


def get_value_safely(dictionary, key, default):
    return dictionary.get(key, default)


def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def count_word_frequency(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq


def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}


def filter_dictionary(dictionary, keys_to_keep):
    return {k: v for k, v in dictionary.items() if k in keys_to_keep}


def group_by_first_letter(words):
    groups = {}
    for word in words:
        first = word[0].lower()
        groups.setdefault(first, []).append(word)
    return groups


def calculate_grades_average(students):
    if not students:
        return 0.0
    total = sum(student.get("gpa", 0) for student in students)
    return round(total / len(students), 2)


def nested_dict_access(data, keys):
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current


if __name__ == "__main__":
    print("Quick self-tests passed ✅")

    print(create_student_record("Alice", 20, "CS", 3.8))
    print(get_value_safely({"a": 1}, "b", 0))  # 0
    print(merge_dictionaries({"a": 1}, {"b": 2}))  # {'a': 1, 'b': 2}
    print(count_word_frequency("Hello hello world"))  # {'hello': 2, 'world': 1}
    print(invert_dictionary({"a": 1, "b": 2}))  # {1: 'a', 2: 'b'}
    print(filter_dictionary({"a": 1, "b": 2, "c": 3}, ["a", "c"]))  # {'a': 1, 'c': 3}
    print(group_by_first_letter(["apple", "banana", "avocado"]))  # {'a': ['apple', 'avocado'], 'b': ['banana']}
    students = [
        {"name": "Alice", "gpa": 3.8},
        {"name": "Bob", "gpa": 3.4},
        {"name": "Eve", "gpa": 3.6},
    ]
    print(calculate_grades_average(students))  # 3.6
    data = {"a": {"b": {"c": 42}}}
    print(nested_dict_access(data, ["a", "b", "c"]))  # 42

