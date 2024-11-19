import itertools

def main() -> None:

    # Count number of items
    for i in itertools.count():
        print(i)
        if i == 100:
            break

    # Repeat items
    for i in itertools.repeat(10, 4):
        print(i)

    # Sum of items
    for i in itertools.accumulate(range(10, 21)):
        print(i)

    # All possbile permuatations
    items = ["a", "b", "c"]
    # perms = itertools.permutations(items)
    # for perm in perms:
    #     print(perm)

    # Combinations of all options
    perms = itertools.combinations(items, 2)
    for perm in perms:
        print(perm)

    # Chain together two iterables
    more_items = ["d", "e", "f"]
    print(list(itertools.chain(items, more_items)))

    # Filter out items
    print(list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))))

    print(list(itertools.starmap(lambda x, y: x * y , [(10, 2), (3, 3), ( 4, 4)])))

if __name__ == "__main__":
    main()
