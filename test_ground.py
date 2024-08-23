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
    "Surrender completely.",
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

# Hypnosis metaphor lists
covert_objects = ["cloud", "leaf", "feather", "bubble", "kite", "balloon", "boat", "sail", "butterfly", "bird", "flower", "seed"]
focus_objects = ["laser", "arrow", "telescope", "spotlight", "magnifying glass", "compass", "watch", "clock", "ruler", "pencil"]
covert_actions = ["drifting", "floating", "wandering", "meandering", "soaring", "gliding", "sailing", "flying", "dancing", "swaying"]
focus_actions = ["aiming", "targeting", "zeroing in", "honing in", "focusing", "concentrating", "meditating", "contemplating"]
covert_states = ["relaxation", "ease", "comfort", "tranquility", "peace", "serenity", "calmness", "quietude", "contentment", "bliss"]
focus_states = ["focus", "clarity", "sharpness", "precision", "keenness", "acuity", "awareness", "alertness", "vigilance", "intent"]
intro_phrases = ["I visualize myself as", "I picture myself as", "I envision myself as", "I see myself as", "I perceive myself as", "I imagine myself to be"]

def generate_confusing_sentence():
    """Generates a confusing sentence by combining random fragments in a more structured way."""
    sentence_structure = random.choice([
        "{time_fragment} is {meaning_fragment} of {feeling_fragment} {bypass_fragment} {command}",
        "The {feeling_fragment} of {time_fragment} is a {meaning_fragment} {bypass_fragment} {command}",
        "A {meaning_fragment} emerges from the {feeling_fragment} of {time_fragment} {bypass_fragment} {command}"
    ])
    sentence = sentence_structure.format(
        time_fragment=random.choice(time_fragments),
        meaning_fragment=random.choice(meaning_fragments),
        feeling_fragment=random.choice(feeling_fragments),
        command=random.choice(commands),
        bypass_fragment=random.choice(bypass_fragments)
    )
    return sentence

def generate_hypnosis_metaphor(metaphor_type):
    """Generates a hypnosis metaphor based on the specified type."""
    if metaphor_type == "covert":
        # Use the covert metaphor generator
        objects = covert_objects
        actions = covert_actions
        states = covert_states
        return f"{random.choice(intro_phrases)} a {random.choice(objects)}, gently {random.choice(actions)} on a warm breeze. Feeling the {random.choice(states)}."
    elif metaphor_type == "focus":
        # Use the focus-based metaphor generator
        objects = focus_objects
        actions = focus_actions
        states = focus_states
        return f"{random.choice(intro_phrases)} a {random.choice(objects)}, {random.choice(actions)} on a specific target. Feeling the {random.choice(states)}."
    else:
        raise ValueError("Invalid metaphor type. Please choose 'covert' or 'focus'.")

def generate_sentence(sentence_type, metaphor_type):
    """Generates a sentence based on the specified type."""
    if sentence_type == "confusing":
        return generate_confusing_sentence()
    elif sentence_type == "metaphor":
        return generate_hypnosis_metaphor(metaphor_type)  # Assuming you want covert metaphors
    else:
        raise ValueError("Invalid sentence type. Please choose 'confusing' or 'metaphor'.")

# Get user input for the desired sentence type
sentence_type = input("Please select a sentence type (confusing statement or metaphor): ").strip()

# Generate and print the desired number of sentences
try:
    x = int(input("How many sentences do you want to generate? "))
    for i in range(x):
        if sentence_type == "metaphor":
            metaphor_type = input("Please select a metaphor type (covert or focus): ").strip()
        print(generate_sentence(sentence_type, metaphor_type))
        print(" ")
except ValueError as e:
    print(f"Error: {e}")
