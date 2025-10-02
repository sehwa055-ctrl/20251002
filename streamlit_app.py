import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 삼각형 각 변 입력
st.header("삼각형 변 입력 및 피타고라스 정리 풀이")
a = st.number_input("변 a", min_value=1, step=1, format="%d")
b = st.number_input("변 b", min_value=1, step=1, format="%d")
c = st.number_input("변 c", min_value=1, step=1, format="%d")


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# 한글 폰트 설정
font_path = "fonts/NanumGothic-Regular.ttf"
fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = fontprop.get_name()
plt.rcParams['axes.unicode_minus'] = False

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def draw_triangle(a, b, c):
    # 삼각형 좌표 계산 (a, b, c가 실제 삼각형을 만들 수 있을 때)
    # A(0,0), B(a,0), C(x,y) 계산
    # 코사인 법칙 이용
    if not is_triangle(a, b, c):
        st.error("입력값으로 삼각형을 만들 수 없습니다.")
        return
    # C(x, y) 계산
    x = (a**2 + c**2 - b**2) / (2*a)
    y = np.sqrt(max(c**2 - x**2, 0))
    fig, ax = plt.subplots()
    ax.plot([0, a, x], [0, 0, y], 'bo-')
    ax.set_aspect('equal')
    ax.set_xlim(-1, max(a, x)+1)
    ax.set_ylim(-1, max(y, 1)+1)
    ax.text(0, 0, 'A', fontsize=12, fontproperties=fontprop)
    ax.text(a, 0, 'B', fontsize=12, fontproperties=fontprop)
    ax.text(x, y, 'C', fontsize=12, fontproperties=fontprop)
    ax.set_title('입력값으로 그린 삼각형', fontproperties=fontprop)
    st.pyplot(fig)

def pythagoras_explain(a, b, c):
    # 피타고라스 정리 판정 및 풀이
    sides = sorted([a, b, c])
    a_, b_, c_ = sides  # c_가 가장 긴 변
    st.subheader("피타고라스 정리 풀이")
    st.write(f"가장 긴 변: {c_}, 나머지: {a_}, {b_}")
    st.latex(f"{a_}^2 + {b_}^2 = {a_**2:.2f} + {b_**2:.2f} = {a_**2 + b_**2:.2f}")
    st.latex(f"{c_}^2 = {c_**2:.2f}")
    if np.isclose(a_**2 + b_**2, c_**2):
        st.success("피타고라스 정리가 성립합니다. 직각삼각형입니다.")
    else:
        st.warning("피타고라스 정리가 성립하지 않습니다. 직각삼각형이 아닙니다.")

if a > 0 and b > 0 and c > 0:
    draw_triangle(a, b, c)
    pythagoras_explain(a, b, c)
