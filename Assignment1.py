# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])  # Output: apple

# Adding elements
fruits.append("date")
print("After append:", fruits)

# Inserting elements at a specific position
fruits.insert(1, "blueberry")
print("After insert:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Iterating through the list
print("Iterating through the list:")
for fruit in fruits:
    print(fruit)

# List comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)



# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Initial dictionary:", person)

# Accessing values
print("Name:", person["name"])

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("After adding email:", person)

# Updating a value
person["age"] = 31
print("After updating age:", person)

# Removing a key-value pair
del person["city"]
print("After deleting city:", person)

# Iterating through keys and values
print("Iterating through dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "email" in person:
    print("Email exists in the dictionary.")


# Creating a set
colors = {"red", "green", "blue"}
print("Initial set:", colors)

# Adding elements
colors.add("yellow")
print("After adding yellow:", colors)

# Adding multiple elements
colors.update(["purple", "orange"])
print("After adding multiple colors:", colors)

# Removing elements
colors.remove("green")  # Raises KeyError if the element is not present
print("After removing green:", colors)

# Discarding elements (does not raise an error if the element is not present)
colors.discard("pink")  # No output, as "pink" is not in the set
print("After discarding pink:", colors)

# Set operations
evens = {2, 4, 6, 8}
odds = {1, 3, 5, 7}

# Union
numbers = evens.union(odds)
print("Union of evens and odds:", numbers)

# Intersection
prime_evens = evens.intersection({2, 3, 5, 7})
print("Intersection with primes:", prime_evens)

# Difference
non_primes = evens.difference({2})
print("Difference from evens:", non_primes)

# Checking subset and superset
print("Evens is subset of numbers:", evens.issubset(numbers))
print("Numbers is superset of odds:", numbers.issuperset(odds))


# Creating a tuple
coordinates = (10.0, 20.0, 30.0)
print("Tuple:", coordinates)

# Accessing elements
print("First coordinate:", coordinates[0])

# Slicing a tuple
print("First two coordinates:", coordinates[:2])

# Tuples with mixed data types
person = ("Bob", 25, "Engineer")
print("Person tuple:", person)

# Nested tuples
nested = (1, (2, 3), (4, 5, 6))
print("Nested tuple:", nested)

# Unpacking tuples
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Immutability demonstration
try:
    coordinates[0] = 15.0
except TypeError as e:
    print("Error:", e)

# Tuple methods
print("Number of elements in person tuple:", len(person))
print("Index of 'Engineer':", person.index("Engineer"))
