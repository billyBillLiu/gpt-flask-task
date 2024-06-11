Dependencies: flask, google-generativeai, python-dotenv

**Structure:**

- 1 HTML file (index) and 1 Python file (main)
- HTML file contains a form. When submitted, the form input is passed to main.py
- main.py initializes the google-generativeai API key and model.
- The input is passed through the API and the response is added to a list.
- The user is redirected to index, where the list is displayed.

To Run:
- Install dependencies (flask, google-generative-ai, python-dotenv)
- Make sure the API Key is valid.
- Run main.py and go to the URL shown in the terminal
