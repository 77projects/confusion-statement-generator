import random

# Lists of sentence fragments and thematic words
time_fragments = ["yesterday's tomorrow", "the future's past", "time's river", "a fleeting moment", "a distant echo", "a forgotten memory", "a recurring dream", "a fading echo", "a timeless artifact", "a fleeting glimpse"]
meaning_fragments = ["a phantom", "a mirage", "an illusion", "a paradox", "a contradiction", "a mystery", "an enigma", "a conundrum", "a puzzle", "a riddle"]
feeling_fragments = ["bittersweet taste", "haunting memory", "fleeting moment", "lingering sensation", "persistent feeling", "vague impression", "faint recollection", "subtle hint", "unconscious thought", "subliminal message"]
bypass_fragments = ["wich lets me just", "that allows me to just", "that gives me the ability to", "that brings me to just", "that leads to simply", "createing a sense of simply"]
relaxation_commands = [
    "Surrender to stillness.",
    "Let go of everything, except peace.",
    "Be completely present, completely calm.",
    "Allow my body to relax, soften, and release tension.",
    "Picture myself floating on a calm, serene lake.",
    "Imagine my mind is a clear, still pond, reflecting the sky above.",
    "Breathe deeply and slowly, feeling my body relax with each exhale.",
    "Visualize stress and tension melting away like ice in the sun.",
    "Let go of worry, doubt, and fear",
    "Feel a wave of relaxation",
    "Picture a beautiful, peaceful scene",
    "surrender completely",
    "relax completely",
    "Let go of any thoughts or worries.",
    "Feel a sense of calm and serenity.",
    "Let go of any negative emotions, ",
]

def generate_confusing_sentence():
  """Generates a confusing sentence by combining random fragments."""
  sentence = random.choice(time_fragments) + " is " + random.choice(meaning_fragments) + " of " + random.choice(feeling_fragments) + " " + random.choice(bypass_fragments) + " " + random.choice(relaxation_commands)
  return sentence

# Generate and print a few sentences

print(generate_confusing_sentence())