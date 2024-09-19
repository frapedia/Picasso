import sys
from graphviz import Digraph

# Check for correct number of arguments
if len(sys.argv) != 2:
    print("┌──────────────────────────────────────────────┐")
    print("|   ____      _                _         _     |")
    print("|  / ___|   _| |__   ___ _ __ / \\   _ __| | _  |")
    print("| | |  | | | |  _ \\ / _ \\ '__/ _ \\ |  __| |/ / |")
    print("| | |__| |_| | |_) |  __/ | / ___ \\| |  |   <  |")
    print("|  \\____\\__, |_ __/ \\___|_|/_/   \\_\\_|  |_|\\_\\ |")
    print("|       |___/   CPM & PSM Development Training |")
    print("|              Picasso State Machine Generator |")
    print("└──────────────────────────────────────────────┘")
    print("Usage: python Picasso.py Process.ini")
    sys.exit(1)

# Read the INI file specified in the command line argument
ini_file = sys.argv[1]

# Create a Digraph
dot = Digraph()

# Initialize variables
in_transitions_section = False

# Open and read the .ini file
with open(ini_file, 'r') as file:
    for line in file:
        line = line.strip()
        
        # Check for section headers
        if line == '[transitions]':
            in_transitions_section = True
            continue
        elif line == '[CPM Parameters Validation]':
            break  # Stop processing when reaching this section

        # Process lines in the transitions section
        if in_transitions_section and line and not line.startswith('#'):  # Ignore comments and empty lines
            state1, transition_name, state2 = [s.strip() for s in line.split(',')]
            dot.node(state1)
            dot.node(state2)
            dot.edge(state1, state2, label=transition_name)

# Save and render the diagram
dot.render('state_machine_diagram', format='png', cleanup=True)

print("Picasso has generated your state machine diagram as 'state_machine_diagram.png'")
