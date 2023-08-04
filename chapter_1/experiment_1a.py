# Experiment 1-A:
# Write a python list comprehension that returns the individual characters of a string 
# that are not whitespace characters. Apply it to a string "4 and 20 blackbirds.\n"

string = "4 and 20 blackbirds.\n"

if __name__ == "__main__":
    # Solution:
    print([char for char in string.strip() if char != " "])