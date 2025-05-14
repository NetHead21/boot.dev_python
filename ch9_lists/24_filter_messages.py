# Filter Messages
# You are about to write a bit more code in a single function than you have before.

# Do not try to write it all at once. Start with the outermost loop, and work your way inwards. Add extra print() statements and run your code often to make sure it's doing what you expect. Just make sure to remove the extra print() statements before submitting your code.

# Running your code often to make sure each line is doing what you expect is called "debugging". All programmers, even seasoned professionals, break large problems down into small ones that they can debug line by line.

# Assignment
# We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

# A list of the same messages but with all instances of the word dang removed.
# A list containing the number of dang words that were removed from the message at that particular index.
# Here are some examples:

# messages = ["dang it bobby!", "look at it go"]
# filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

# messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
# filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]

# Here are the steps for you to follow:

# Create the 2 empty lists that you'll return at the end:
# One for the filtered messages.
# And one for counts of words removed.
# For each message in the input list:
# Split the message into a list of words using the .split() string method (see below for help).
# Create a new empty list for all the non-bad words for this message.
# Create a removed variable and set it to 0. We'll increment this when we remove words from this message.
# For each word in the message:
# If the word is dang, increment removed
# If it is not dang, add the word to the non-bad word list you created
# Join the list of non-bad words into a single string using the .join() method (see below for help)
# Append the new clean message to the final list of filtered messages
# Append the count of bad words removed to its list
# Return the filtered messages first, then the counters
# Tips
# Because we are working with strings that need to be converted to lists and vice versa, here are some very helpful Python methods we can use to make our lives much easier.

# Split a String Into a List of Words
# The .split() method in Python is called on a string and returns a list by splitting the string based on a given delimiter. If no delimiter is provided, it will split the string on whitespace. Here's a quick example:

# message = "hello there sam"
# words = message.split()
# print(words)
# # Prints: ["hello", "there", "sam"]

# Join a List of Strings Into a Single String
# The .join() method is called on a delimiter (what goes between all the words in the list), and takes a list of strings as input.

# list_of_words = ["hello", "there", "sam"]
# sentence = " ".join(list_of_words)
# print(sentence)
# # Prints: "hello there sam"


def filter_messages(messages):
    filtered_messages = []  # Stores cleaned messages
    removal_counts = []  # Stores count of removed words

    for message in messages:
        words = message.split()  # Split message into words
        cleaned_words = []  # Stores words that are not "dang"
        count = 0  # Counter for "dang" removals

        for word in words:
            if word.lower() == "dang":  # Check if word is "dang" (case insensitive)
                count += 1
            else:
                cleaned_words.append(word)

        filtered_messages.append(" ".join(cleaned_words))  # Rebuild cleaned message
        removal_counts.append(count)

    return filtered_messages, removal_counts
