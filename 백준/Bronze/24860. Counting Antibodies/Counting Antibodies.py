v_kap, j_kap = map(int, input().split())
v_lam, j_lam = map(int, input().split())
v_h, d_h, j_h = map(int, input().split())
print(v_h * d_h * j_h * (v_kap * j_kap + v_lam * j_lam))