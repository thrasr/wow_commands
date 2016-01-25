import xchat

__module_name__ = "WoW commands" 
__module_version__ = "0.1" 
__module_description__ = "Adds common /commands from World of Warcraft" 

# To start, use /load wow_commands.py in xchat

# TODO:
# emote commands
# aliases for /msg and /whisper type stuff


#def valid_nick(target, userdata):
  #xchat.get_list("users") # list["nick"]
  # See if %t is in the list of users
  # return false if no valid target

#def dance_cb(word, word_eol, userdata):
#  if word[1] and valid_nick(word[1]):
#    xchat.command("me dances with " + word[1] + ".")
#  else:
#    xchat.command("me bursts into dance.")
#  return xchat.EAT_ALL

#look at current = xchat.get_context() and current.command("me does stuff.")???

'''
def wowcommand_cb(word, word_eol, userdata):
  # Check the command
  cmd = word[0].lower()
  if cmd in defaults:
    # Continue as usual for a standard command
    return xchat.EAT_NONE
  elif cmd in wow.keys():
    # Replace with the appropriate wow command
    # if word[1] and valid_nick(word[1], userdata):
    # if word[1] and word[1] in userdata.nicks: (this would be the target (%t) - a user in the channel)
      # use the secondary definition
      # xchat.command(wow[cmd][1]) # have to do a replace here?
    # else: # print out the primary definition
      # xchat.command(wow[cmd][0])

    xchat.command(wow[word[0].lower()])
    return xchat.EAT_ALL
  #elif word[0].lower() in ?.keys(): # option to add other command dictionaries!
  else:
    return xchat.EAT_NONE
'''


# may have to write one of these for EVERY OPTION?  Hmmm...
xchat.hook_command("dance", dance_cb, help="/dance %t Emotes dancing (optional target %t)")
#xchat.hook_command("", wowcommand_cb)
