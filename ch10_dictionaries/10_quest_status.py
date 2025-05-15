# Quest Status
# Fantasy Quest stores each character's progress in a nested dictionary structure, here's what it looks like:

# {
#     "entity": {
#         "character": {
#             "name": "Kaladin",
#             "quests": {
#                 "bridge_run": {
#                     "status": "In Progress",
#                 },
#                 "talk_to_syl": {
#                     "status": "Completed",
#                 },
#             },
#         }
#     }
# }

# The values can change of course, but the structure will always be the same. For example, another character's might look like this:

# {
#     "entity": {
#         "character": {
#             "name": "Shallan",
#             "quests": {
#                 "bridge_run": {
#                     "status": "Completed",
#                 },
#                 "talk_to_syl": {
#                     "status": "In Progress",
#                 },
#             },
#         }
#     }
# }

# Assignment
# Complete the get_quest_status function. It accepts a progress dictionary (structure defined above) and returns the character's status in the "bridge_run" quest.

# Tip
# You can chain dictionary keys to access a dictionary inside of another dictionary:

# outer_dictionary["outer_key"]["inner_key"]


def get_quest_status(progress):
    return progress["entity"]["character"]["quests"]["bridge_run"]["status"]
