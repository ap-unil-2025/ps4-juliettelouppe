"""
Problem 3: Mini Contact Manager
Build a simple contact manager using lists and dictionaries.
Practice combining data structures and writing functions.
"""

def create_contact(name, phone, email):
    return {"name": name, "phone": phone, "email": email}

def add_contact(contacts, name, phone, email=""):
    contacts.append(create_contact(name, phone, email))
    return contacts

def find_contact_by_name(contacts, name):
    target = name.strip().lower()
    for c in contacts:
        if c.get("name", "").lower() == target:
            return c
    return None

def search_contacts(contacts, search_term):
    term = search_term.strip().lower()
    if not term:
        return []
    results = []
    for c in contacts:
        n = str(c.get("name", "")).lower()
        p = str(c.get("phone", "")).lower()
        if term in n or term in p:
            results.append(c)
    return results

def delete_contact(contacts, name):
    target = name.strip().lower()
    for i, c in enumerate(contacts):
        if c.get("name", "").lower() == target:
            contacts.pop(i)
            return True
    return False

def count_contacts_with_email(contacts):
    return sum(1 for c in contacts if str(c.get("email", "")).strip() != "")

def get_all_phone_numbers(contacts):
    return [c["phone"] for c in contacts if "phone" in c and str(c["phone"]).strip() != ""]

def sort_contacts_by_name(contacts):
    return sorted(contacts, key=lambda c: c.get("name", "").lower())

def contact_exists(contacts, name):
    return find_contact_by_name(contacts, name) is not None


# Test cases
if __name__ == "__main__":
    print("Testing Mini Contact Manager...")
    print("-" * 50)

    # Create test contacts list
    contacts = []

    # Test 1: create_contact
    print("Test 1: create_contact")
    contact = create_contact("Alice", "555-0001", "alice@email.com")
    print(f"Created: {contact}")
    assert contact == {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'}
    print("✓ Passed\n")

    # Test 2: add_contact
    print("Test 2: add_contact")
    add_contact(contacts, "Alice", "555-0001", "alice@email.com")
    add_contact(contacts, "Bob", "555-0002")
    add_contact(contacts, "Charlie", "555-0003", "charlie@email.com")
    print(f"Added 3 contacts. Total: {len(contacts)}")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 3: find_contact_by_name
    print("Test 3: find_contact_by_name")
    found = find_contact_by_name(contacts, "alice")  # Case-insensitive
    print(f"Found: {found}")
    assert found is not None and found['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 4: search_contacts
    print("Test 4: search_contacts")
    results = search_contacts(contacts, "555-000")
    print(f"Search '555-000' found {len(results)} contacts")
    assert len(results) == 3  # All have 555-000 in phone
    print("✓ Passed\n")

    # Test 5: count_contacts_with_email
    print("Test 5: count_contacts_with_email")
    count = count_contacts_with_email(contacts)
    print(f"Contacts with email: {count}")
    assert count == 2  # Alice and Charlie have emails
    print("✓ Passed\n")

    # Test 6: get_all_phone_numbers
    print("Test 6: get_all_phone_numbers")
    phones = get_all_phone_numbers(contacts)
    print(f"Phone numbers: {phones}")
    assert phones == ['555-0001', '555-0002', '555-0003']
    print("✓ Passed\n")

    # Test 7: sort_contacts_by_name
    print("Test 7: sort_contacts_by_name")
    sorted_contacts = sort_contacts_by_name(contacts)
    names = [c['name'] for c in sorted_contacts]
    print(f"Sorted names: {names}")
    assert names == ['Alice', 'Bob', 'Charlie']
    print("✓ Passed\n")

    # Test 8: contact_exists
    print("Test 8: contact_exists")
    assert contact_exists(contacts, "Alice") == True
    assert contact_exists(contacts, "David") == False
    print("✓ Passed\n")

    # Test 9: delete_contact
    print("Test 9: delete_contact")
    deleted = delete_contact(contacts, "Bob")
    print(f"Deleted Bob: {deleted}, Remaining: {len(contacts)}")
    assert deleted == True and len(contacts) == 2
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work on the contact manager!")
