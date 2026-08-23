"""
Lab: "Good Enough" -- Greedy Algorithms and Approximation

Three parts:
  Part 1: Greedy gets it exactly right -- classroom scheduling
  Part 2: Greedy gets it wrong -- 0/1 knapsack counterexample
  Part 3: When exact isn't an option -- set covering + subset counting

All data below is hardcoded (no randomness, no file I/O) so results are
reproducible and gradeable.
"""

import itertools


# ---------------------------------------------------------------------------
# Part 1: Greedy gets it exactly right -- classroom scheduling
# ---------------------------------------------------------------------------

def schedule_classes(classes):
    """Given a list of (name, start, end) tuples, greedily pick classes so
    that no two scheduled classes overlap, and as many classes as possible
    get scheduled.

    Greedy rule: always pick the class that ends soonest among the ones
    that don't conflict with what has already been scheduled.
    """
    sorted_classes = sorted(classes, key=lambda c: c[2])

    scheduled = []
    last_end_time = None

    for name, start, end in sorted_classes:
        if last_end_time is None or start >= last_end_time:
            scheduled.append((name, start, end))
            last_end_time = end

    return scheduled


# ---------------------------------------------------------------------------
# Part 2: Greedy gets it wrong -- the knapsack counterexample
# ---------------------------------------------------------------------------

def greedy_knapsack(items, capacity):
    """items: list of (name, value, weight) tuples.
    Greedily grab the most valuable item that still fits in the remaining
    capacity, repeat until nothing else fits.
    """
    sorted_items = sorted(items, key=lambda i: i[1], reverse=True)

    chosen_items = []
    total_value = 0
    remaining_capacity = capacity

    for item in sorted_items:
        name, value, weight = item
        if weight <= remaining_capacity:
            chosen_items.append(item)
            total_value += value
            remaining_capacity -= weight

    return chosen_items, total_value


def brute_force_knapsack(items, capacity):
    """items: list of (name, value, weight) tuples.
    Check every possible subset (use itertools.combinations) and return the
    subset with the highest total value that still fits under capacity.

    Keep this to at most 15 items in practice (2^15 subsets is fast).
    """
    best_items = []
    best_value = 0

    for size in range(len(items) + 1):
        for combo in itertools.combinations(items, size):
            total_weight = sum(item[2] for item in combo)
            if total_weight <= capacity:
                total_value = sum(item[1] for item in combo)
                if total_value > best_value:
                    best_value = total_value
                    best_items = list(combo)

    return best_items, best_value


# ---------------------------------------------------------------------------
# Part 3: When exact isn't an option -- set covering
# ---------------------------------------------------------------------------

def greedy_set_cover(states_needed, stations):
    """states_needed: a set of states that must be covered.
    stations: a dict mapping station name -> set of states it covers.

    Repeatedly pick the station that covers the most still-uncovered
    states, until every needed state is covered.
    """
    final_stations = []
    states_left = states_needed.copy()

    while states_left:
        best_station = None
        best_covered = set()

        for station, states_covered in stations.items():
            covered = states_covered & states_left
            if len(covered) > len(best_covered):
                best_station = station
                best_covered = covered

        if best_station is None:
            break

        final_stations.append(best_station)
        states_left -= best_covered

    return final_stations


def count_subsets(n):
    """Return the number of possible subsets of n items (2**n).

    This is what an exact set-cover / knapsack solver would have to check
    in the worst case -- we print the count instead of ever computing it
    for large n, since 2**100 subsets can never actually be enumerated.
    """
    return 2 ** n


# ---------------------------------------------------------------------------
# Entry point -- deterministic, hardcoded data from the book's examples
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # --- Part 1 data: the book's five-class scheduling table ---
    classes = [
        ("Art", 9.0, 10.0),
        ("English", 9.5, 10.5),
        ("Math", 10.0, 11.0),
        ("CS", 10.5, 11.5),
        ("Music", 11.0, 12.0),
    ]

    scheduled = schedule_classes(classes)
    print("Part 1: Scheduled classes")
    print(scheduled)

    # --- Part 2 data: the book's stereo / laptop / guitar knapsack ---
    items = [
        ("stereo", 3000, 4),
        ("laptop", 2000, 3),
        ("guitar", 1500, 1),
    ]
    capacity = 4

    greedy_items, greedy_value = greedy_knapsack(items, capacity)
    print("Part 2: Greedy knapsack choice")
    print(greedy_items)
    print("Part 2: Greedy knapsack value")
    print(greedy_value)

    best_items, best_value = brute_force_knapsack(items, capacity)
    print("Part 2: Brute-force knapsack choice")
    print(best_items)
    print("Part 2: Brute-force knapsack value")
    print(best_value)

    gap = best_value - greedy_value
    print("Part 2: Gap between brute force and greedy")
    print(gap)

    # --- Part 3 data: the book's radio-station set-covering example ---
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

    stations = {}
    stations["kone"] = {"id", "nv", "ut"}
    stations["ktwo"] = {"wa", "id", "mt"}
    stations["kthree"] = {"or", "nv", "ca"}
    stations["kfour"] = {"nv", "ut"}
    stations["kfive"] = {"ca", "az"}

    final_stations = greedy_set_cover(states_needed, stations)
    print("Part 3: Stations chosen by greedy set cover")
    print(final_stations)

    for n in (5, 20, 100):
        print(f"Part 3: Number of subsets an exact solver checks for n={n}")
        print(count_subsets(n))
