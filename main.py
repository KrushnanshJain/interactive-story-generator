from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# Initialize the Mira client
client = MiraClient(config={"API_KEY": api_key})

# Load the generation flow from the YAML file
generation_flow = Flow(source="flow.yaml")

# Define our initial generation inputs
gen_inputs = {
    "story_overview": "A post-apocalyptic world where magic and technology coexist.",
    "genre": "Fantasy",
    "themes": "Rebellion, survival",
    "magic_or_tech_rules": "Magic is powered by emotions; technology is ancient and hard to repair.",
    "major_characters": 5,
    "character_traits": "Heroic leader, cunning rogue, wise mentor",
    "feedback": "",  # Will accumulate user feedback over time
    "story": ""   # Initially empty; will hold the generated story
}

# PHASE 1: Generate Initial Story & Refine with Feedback
print("Step 1: Generating initial story...\n")
# Extract the generated content from the returned dictionary
gen_response = client.flow.test(generation_flow, gen_inputs)
generated_story = gen_response["result"]
print("Story:")
print(generated_story)

# Allow the user to refine the story with iterative feedback.
all_feedback = ""
while True:
    user_feedback = input("\nEnter further feedback to refine the story (or press Enter to finalize the story): ").strip()
    
    if not user_feedback:
        print("Story finalized.")
        break
    
    all_feedback += f" {user_feedback}"
    gen_inputs["feedback"] = all_feedback.strip()
    gen_inputs["story"] = generated_story

    gen_response = client.flow.test(generation_flow, gen_inputs)
    generated_story = gen_response["result"]
    
    print("\nRevised Story:")
    print(generated_story)

# Save the finalized story as final_story
final_story = generated_story

# PHASE 2: Interactive Story Continuation
print("\n--- Story Finalized ---")
print("You now have two options:")
print("  1. Conclude the story (press Enter)")
print("  2. Continue the story (type 'C' and press Enter)")

while True:
    choice = input("\nWould you like to continue the story? (Enter 'C' to continue, or press Enter to conclude): ").strip()
    
    if choice.lower() != 'c':
        print("\nFinal Story:")
        print(final_story)
        break

    # Prompt for additional inputs for the story continuation
    new_feedback = input("\nEnter details for the next segment of the story: ").strip()
    
    # Provide the new instructions while preserving the established story
    gen_inputs["feedback"] = new_feedback
    gen_inputs["story"] = final_story

    # Extract the new segment from the returned dictionary
    gen_response = client.flow.test(generation_flow, gen_inputs)
    new_segment = gen_response["result"]
    
    # Append the new segment to the existing story
    final_story = final_story + "\n" + new_segment
    print("\nStory updated with new segment:")
    print(final_story)

    print("\n-- Would you like to add another segment? --")
