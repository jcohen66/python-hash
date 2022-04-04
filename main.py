# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from hash_distribution import plot, distribute
from string import printable

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plot(distribute(printable, num_containers=2))
    plot(distribute(printable, num_containers=3))
    plot(distribute(printable, num_containers=30))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
