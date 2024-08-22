import random

# Lists of sentence fragments and thematic words
time_fragments = ["yesterday's tomorrow", "the future's past", "time's river", "a fleeting moment", "a distant echo", "a forgotten memory", "a recurring dream", "a fading echo", "a timeless artifact", "a fleeting glimpse"]
meaning_fragments = ["a phantom", "a mirage", "an illusion", "a paradox", "a contradiction", "a mystery", "an enigma", "a conundrum", "a puzzle", "a riddle"]
feeling_fragments = ["bittersweet taste", "haunting memory", "fleeting moment", "lingering sensation", "persistent feeling", "vague impression", "faint recollection", "subtle hint", "unconscious thought", "subliminal message"]
bypass_fragments = ["wich lets me just", "that allows me to just", "that gives me the ability to just", "that brings me to just", "that leads me to just", "createing a sense to just"]
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
    "Surrender.",
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
  """Generates a confusing sentence by combining random fragments."""
  sentence = random.choice(time_fragments) + " is " + random.choice(meaning_fragments) + " of " + random.choice(feeling_fragments) + " " + random.choice(bypass_fragments) + " " + random.choice(commands)
  return sentence

# Generate and print a few sentences

print(generate_confusing_sentence())
