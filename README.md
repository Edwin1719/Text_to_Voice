# Text_to_Voice
Text_to_Voice is a Streamlit app for converting text to speech using Eleven Labs' API. Enter text, choose a voice, and play audio instantly. Features include API key entry, multiple voice options, and real-time playback, all within a user-friendly interface ideal for accessibility and custom audio messages.


**FEATURES**

-**Set Up Streamlit Environment:** Install and set up Streamlit in your Python environment. Streamlit provides the framework for creating the app’s interactive UI.

-**Define Voice Dictionary:** Create a dictionary mapping voice names to their respective IDs for easier selection within the app.

-**API Key Entry:** Add a secure text input field to allow users to enter their Eleven Labs API key directly into the app.

-**Text and Voice Input:** Implement a text area for inputting the text to be converted and a dropdown to select from the available voices.

-**Fetch Audio with API:** Write a function to call the Eleven Labs API with the user-input text and selected voice. Handle responses to ensure valid audio is retrieved.

-**Audio Playback:** Integrate audio playback using pygame to allow real-time listening of the generated audio within the app.

-**Developer Info and Branding:** Add branding elements, including a logo, developer information, and social media links to enhance the app’s appearance and usability.
