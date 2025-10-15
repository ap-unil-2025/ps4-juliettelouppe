"""
Problem 4: Data Persistence with JSON
Learn to use Python modules (imports) and save data to files using JSON.
"""

import json
import shutil
import os
from typing import Any, List, Dict
from pathlib import Path

# Note: json is a built-in Python module for working with JSON data

def save_to_json(data: Any, filename: str) -> None:
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_from_json(filename: str) -> Any:
    path = Path(filename)
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)



def save_contacts_to_file(contacts: List[Dict[str, Any]], filename: str) -> None:
    save_to_json(contacts, filename)


def load_contacts_from_file(filename: str) -> List[Dict[str, Any]]:
    data = load_from_json(filename)
    if data is None:
        return []
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return [data]
    return []


def append_contact_to_file(contact: Dict[str, Any], filename: str) -> List[Dict[str, Any]]:
    contacts = load_contacts_from_file(filename)
    contacts.append(contact)
    save_contacts_to_file(contacts, filename)
    return contacts



def backup_file(source_filename: str, backup_filename: str) -> bool:
    src = Path(source_filename)
    if not src.exists():
        return False
    dst = Path(backup_filename)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def get_file_stats(filename: str) -> Dict[str, Any]:
    path = Path(filename)
    stats = {
	"exists": path.exists(),
	"size_bytes": path.stat().st_size if path.exists() else 0,
	"lines": sum(1 for _ in open(path)) if path.exists() else 0,
	"type": "list",
	"count" : 0
    }
    if path.exists():
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    stats['count'] = len(data)
        except Exception:
            stats['count'] = 0

    return stats
	
def merge_json_files(file1: str, file2: str, output_file: str) -> Any:
    d1 = load_from_json(file1)
    d2 = load_from_json(file2)

    if isinstance(d1, list) and isinstance(d2, list):
        merged: Any = d1 + d2
    elif isinstance(d1, dict) and isinstance(d2, dict):
        merged = {**d1, **d2}
    else:
        merged = {"file1": d1, "file2": d2}

    save_to_json(merged, output_file)
    return merged


def search_json_file(filename: str, key: str, value: Any) -> List[Dict[str, Any]]:
    data = load_from_json(filename)
    matches: List[Dict[str, Any]] = []

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and item.get(key) == value:
                matches.append(item)
    elif isinstance(data, dict):
        if data.get(key) == value:
            matches.append(data)

    return matches

# Test cases
if __name__ == "__main__":
    print("Testing JSON File Operations...")
    print("-" * 50)

    # Test 1: save_to_json and load_from_json
    print("Test 1: save_to_json and load_from_json")
    test_data = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
    save_to_json(test_data, 'test_data.json')
    loaded_data = load_from_json('test_data.json')
    print(f"Saved and loaded: {loaded_data}")
    assert loaded_data == test_data
    print("✓ Passed\n")

    # Test 2: save_contacts_to_file and load_contacts_from_file
    print("Test 2: save and load contacts")
    contacts = [
        {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'},
        {'name': 'Bob', 'phone': '555-0002', 'email': 'bob@email.com'}
    ]
    save_contacts_to_file(contacts, 'test_contacts.json')
    loaded_contacts = load_contacts_from_file('test_contacts.json')
    print(f"Loaded {len(loaded_contacts)} contacts")
    assert len(loaded_contacts) == 2
    assert loaded_contacts[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 3: append_contact_to_file
    print("Test 3: append_contact_to_file")
    new_contact = {'name': 'Charlie', 'phone': '555-0003', 'email': 'charlie@email.com'}
    append_contact_to_file(new_contact, 'test_contacts.json')
    contacts = load_contacts_from_file('test_contacts.json')
    print(f"After append: {len(contacts)} contacts")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 4: backup_file
    print("Test 4: backup_file")
    backup_file('test_contacts.json', 'test_contacts_backup.json')
    backup_data = load_from_json('test_contacts_backup.json')
    print(f"Backup created with {len(backup_data)} items")
    assert len(backup_data) == 3
    print("✓ Passed\n")

    # Test 5: get_file_stats
    print("Test 5: get_file_stats")
    stats = get_file_stats('test_contacts.json')
    print(f"File stats: {stats}")
    assert stats is not None
    assert stats['exists'] == True
    assert stats['type'] == 'list'
    assert stats['count'] == 3
    print("✓ Passed\n")

    # Test 6: merge_json_files
    print("Test 6: merge_json_files")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    save_to_json(list1, 'list1.json')
    save_to_json(list2, 'list2.json')
    merge_json_files('list1.json', 'list2.json', 'merged.json')
    merged = load_from_json('merged.json')
    print(f"Merged list: {merged}")
    assert merged == [1, 2, 3, 4, 5, 6]
    print("✓ Passed\n")

    # Test 7: search_json_file
    print("Test 7: search_json_file")
    results = search_json_file('test_contacts.json', 'name', 'Alice')
    print(f"Search results: {results}")
    assert len(results) == 1
    assert results[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Cleanup
    print("Cleaning up test files...")
    import os
    for file in ['test_data.json', 'test_contacts.json', 'test_contacts_backup.json',
                 'list1.json', 'list2.json', 'merged.json']:
        if os.path.exists(file):
            os.remove(file)
    print("✓ Cleaned up\n")

    print("=" * 50)
    print("All tests passed! You've mastered JSON file operations!")
