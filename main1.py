# PURPOSE: The program will provide the user with all tables that are available to use, based on the party size. 

#SIMPLIFIED PSEUDOCODE: 
# 1. Ask user for their name and greet them kindly.
# 2. Define table chart with table names, capacities, and availability ('o' for open, 'x' for occupied).
# 3. Look at the tables and determine which are free for the user:
#   - Loop through the table chart.
#   - If a table is represented by'o' in any row, add to the 'free tables list'.
#4. Display all free tables to the user.
#5. Ask user for their party size.
#6. Find a single table:
#   - Go through all tables, check if the capacity >= party size (and if it's free).
#   - If one is found, display it.
# 7. Find all tables that can fit the party size:
#   - Loop through all free tables and list those with sufficient capacity.
#8. Check if two adjacent tables are able to be combined:
#   - Once again, loop through tables, check if two side-by-side tables are both free.
#   - If their combined capacity meets the party size, print it to them.
# 9. Print out final outcome of the program, making sure it is user-friendly.


name = input("Enter your name: ") # This portion will greet the guest.
print(f"Welcome, {name}, to the Elite Restaurant!\n")
print("Please enter the information corresponding to your party so we can assist you.\n")

restaurant_tables = [
    ['T1(2)', 'T2(4)', 'T3(2)', 'T4(6)', 'T5(4)', 'T6(2)'],  # Table headers
    ['x', 'o', 'o', 'o', 'o', 'x'],  # Row 1,
    ['o', 'x', 'o', 'o', 'x', 'o'],  # Row 2,
    ['x', 'x', 'o', 'x', 'o', 'o'],  # Row 3,
    ['o', 'o', 'o', 'x', 'o', 'x'],  # Row 4,
    ['o', 'x', 'o', 'x', 'o', 'o'],  # Row 5,
    ['o', 'o', 'o', 'o', 'x', 'o']   # & Row 6,
]   # Table layout with all capacities

free_tables = [] # Will find all currently free tables (pt1)
for col in range(len(restaurant_tables[0])):
    for row in range(1, len(restaurant_tables)):
        if restaurant_tables[row][col] == 'o':
            free_tables.append(restaurant_tables[0][col])
            break

print("Our available tables include:")
for table in free_tables:
    print("-", table)
print()

party_size = int(input("What is the size of your party?: ")) # User inputs their party size here

selected_table = None # Program looks for a single table that fits the party size (pt2)
for col in range(len(restaurant_tables[0])):
    table_id = restaurant_tables[0][col]
    capacity = int(table_id[table_id.index('(')+1:table_id.index(')')])
    for row in range(1, len(restaurant_tables)):
        if restaurant_tables[row][col] == 'o' and capacity >= party_size:
            selected_table = table_id
            break
    if selected_table:
        break
# Improvements: Could better handle the edge case if user was to provide invalid integer.

if selected_table: # Prints out a single table recommendation
    print(f"We have found a suitable table for you: {selected_table}.")
else:
    print("No single table can accommodate your party size.")
print()

suitable_tables = [] # Will find all tables that fit the party size (pt3)
for col in range(len(restaurant_tables[0])):
    table_id = restaurant_tables[0][col]
    capacity = int(table_id[table_id.index('(')+1:table_id.index(')')])
    for row in range(1, len(restaurant_tables)):
        if restaurant_tables[row][col] == 'o' and capacity >= party_size:
            suitable_tables.append(table_id)
            break

if suitable_tables:
    print(f"Here are all tables that can accommodate your party, {name}:")
    for table in suitable_tables:
        print("-", table)

# Incomplete pseudocode to check for adjacent table combinations (pt4)
#adjacent_combinations = []
#for each col in range(len(restaurant_tables[0]) - 1):
#    table1 = restaurant_tables...
#    table2 = restaurant_tables...
#
#if adjacent_combinations:
#    print("However, we can combine the following tables for your party:")
#    for combo in adjacent_combinations:
#        print(f"- ___ and ____ can seat _____ people.")
#else:
#    print("Unfortunately, there are no adjacent tables available to combine for your party size.")