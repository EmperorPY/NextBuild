# NextBuild

A Python project I made while learning Python.

## What it does

NextBuild is a desktop app that gives you a random project idea. You type in a programming language and a difficulty (easy, medium or hard), and it picks a matching project from a library of 500 ideas, so you never run out of things to build for your portfolio.

## Features

* A library of 500 project ideas stored in a JSON file, across 3 difficulty levels and 6 categories (general, web, game, data, mobile and systems).
* Filters by programming language and difficulty, then picks one random match.
* Shows the project title, difficulty, supported languages and category.
* Friendly error message in red when nothing matches, to catch spelling mistakes.
* Modern dark-mode interface built with CustomTkinter, and the Enter key works as a shortcut for the Generate button.
* Fully automated file path handling with the Python OS module, so it runs from any folder.

## What I learned

* How to parse data from a JSON file using the `json` module, and what encoding is and why to use `encoding="utf-8"`.
* How to filter a list of dictionaries with loops and conditions, then choose a random result with `random.choice()`.
* How to use the OS module to find files relative to the script's location.
* How to format output with f-strings and `", ".join()`.

## How to run

Make sure you install the required package first:
```bash
pip install customtkinter
```
Then download the script and `projects.json`, keep them in the same folder, and run the Python file:
```
python NextBuild.py
```

## Made with

Python, CustomTkinter, json, random, os.

## Future improvements

* Dropdown menus instead of typing the language and difficulty.
* Save favourite projects to a file.

## Why did I build this?

Coder's block is common when learning: you want to practise but don't know what to make. NextBuild solves that by matching you with a random project based on your language and difficulty. I built it to practise working with JSON data, filtering lists and building a desktop GUI.
