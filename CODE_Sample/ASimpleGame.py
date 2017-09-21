class GameObject:
    """docstring for GameObject."""
    class_name = ""
    desc = ""
    objects = {}
    def __init__(self, name):
        class_name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name+"\n"+self.desc

class Goblin(GameObject):
    class_name = "goblin"
    desc = "A foul creature"
goblin = Goblin("Gobby")

def say(noun):
    print("You said{}".format(noun))

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here".format(noun)

def Get_Input():
    command = input(":").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


verb_dict ={
"say":say,
"examine":examine,
}

while True:
    Get_Input()
