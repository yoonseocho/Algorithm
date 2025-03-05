def solution(genres, plays):
    memo = {}
    for idx, val in enumerate(genres):
        memo[(idx, val)] = plays[idx]
        
    genre_count = {}
    for (idx, genre), play in memo.items():
        if genre not in genre_count:
            genre_count[genre] = 0
        genre_count[genre] += play
    
    sorted_genres = sorted(genre_count.keys(), key=lambda g: genre_count[g], reverse=True)
    
    result = []
    for genre in sorted_genres:
        songs = [(idx, play) for (idx, g), play in memo.items() if g == genre]
        songs.sort(key=lambda x: (-x[1], x[0]))
        result.extend(idx for idx, _ in songs[:2])
        
    return result