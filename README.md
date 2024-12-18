# Bumble Chat Automation

This Python script automates interactions on Bumble by logging in using stored cookies, retrieving the last message from a match, and sending a generated response using OpenAI's GPT-3 model. The goal is to engage in casual and flirty conversations without being too formal or robotic.

## Key Features
- **Automatic Login**: Logs in to Bumble using previously saved cookies.
- **Chat Automation**: Fetches the last message from a random match and generates a custom response using OpenAI's GPT-3.
- **Message Sending**: Sends the generated response to the match.
- **Cookie Management**: Save and load cookies for faster login in the future.

## Prerequisites

Before running the script, ensure that you have the following installed and set up:

- Python 3.7+
- **Selenium**: For browser automation
- **OpenAI**: To generate AI-driven responses
- **Chrome WebDriver**: For automating Chrome browser interactions

## Installation

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/dotslashsimran/Bumble_Automation
   cd Bumble_Automation
    ```

2. **Install Required Libraries**:
    Install the necessary Python packages using `pip`:
    ```bash
    pip install selenium openai
    ```

3. **Download ChromeDriver**:
    Ensure you have the appropriate ChromeDriver version for your Chrome browser. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

4. **Set Up OpenAI API Key**:
    Replace the placeholder `OPENAI_API_KEY` in the script with your OpenAI API key. You can obtain your API key from [OpenAI](https://beta.openai.com/signup/).

5. **Save Cookies**:
    When you first run the script, it will prompt you to log in manually. After logging in successfully, the script will save the cookies to a file (`cookies.json`) for future logins.

## How to Use

1. **Run the Script**:
    To start the automation process, run the script using:
    ```bash
    python bumble_chatbot.py
    ```

    This will open a Chrome browser, navigate to the Bumble app, and attempt to log in using the saved cookies.

2. **Interaction**:
    - Once logged in, the script will fetch a random match from your Bumble connections.
    - It will then retrieve the last message sent by that match and pass it to OpenAI to generate a fun and flirty response.
    - The generated response will be sent back as a message.

3. **Exit**:
    After interacting with a match, the browser window will automatically close.

## Important Notes

- **Cookies**: Cookies are saved in the `cookies.json` file. If the cookies are invalid or expired, you will need to log in manually once more to regenerate the cookies.
- **OpenAI API Key**: Make sure to replace `OPENAI_API_KEY` with your actual API key to enable the chat generation feature.
- **WebDriver Path**: Update the `CHROMEDRIVER_PATH` variable to the correct path of your downloaded ChromeDriver executable.

## Customization

You can modify the following sections in the code to suit your preferences:

- **Message Tone**: Modify the prompt in the `generate_chat_response()` function to adjust the tone or style of responses.
- **Browser Settings**: Customize Chrome options in the `setup_driver()` function for different preferences (e.g., headless mode, window size).
- **Timeouts**: Adjust the `time.sleep()` values to control wait times between interactions.

## Troubleshooting

- **Cookies Not Found**: If the script can't find the cookies file, it will prompt you to log in manually. Ensure that the file `cookies.json` exists and is properly formatted.
- **Message Not Sent**: If the message box element is not found, check the XPath and adjust it if necessary based on updates to the Bumble web app.
