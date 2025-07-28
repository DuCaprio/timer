import streamlit as st
import time # 시간 관련 함수 모듈(예: 현재시간 측정)

# 페이지 탭 설정 
st.set_page_config(page_title="위니브 타이머",
                   page_icon="⏰",
                   layout='centered')
# st.markdown("# <span style ='color:Skyblue;'>⏱위니브 타이머</span>",
#             unsafe_allow_html=True)
# st.caption("작업 리듬을 만들어주는 음악 타이머")

# 메인 제목
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h1 style="font-size: 3rem; font-weight: bold;">위니브 타이머⏱</h1>
    <p style="color: #888; font-size: 0.8rem;">작업 리듬을 만들어주는 음악 타이머</p>
</div>
""", unsafe_allow_html=True)

# # 상태 변수 정의 
# # 타이머 실행 
# if 'timer_running' not in st.session_state:
#     st.session_state['timer_running'] = False
# # 타이머 일시정지 
# if 'timer_paused' not in st.session_state:
#     st.session_state['timer_paused'] = False
# # 타이머 시작 시각  
# if 'start_time' not in st.session_state:
#     st.session_state['start_time'] = None # 변수의 성질로 인해 
# # 전체 정지 시간 
# if 'total_paused_time' not in st.session_state:
#     st.session_state['total_paused_time'] = 0 
# if 'remaining_time' not in st.session_state:
#     st.session_state['remaining_time'] = 0
# # 타이머 전체 시간(초 단위)
# if 'total_seconds' not in st.session_state:
#     st.session_state['total_seconds'] = 25*60 # 25분 
# # 타이머 종료 여부 
# if 'timer_completed' not in st.session_state:
#     st.session_state['timer_completed'] = False
# # 타이머 종료 시 축하 애니메이션 표시 여부 
# if 'show_celebration' not in st.session_state:
#     st.session_state['show_celebration'] = False 

# # 함수 정의 
# def update_timer():
#     # 타이머가 실행 중일 때 
#     if st.session_state['timer_running'] and not st.session_state['timer_paused']:
#         current_time = time.time() # 현재 시간 
#         # 타이머가 시작된 이후 실제로 흘러간 시간 
#         elapsed = current_time-st.session_state['start_time'] - st.session_state['total_paused_time']
#         # 남은 시간 = 전체 시간 - 실제 흘러간 시간 
#         remaining_time = st.session_state['total_seconds'] - int(elapsed)

#         if remaining_time<=0:
#             st.session_state['remaining_seconds'] = 0
#             st.session_state['timer_running'] = False
#             st.session_state['timer_completed'] = True
#             st.session_state['show_celebration'] = True
#         else:
#             st.session_state['remaining_seconds'] = remaining_time

