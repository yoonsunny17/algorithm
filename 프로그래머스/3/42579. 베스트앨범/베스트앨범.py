def solution(genres, plays):
    # 각 장르별로 총 재생 수 계산
    total_plays = {}
    musics = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 총 재생 수 누적
        if genre not in total_plays:
            total_plays[genre] = play
        else:
            total_plays[genre] += play

        # 장르별 곡 저장 (재생 수, 고유번호)
        if genre not in musics:
            musics[genre] = [[play, i]]
        else:
            musics[genre].append([play, i])
    
    # 장르별 총 재생 수 많은 순 정렬
    sorted_musics = dict(sorted(musics.items(), key=lambda item: sum(x[0] for x in item[1]), reverse=True))

    ans = []

    # 각 장르 내의 곡 정렬 (재생 수 많은 > 고유번호 낮은)
    for k, v in sorted_musics.items():
        v.sort(key=lambda x:(x[0], -x[1]), reverse=True)
        sorted_musics[k] = v[:2]

    for v in sorted_musics.values():
        for i in range(len(v)):
            ans.append(v[i][1])

    return ans