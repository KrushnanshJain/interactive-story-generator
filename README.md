# Interactive Story Generator

This repository contains an interactive story generator that allows writers and creatives to craft detailed, engaging narratives with iterative and cumulative feedback. The tool leverages the Mira SDK and Anthropic's language model to support both the initial creation of a story and its seamless continuation with new segments—all while preserving the established narrative.

## Features

- **Initial Story Creation:** Provide details such as the story overview, genre, themes, magic/tech rules, number of major characters, and key character traits to generate a foundational narrative.
- **Iterative Refinement:** Refine the initial story by supplying feedback in an interactive loop until the narrative meets your vision.
- **Story Continuation:** Append new segments to an established narrative. Each continuation preserves earlier content and ensures a cohesive narrative flow.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Mira SDK (install via `pip install mira_sdk`)
- python-dotenv (install via `pip install python-dotenv`)
- A valid API key provided by Mira

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd interactive-story-generator
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project's root directory and add your Mira API key:
   ```
   API_KEY=your_api_key_here
   ```

3. **Install required packages:**
   If you have a requirements file, run:
   ```bash
   pip install -r requirements.txt
   ```
   
   Otherwise, install directly:
   ```bash
   pip install mira_sdk python-dotenv
   ```

4. **Run the script:**
   Execute the main file to start generating and refining your story:
   ```bash
   python main.py
   ```

## Repository Structure

```
interactive-story-generator/
├── flow.yaml    # YAML file defining the interactive story generation flow and prompts
├── main.py      # Python script for interactive story creation and continuation
├── .env         # Environment variables file (ensure this is in .gitignore for security)
└── README.md    # This file
```

## How to Use the Generator

The story generator operates in two main phases:

- **Phase 1: Initial Story Generation and Refinement**
  - Input the story overview, genre, themes, magic/tech rules, character information, and any initial feedback.
  - An initial story segment is generated.
  - You can iteratively refine the story by providing additional feedback until you are satisfied with the narrative.

- **Phase 2: Interactive Story Continuation**
  - Once the initial story is finalized, you have the option to either conclude the narrative or continue it.
  - For continuations, input new segment details. The newly generated segment will append to the previous narrative while preserving all existing content.


## License

This project is licensed under the MIT License. See the LICENSE file for additional details.

## Contact

For questions or suggestions, feel free to reach out at jainkrushnansh@gmail.com. I truly believe this has great potential and would love to hear your thoughts!
