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
