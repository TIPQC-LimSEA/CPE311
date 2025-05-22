# Brain Teaser: Tower of Hanoi ^_^
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move peg 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move peg {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

tower_of_hanoi(3, 'A', 'C', 'B')
