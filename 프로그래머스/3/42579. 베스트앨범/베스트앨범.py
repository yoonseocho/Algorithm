def solution(genres, plays):
    memo = {}
    
    for idx, val in enumerate(genres):
        memo[(idx, val)] = plays[idx]
    
    genre_play_count = {}
    for (idx, genre), play in memo.items():
        if genre not in genre_play_count:
            genre_play_count[genre] = 0
        genre_play_count[genre] += play
    
    sorted_genres = sorted(genre_play_count.keys(), key=lambda g: genre_play_count[g], reverse=True)
    
    result = []
    for genre in sorted_genres:
        songs = [(idx, play) for (idx, g), play in memo.items() if g == genre]
        top_songs = sorted(songs, key=lambda x: (-x[1], x[0]))[:2]
        result.extend(idx for idx, _ in top_songs)
    return result