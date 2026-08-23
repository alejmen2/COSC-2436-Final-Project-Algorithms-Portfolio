from collections import deque


network = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["jonny", "peggy"],
    "anuj": [],
    "peggy": ["you", "alice", "bob"],
    "jonny": ["sam"],
    "sam": []
}


skills = {
    "you": ["javascript"],
    "alice": ["design"],
    "bob": ["sales"],
    "claire": ["management"],
    "anuj": ["manufacturing"],
    "peggy": ["marketing"],
    "jonny": ["testing"],
    "sam": ["python"]
}


def person_has_skill(name, skill_to_find):
    persons_skills = skills.get(name, [])
    return skill_to_find in persons_skills


def search(start_name, skill_to_find):
    search_queue = deque()
    search_queue.extend(network.get(start_name, []))

    searched = set()

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_has_skill(person, skill_to_find):
                return True

            search_queue.extend(network.get(person, []))
            searched.add(person)

    return False


def search_shortest_path(start_name, skill_to_find):
    search_queue = deque(
        (neighbor, 1)
        for neighbor in network.get(start_name, [])
    )

    searched = set()

    while search_queue:
        person, distance = search_queue.popleft()

        if person not in searched:
            if person_has_skill(person, skill_to_find):
                return distance

            for neighbor in network.get(person, []):
                search_queue.append((neighbor, distance + 1))

            searched.add(person)

    return -1


def search_with_path(start_name, skill_to_find):
    search_queue = deque(network.get(start_name, []))

    searched = set()

    came_from = {
        neighbor: start_name
        for neighbor in network.get(start_name, [])
    }

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_has_skill(person, skill_to_find):
                path = [person]

                while path[-1] != start_name:
                    path.append(came_from[path[-1]])

                path.reverse()
                return path

            for neighbor in network.get(person, []):
                if neighbor not in came_from:
                    came_from[neighbor] = person
                    search_queue.append(neighbor)

            searched.add(person)

    return []


if __name__ == "__main__":
    print(
        "Does anyone in my network know Python?",
        search("you", "python")
    )

    print(
        "Does anyone know astronomy?",
        search("you", "astronomy")
    )

    print(
        "Hops to nearest manufacturing contact:",
        search_shortest_path("you", "manufacturing")
    )

    print(
        "Hops to nearest python contact:",
        search_shortest_path("you", "python")
    )

    print(
        "Hops to nonexistent skill:",
        search_shortest_path("you", "astronomy")
    )

    print(
        "Path to manufacturing contact:",
        search_with_path("you", "manufacturing")
    )
