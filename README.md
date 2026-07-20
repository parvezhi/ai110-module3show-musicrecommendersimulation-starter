# How The System Works

Real music platforms like Spotify use collaborative filtering (similar users) and content‑based filtering (song attributes). This project focuses on content‑based filtering only. Each song has features like genre, mood, energy, and tempo. The system compares these features to a user’s taste profile and calculates a weighted score.

## Features Used
- genre  
- mood  
- energy (0–1)  
- tempo_bpm  

## Algorithm Recipe
- +3 points for matching genre  
- +2 points for matching mood  
- Energy score = 1 − |song_energy − target_energy|  
- Tempo score = 1 − (|song_tempo − target_tempo| / 200)  
- Final score = sum of all components  

## Sample Recommendation Output

