import random

# Lists of sentence fragments and thematic words
time_fragments = ["the future's past", "time's river", "a fleeting moment", "a distant echo", "a forgotten memory", "a recurring dream", "a fading echo", "a timeless artifact", "a fleeting glimpse"]
meaning_fragments = ["phantom", "mirage", "an illusion", "paradox", "contradiction", "mystery", "enigma", "conundrum", "puzzle", "riddle"]
feeling_fragments = ["bittersweet taste", "haunting memory", "fleeting moment", "lingering sensation", "persistent feeling", "vague impression", "faint recollection", "subtle hint", "unconscious thought", "subliminal message"]
bypass_fragments = ["which lets me just", "that allows me to just", "that gives me the ability to just", "that brings me to just", "that leads me to just", "creating a sense to kinda"]
commands = [
    "Breathe deeply.",
    "Relax completely.",
    "Empty my mind.",
    "Drift away.",
    "Savor the moment.",
    "Be present.",
    "Trust completely.",
    "Feel the calm.",
    "Release tension.",
    "Soften.",
    "Let go.",
    "Imagine peace.",
    "Find stillness.",
    "Surrender compleatly.",
    "Be at one.",
    "Release worry.",
    "Find serenity.",
    "Embrace peace.",
    "Let go of resistance.",
    "Yield to tranquility.",
    "Embrace the moment.",
    "Let go of control.",
    "Allow peace to flow.",
    "Feel the weight lift.",
    "Embrace the present.",
    "Let go of expectations.",
    "Trust the process.",
    "Release the past.",
    "Focus on the present.",
    "Let go of the future.",
    "Be here now.",
    "Embrace the moment.",
    "Let go of control.",
    "Allow peace to flow.",
    "Feel the weight lift.",
    "Embrace the present.",
    "Let go of expectations.",
    "Trust the process.",
    "Release the past.",
    "Focus on the present.",
    "Let go of the future.",
    "Be here now.",
]

def generate_confusing_sentence():
    """Generates a confusing sentence by combining random fragments in a more structured way."""
    sentence_structure = random.choice([
        "{time_fragment} is a {meaning_fragment} of {feeling_fragment} {bypass_fragment} {command}",
        "The {feeling_fragment} of a {time_fragment} is a {meaning_fragment} {bypass_fragment} {command}",
        "A {meaning_fragment} emerges from the {feeling_fragment} of a {time_fragment} {bypass_fragment} {command}"
    ])
    sentence = sentence_structure.format(
        time_fragment=random.choice(time_fragments),
        meaning_fragment=random.choice(meaning_fragments),
        feeling_fragment=random.choice(feeling_fragments),
        command=random.choice(commands),
        bypass_fragment=random.choice(bypass_fragments)
    )
    return sentence

# Generate and print a few sentences
x = input("number of sentences you want to print: ")
for i in range(int(x)):
    print(generate_confusing_sentence())
    print(" ")
