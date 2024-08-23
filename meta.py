import random

# Lists of words for different types of hypnosis metaphors
covert_objects = ["cloud", "leaf", "feather", "bubble", "kite", "balloon", "boat", "sail", "butterfly", "bird", "flower", "seed"]  # For covert metaphors
focus_objects = ["laser", "arrow", "telescope", "spotlight", "magnifying glass", "compass", "watch", "clock", "ruler", "pencil"]  # For focus metaphors
covert_actions = ["drifting", "floating", "wandering", "meandering", "soaring", "gliding", "sailing", "flying", "dancing", "swaying"]  # For covert metaphors
focus_actions = ["aiming", "targeting", "zeroing in", "honing in", "focusing", "concentrating", "meditating", "contemplating"]  # For focus metaphors
covert_states = ["relaxation", "ease", "comfort", "tranquility", "peace", "serenity", "calmness", "quietude", "contentment", "bliss"]  # For covert metaphors
focus_states = ["focus", "clarity", "sharpness", "precision", "keenness", "acuity", "awareness", "alertness", "vigilance", "intent"]  # For focus metaphors
intro_phrases = ["I visualize myself as", "I picture myself as", "I envision myself as", "I see myself as", "I perceive myself as", "I imagine myself to be"]

def generate_hypnosis_metaphor(metaphor_type):
    """Generates a hypnosis metaphor based on the specified type."""
    if metaphor_type == "relaxation":
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

# Get user input for the desired metaphor type
metaphor_type = input("Please select a metaphor type (relaxation or focus): ")

# Generate and print the desired number of metaphors
x = int(input("How many metaphors do you want to generate? "))
for i in range(x):
    print(generate_hypnosis_metaphor(metaphor_type))
    print(" ")
