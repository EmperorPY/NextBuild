import json      # for reading the projects.json file
import random    # for picking a random project
import os        # for building the file path
import customtkinter as ctk  # the GUI library


# Create the main window
root = ctk.CTk()

# Set the window size
root.geometry("400x650+0")

# Use dark mode for all widgets
ctk.set_appearance_mode("dark")

# File handling
# Get the folder this script is in, so the JSON file is found no matter where it's run from
scriptdir = os.path.dirname(os.path.abspath(__file__))

# Open projects.json and load it into a list of dictionaries
with open(os.path.join(scriptdir, "projects.json"), "r", encoding="utf-8") as f:
    projects = json.load(f)


# Main script

def spit_project():
    # Read what the user typed, removing extra spaces and converting to lowercase
    difficulty = difficulty_entry.get().strip().lower()
    language = language_entry.get().lower().strip()

    # Start with an empty shortlist of matching projects
    matches = []

    # Go through every project
    for p in projects:
        # Keep it only if the difficulty matches...
        if p["difficulty"] == difficulty:
            # ...and the chosen language is in the project's language list
            if language in p["languages"]:
                matches.append(p)

    # If nothing matched, show a red error message and stop
    if len(matches) == 0:
        project_show.configure(text="No projects found.\nCheck difficulty or language for spelling errors", wraplength=300, font=("Inter", 30), text_color="red")
        return

    # Pick one random project from the matches
    chosen = random.choice(matches)

    # Turn the list of languages into one readable string
    languages = ", ".join(chosen["languages"])

    # Show the chosen project's details in white text
    project_show.configure(text=f"{chosen['title']}\n({chosen['difficulty']})\n\nLanguages: {languages}\n\nCategory: {chosen['category']}", wraplength=350, font=("Inter", 30), text_color="white")


# Title label at the top of the window
title = ctk.CTkLabel(root, text="NextBuild", font=("Inter", 60, "italic"))
title.pack(pady=20)

# Text box for the language
language_entry = ctk.CTkEntry(root, placeholder_text="Language")
language_entry.pack(pady=5)

# Text box for the difficulty
difficulty_entry = ctk.CTkEntry(root, placeholder_text="Difficulty")
difficulty_entry.pack(pady=5)

# Button that runs spit_project() when clicked
generate = ctk.CTkButton(root, text="Generate.", text_color="black", fg_color="white",  hover_color="grey", command=spit_project)
generate.pack(pady=10)

# Label that displays the result (empty until a project is generated)
project_show = ctk.CTkLabel(root, text="")
project_show.pack()

# Pressing Enter also runs spit_project()
root.bind("<Return>", lambda event: spit_project())

# Text shown in the window's title bar
root.title("NextBuild - Project Generator")

# Start the app and keep the window open
root.mainloop()