import requests #importing request to make request to the API

API_KEY = "YOUR_API_KEY_GOES_HERE" #Go to the AI21 website and make your own API key

# This is the api url endpoint for j2-large model
API_URL = "https://api.ai21.com/studio/v1/j2-mid/complete"


# ask to draw a request with ai21
def chat_with_ai21(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # data to send to the API
    data = {
        "prompt": prompt,
        "numResults": 1,
        "maxTokens": 1024,  # Number of tokens to generate
        "temperature": 0.4,  # Adjusts randomness of the response
        "topKReturn": 0,
        "topP": 1
    }

    # Let's make a request to the API
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        # store the generated text and return it
        result = response.json()
        return result['completions'][0]['data']['text']
    else:
        return f"Error: {response.status_code}, {response.text}"


#chat with the bot
if __name__ == "__main__":
    print("You can now chat with the AI21 Labs J2-Large model chatbot. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        # Send user input to the AI and get the response
        ai_response = chat_with_ai21(user_input)
        print(f"AI: {ai_response}")
