# Model Card — VibeFinder 1.0

## Goal / Task
VibeFinder 1.0 predicts which songs a user will enjoy based on genre, mood, energy, and tempo. It ranks songs using a weighted scoring system.

## Data Used
The dataset contains 15–20 songs with attributes: title, artist, genre, mood, energy (0–1), and tempo_bpm. The dataset is small and not representative of real music diversity.

## Algorithm Summary
The system gives points for matching genre and mood, then adds continuous scores based on how close a song’s energy and tempo are to the user’s preferences. Songs are sorted from highest to lowest score.

## Observed Behavior / Biases
The system strongly favors the user’s favorite genre, which can create a “filter bubble.” Songs with slightly different moods or genres may be ignored even if they match the vibe. The dataset itself is imbalanced, so pop songs appear more often.

## Evaluation Process
I tested multiple profiles (pop/happy, rock/intense, lofi/chill). Each profile shifted the ranking in predictable ways: high‑energy profiles preferred fast songs, while chill profiles preferred low‑energy acoustic tracks.

## Intended Use
This system is meant for educational simulation and demonstrating basic content‑based recommendation logic.

## Non‑Intended Use
Not suitable for real music recommendations, personalization, or commercial deployment.

## Ideas for Improvement
- Add more features like danceability or acousticness.
- Add diversity penalties to avoid repeating artists.
- Add multiple scoring modes (genre‑first, mood‑first).
- Expand dataset to reduce bias.

## Personal Reflection
I learned how simple scoring rules can create surprisingly realistic recommendations. Using AI tools helped speed up brainstorming, but I still needed to verify logic manually. The biggest surprise was how much genre weighting shaped the results. If I continued this project, I’d experiment with hybrid recommenders.
