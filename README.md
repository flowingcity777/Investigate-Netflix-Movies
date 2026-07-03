# Investigate Netflix Movies

A Python-based data analysis project that explores Netflix's movie catalog to investigate trends in movie durations over time. 

## Project Overview
There is a common perception that movies on streaming platforms have been getting shorter in recent years. This project analyzes a historical dataset of Netflix movies to test this hypothesis, visualize duration trends, and break down the data by release year and genre.

## Features
- **Data Cleaning:** Filters out TV shows and non-movie content to focus purely on feature films.
- **Trend Analysis:** Examines how the average runtime of movies has evolved over the decades.
- **Genre Insights:** Identifies specific genres (like Documentaries, Children, and Stand-Up) that might skew the overall duration averages.
- **Data Visualization:** Uses matplotlib to create clear, color-coded scatter plots to easily spot patterns and outliers.

## File Structure
- `investigate_netflix_movies.py`: The main Python script containing the data loading, filtering, analysis, and visualization logic.
- `.gitignore`: Standard rules to avoid committing unnecessary or temporary files.
- `LICENSE`: MIT License.

## Prerequisites
To run the script locally, you need Python installed along with the following libraries:
- `pandas`
- `matplotlib`

You can install them via pip:
```bash
pip install pandas matplotlib
