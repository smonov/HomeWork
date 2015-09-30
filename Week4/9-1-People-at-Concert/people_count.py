#Week4 Task9-1 People_at_concert

def get_people_count(activity):
    counted_people = []
    
    for person in activity:
        if person not in counted_people:
            counted_people += [person]

    return len(counted_people)

print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]))
