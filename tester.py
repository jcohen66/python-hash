from hash_distribution import plot, distribute
from string import printable
from my_hash_func import hash_function
plot(distribute(printable, 6, hash_function))
