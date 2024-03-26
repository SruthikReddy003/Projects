def first(s, productions):
    first_set = set()

    for i in range(len(productions[s])):
        for j in range(len(productions[s][i])):
            c = productions[s][i][j]

            if c.isupper():  # If c is a Non-Terminal
                f = first(c, productions)
                if 'eps' not in f:  # If A->BC then First(A)=First(B) if eps not in First of B
                    first_set |= f
                    break
                else:  # If eps in First of B then First(A)=First(B) union First(C)
                    if j == len(productions[s][i]) - 1:
                        first_set |= f
                    else:
                        f.discard('eps')
                        first_set |= f

            else:  # If A->a alpha First(A)={a}
                first_set.add(c)
                break

    return first_set

# -------------------------------------------------------------------------------------------------------------------------------------

def follow(s, productions, start_symbol):
    follow = set()

    # Add $ to the start symbol's FOLLOW set
    if s == start_symbol:
        follow.add('$')

    for nt, prod in productions.items():
        for p in prod:
            if s in p:
                idx = p.index(s)
                if idx + 1 < len(p):  # Check if there is a next symbol
                    next_sym = p[idx + 1]
                    if next_sym.isupper():
                        follow |= first_sets[next_sym]
                        follow.discard('eps')
                        if 'eps' in first_sets[next_sym] or idx == len(p) - 1:
                            follow |= follow(nt, productions, start_symbol)
                    else:
                        follow.add(next_sym)

    return follow


# Given productions
productions = {
    'S': ['AB', 'BC'],
    'A': ['aA', ''],
    'B': ['bB', ''],
    'C': ['cC', '']
}

# Start symbol
start_symbol = 'S'

# Calculate FIRST sets for each non-terminal symbol
first_sets = {}
for symbol in productions.keys():
    first_sets[symbol] = first(symbol, productions)

# Calculate FOLLOW sets for each non-terminal symbol
follow_sets = {}
for symbol in productions.keys():
    follow_sets[symbol] = follow(symbol, productions, start_symbol)


# Print FIRST and FOLLOW sets
print("FIRST Sets:")
for symbol, first_set in first_sets.items():
    print(f"FIRST({symbol}): {first_set}")

print("\nFOLLOW Sets:")
for symbol, follow_set in follow_sets.items():
    print(f"FOLLOW({symbol}): {follow_set}")
#-------------------------------------------------------------------------------------------------------------------------------------
print("")
# Got Function
def goto(s, productions, state):
    # Get the productions for the current state
    current_productions = productions.get(state, [])
    
    # Iterate through the productions
    for production in current_productions:
        # Check if the non-terminal symbol s is present in the production
        if s in production:
            # Find the index of the non-terminal symbol s in the production
            index = production.index(s)
            # Check if there is a next state
            if index + 1 < len(production):
                return production[index + 1]  # Return the next state
    return None  # No transition found

# Given productions
productions = {
    'S': ['AB', 'BC'],
    'A': ['aA', ''],
    'B': ['bB', ''],
    'C': ['cC', '']
}

# Example usage:
s = 'A'  # Non-terminal symbol
state = 'S'  # Current state
next_state = goto(s, productions, state)
if next_state is not None:
    print(f"Transition from {state} with symbol {s}: {next_state}")
else:
    print(f"No transition found for symbol {s} in state {state}")

