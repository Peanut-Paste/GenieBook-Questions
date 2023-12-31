# You've built an inflight entertainment system with on-demand movie streaming.
# Users on longer flights like to start a second movie right when their first one ends, but they complain that the
# plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose
# total runtimes will equal the exact flight length.

# Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes)
# and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals
# flight_length.

# When building your function:
# • Assume your users will watch exactly two movies
# • Don't make your users watch the same movie twice

def two_movies(fl, ml):
    for i, v in enumerate(ml):
        for x in range(i + 1, len(ml)):
            if ml[x] + v == fl:
                return True
    return False

print(two_movies(10, [1, 2, 4, 6]))