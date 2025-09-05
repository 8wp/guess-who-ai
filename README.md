<p><sub>Created by 8wp</sub></p>

<h2>How it works</h2>

<p>This tool is a locally hosted Python script that leverages the OpenAI API to implement a dynamic 20-questions style guessing game. The script maintains a structured conversation history, which is sent as context to the OpenAI endpoint (chat.completions.create) to generate the next question or a final guess. Each interaction is treated as a message in the conversation, allowing the model to reason over prior answers and adapt its line of questioning. The script includes logic to control when the model should make a guess, and all API calls are made in real-time to OpenAI’s gpt-4o-mini model. The architecture is fully local, with no external orchestration — the script handles question generation, history tracking, and response evaluation end-to-end.</p>

<h2>Demonstration</h2>

W.I.P

<h2>Install dependencies</h2>

Run the following command to install all required packages:

```sh
pip install openai
```
<h2>How to use</h2>

<ol>
  <li>Download the <code>guess-who-ai.py</code> file.</li>
  <li>Open the <code>guess-who-ai.py</code> file in a text editor or IDE.</li>
  <li>Create an <a href="https://platform.openai.com/settings/organization/api-keys" target="_blank" rel="noopener noreferrer">OpenAI API</a> key from the OpenAI Developer Platform.</li>
  <li>Paste your api key into the <code>guess-who-ai.py</code> file at <code>line 5</code>, in place of <code>API_KEY</code>.</li>
  <li>Save the updated <code>guess-who-ai.py</code> file, and run it.</li>
  <li>Follow the prompts on the console to play the game.</li>
 
</ol>



