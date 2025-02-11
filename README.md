# Interactive Fairy Tale Generator

This project creates an interactive fairy tale experience for children using GPT for story generation, TTS (Text-to-Speech) for narration, and dynamic options for children to choose the story's progression.

## Overview

- **Purpose:**
  - To provide an engaging and educational storytelling experience for children by allowing them to participate in creating their own stories.
  - Utilizes AI-generated stories and options, voice narration, and visual aids to bring fairy tales to life.

## Features

1. **Story Generation:**
   - Leverages GPT to generate a continuous story based on children's choices.
   - Stories are presented with dynamic options to guide the plot.
2. **Text-to-Speech (TTS):**
   - Uses Google TTS to narrate the generated content in a child-friendly voice.
3. **Image Generation:**
   - Creates cartoon-style illustrations for each part of the story using OpenAI's DALL·E.
4. **Interactive UI:**
   - Built with Gradio for a simple and intuitive interface where children can select story options.
5. **Save and Load:**
   - Stories can be saved and reloaded for future sessions.

## Components

### 1. Backend
- **Python Scripts:**
  - `main.py`: Launches the application.
  - `func.py`: Handles logic for story generation and user interactions.
  - `audio_generate.py`: Generates TTS audio files for narration.
  - `image_generate.py`: Generates illustrations for the story.
  - `structure.py`: Defines the app's layout and flow.
- **GPT API Integration:**
  - Utilizes OpenAI's GPT for text generation.
- **Image API Integration:**
  - Uses OpenAI's DALL·E for creating story illustrations.

### 2. Frontend
- **Gradio Interface:**
  - Provides buttons, sliders, and text areas for user interaction.
  - Displays generated images and plays narration audio.

### 3. Data Files
- `fairy.json`: Predefined fairy tale templates.
- `save_fairy.json`: Stores user-generated stories for retrieval.

## Setup Instructions

### Prerequisites
- Python 3.8 or above.
- Required Python packages: `gradio`, `openai`, `gtts`.

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. **Install Dependencies:**
   ```bash
   pip install gradio openai gtts
   ```
3. **Set Up API Keys:**
   - Add your OpenAI API key in the `initial.py` file:
     ```python
     api_key = 'your_openai_api_key_here'
     ```

### Run the Application
1. Launch the app using the following command:
   ```bash
   python structure.py
   ```
2. Open the provided Gradio link in your web browser.

## Usage

1. Start the application.
2. Choose a fairy tale template or create a new story.
3. Listen to the narration and view the illustrations.
4. Select options to progress the story.
5. Save the story to revisit it later.

## Future Enhancements

- Add more customizable options, such as genre and tone.
- Include multilingual support for narration.
- Expand the library of predefined fairy tales.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

For more details, refer to the provided Python scripts.
