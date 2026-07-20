def score_song(user_prefs, song):
    """
    Calculate a weighted relevance score for a single song.
    Returns a tuple: (final_score, reasons_list)
    """

    reasons = []
    score = 0.0

    # --- Genre Match (High Weight) ---
    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 3.0
        reasons.append("Genre match (+3)")
    else:
        reasons.append("Genre mismatch (+0)")

    # --- Mood Match (Medium Weight) ---
    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 2.0
        reasons.append("Mood match (+2)")
    else:
        reasons.append("Mood mismatch (+0)")

    # --- Energy Score (Continuous Feature) ---
    # Closer energy → higher score
    energy_gap = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = 1 - energy_gap  # range: 0 to 1
    score += energy_score
    reasons.append(f"Energy closeness (+{energy_score:.2f})")

    # --- Tempo Score (Continuous Feature) ---
    # Normalize tempo difference by dividing by 200 BPM
    tempo_gap = abs(song["tempo_bpm"] - user_prefs["target_tempo"]) / 200
    tempo_score = max(0, 1 - tempo_gap)  # avoid negative scores
    score += tempo_score
    reasons.append(f"Tempo closeness (+{tempo_score:.2f})")

    return score, reasons

import csv

def load_songs(csv_path="data/songs.csv"):
    songs = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            songs.append(row)
    return songs


def score_song(user_prefs, song):
    # Paste the scoring function here
    pass


def recommend_songs(user_prefs, songs, k=5):
    scored = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append({
            "title": song["title"],
            "artist": song["artist"],
            "score": score,
            "reasons": reasons
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:k]


def main():
    songs = load_songs()
    print(f"Loaded songs: {len(songs)}")

    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.7,
        "target_tempo": 120
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations:")
    for rec in recommendations:
        print(f"\n🎵 {rec['title']} — Score: {rec['score']:.2f}")
        for reason in rec["reasons"]:
            print(f"   - {reason}")


if __name__ == "__main__":
    main()

