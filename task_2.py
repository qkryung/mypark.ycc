#삼성물산, 에이텍의 PER, PBR을 구하려면? 


s_price = 115500
s_eps = 5477
s_bps = 161837
a_price = 37900
a_eps = 777
a_bps = 9288

s_per = ( s_price / s_eps )
s_pbr = ( s_price / s_bps )
a_per = ( a_price / a_eps )
a_pbr = ( a_price / a_bps )

print(round(s_per,2))
print(round(s_pbr,2))
print(round(a_per,2))
print(round(a_pbr,2))


s_cmt = f"삼성물산의 PER은 {round(s_per,2)}이며 PBR은 {round(s_pbr,2)}입니다"

print(s_cmt)


a_cmt = f"에이텍의 PER은 {round(a_per,2)}이며 PBR은 {round(a_pbr,2)}입니다"

print(a_cmt)
