import random

wt = ('ドド', 'スコ')
t = (
    # dummy
    (),
    # st.1
    (2, 1), #ドド
    # st.2
    (2, 3), #スコ
    # st.3
    (2, 4), #スコ
    # st.4
    (2, 1), #スコ
)

cur_st, nxt_st = 1, 1

[
    [
        [
            (cur_st:=nxt_st),
            (nxt_st:=t[cur_st][w]),
            print(wt[w], end=''),
            print('❤❤ラブ注入❤❤', end='') if cur_st == 4 and w == 1 else None,
        ]
        for w in (random.choice((0,1)),)
    ]
    for i in range(0,1000)
]

