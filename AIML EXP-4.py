courses = {
    'c-language':   ('T1', 40, []),
    'Physics101':('T2', 30, ['Mon-9']),
    'Chem101':   ('T1', 20, []),
    'Bio101':    ('T3', 25, ['Tue-10']),
    'Python-3':     ('T4', 60, []),
    'Signals':    ('T2', 35, [])
}

time_slots = ['Mon-9', 'Mon-10', 'Tue-9', 'Tue-10']

rooms = {
    'R1': 50,
    'R2': 30,
    'R3': 70
}

# Keep track of which rooms and teachers are booked at which times
room_schedule = {room: set() for room in rooms}
teacher_schedule = {}

assignments = {}

for course, (teacher, students, preferred_times) in courses.items():
    possible_times = preferred_times if preferred_times else time_slots
    
    assigned = False
    for time in possible_times:
        # Check if teacher is free at this time
        if teacher in teacher_schedule and time in teacher_schedule[teacher]:
            continue
        
        # Find a room with enough capacity that's free at this time
        for room, capacity in rooms.items():
            if capacity >= students and time not in room_schedule[room]:
                # Assign this course to this room and time
                assignments[course] = (room, time)
                
                # Mark room and teacher as busy at this time
                room_schedule[room].add(time)
                teacher_schedule.setdefault(teacher, set()).add(time)
                
                assigned = True
                break
        
        if assigned:
            break
    
    if not assigned:
        assignments[course] = None  # Could not find a slot

# Print the assignments
for course, assignment in assignments.items():
    if assignment:
        room, time = assignment
        print(f"{course} assigned to {room} at {time}")
    else:
        print(f"{course} could not be assigned a room and time slot.")
