# Scenario: You are building a simple waitlist manager for an affordable housing program. 
# Applicants can be added to a waitlist and served (removed) in order. Occasionally, certain applicants (e.g., emergency cases)
# should be prioritized.

# Part 1:
# Applicant Class: Create a class Applicant with attributes like name (string) and an optional priority flag
# (boolean, default False). This class just holds applicant info.

class Applicant:
    def __init__(self, name: str, priority: bool = False):
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"Applicant(name={self.name}, priority={self.priority})"
    
# # Part 2:
# Waitlist Class: Create a class Waitlist that internally maintains a list of Applicant objects in waiting order. Implement methods:
# add_applicant(applicant): Adds a new applicant to the waitlist. By default, add to the end of the list. If the applicant has priority=True,
# add them to the front of the list (so they get served sooner). If an applicant with the same name is already waiting, prevent adding (to avoid duplicates).
# serve_next(): Removes and returns the next Applicant from the list (the one at the front). If the waitlist is empty, return None
# (or indicate that no one is waiting).

class Waitlist:
    def __init__(self):
        self.queue = []

    def add_applicant(self, applicant):
        # prevent duplicates by name
        for existing in self.queue:
            if existing.name == applicant.name:
                print(f"Error: Applicant '{applicant.name}' already in system.")
                return

        if applicant.priority:
            self.queue.insert(0, applicant)  # insert at front
        else:
            self.queue.append(applicant)  # add to back

        print(f"Added {applicant.name} {'(priority)' if applicant.priority else ''}")

    def serve_next(self):
        if not self.queue:
            print("No applicants to serve.")
            return None

        next_applicant = self.queue.pop(0)
        print(f"Serving {next_applicant.name} {'(priority)' if next_applicant.priority else ''}")
        return next_applicant

# Step 3 – Add CLI interaction:
# Accept these commands:

# ADD <name> → regular applicant

# ADDURGENT <name> → priority applicant

# NEXT → serve the next person in line

# EXIT → quit the CLI loop

waitlist = Waitlist()
    
while True:
    commandStr = input("Enter a command:\n")
    # break up command by spaces
    
    commandList = commandStr.strip().split()

    # Handle wrong format
    if len(commandList) == 0:
        print("Please enter a command.")
        continue

    cmd = commandList[0].upper()
    arg = commandList[1] if len(commandList) > 1 else None
    

    
    if cmd == 'ADD' and arg:
        applicant = Applicant(arg)
        waitlist.add_applicant(applicant)
    elif cmd == 'ADDURGENT' and arg:
        applicant = Applicant(arg, priority=True)
        waitlist.add_applicant(applicant)
    elif cmd == 'NEXT':
        waitlist.serve_next()
    elif cmd == 'EXIT':
        break
    else:
        print("Invalid command or missing name.")

    
    
# app1 = Applicant('Danny')
# app2 = Applicant('Sam')
# app3 = Applicant('Owen')

# queue = Waitlist()

# queue.add_applicant(app1)
# queue.add_applicant(app2)
# queue.add_applicant(app3)

# for i in range(0,3):
#     queue.serve_next()
