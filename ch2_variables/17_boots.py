# Boots
# You may have already figured this out by now, but below the lesson explanation (or in the Boots tab on mobile), there's an adorable bear-wizard named Boots.

# His job is to help you when if you get stuck. Here's how:

# Boots is an AI chatbot, like ChatGPT, that's been trained on our lessons. When you ask him a question, he already knows:
# The official solution
# What you've been asked to do
# The current state of your code (if you press the clipboard button to paste it in)
# He's been trained to not give you the answer (that's bad for learning), but instead to use the Socratic method to help you figure it out. He asks you follow up questions and explains fundamental concepts to keep you moving forward.
# Chatting with Boots before you've completed a lesson costs a Baked Salmon (he's a hungry guy), or, if you don't have one, 50% of the XP that you'd earn from completing the lesson. You only need to pay once per lesson to start the conversation.
# Chatting with Boots after you've completed a lesson is free. Use this to ask follow up questions, review the concepts, or ask for more examples.
# Assignment
# Fantasy Quest's dialogue messages are all jumbled up. Fix it!

# Run the code. Notice that nothing prints to the console.
# Ask Boots why nothing is printing. You'll need to pay up (just do it). Be sure to click the clipboard icon on the text input to include your code so that he can see it. Notice only what's below the comment is pasted - this is intentional since Boots already has the starting code.
# Use Boots to figure out what's wrong, fix the code, then submit it. We're expecting the following output:
# You there! Adventurer!
# The local mine has been taken over by orcs!
# We need your help taking it back. Bring back 8 of their axes as proof of your hard work.


quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

# don't touch above this line
print(quest_start)
print(quest_middle)
print(quest_end + space + quest_objective)
