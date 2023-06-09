import openai
import tkinter as tk
import textwrap

# Set up OpenAI API key
openai.api_key = "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"

def generate_summary(topic):
    # Use OpenAI's GPT-3 to generate summary for the given topic
    prompt = f"Summarize the topic '{topic}' in one paragraph."
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = response.choices[0].text.strip()

    # Wrap the summary to fit within the screen limit
    summary = textwrap.fill(summary, width=80)

    return summary


def search_topics1():
    # Read the topics from a text file
    with open("mathpoints\CSE 201306.05.2023-08.48.05.txt", "r") as file:
        topics = [line.strip() for line in file]

    # Display each topic in the window with a button to show the summary
    for topic in topics:
        topic_label = tk.Label(window, text=topic)
        topic_label.pack(side=tk.TOP)
        summary_button = tk.Button(window, text="Summary", command=lambda t=topic: display_summary(t))
        summary_button.pack(side=tk.TOP)

def search_topics2():
    # Read the topics from a text file
    with open("mathpoints\CSE 2010 06.05.2023-08.58.41.txt", "r") as file:
        topics = [line.strip() for line in file]

    # Display each topic in the window with a button to show the summary
    for topic in topics:
        topic_label = tk.Label(window, text=topic)
        topic_label.pack(side=tk.TOP)
        summary_button = tk.Button(window, text="Summary", command=lambda t=topic: display_summary(t))
        summary_button.pack(side=tk.TOP)

def display_summary(topic):
    # Get the summary for the topic
    summary = generate_summary(topic)

    # Clear the output box and display the summary
    output_box.delete('1.0', tk.END)
    if summary:
        output_box.insert(tk.END, summary)
    else:
        output_box.insert(tk.END, "No summary found.")

# Create the main window
window = tk.Tk()
window.title("Today's Revision")
window.geometry("1080x720")

# Create the button to start the search
search_button1 = tk.Button(window, text="CSE 2013", command=search_topics1, height=10, width=10, bg="pink")
search_button1.pack()
search_button1.place(x=1,y=0)


search_button2 = tk.Button(window, text="CSE 2010", command=search_topics2, height=10, width=10, bg="orange")
search_button2.pack()
search_button2.place(x=100,y=0)


# Create the output box for the summaries
output_box = tk.Text(window)
output_box.pack()

# Start the event loop
window.mainloop()
