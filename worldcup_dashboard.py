import streamlit as st
import pandas as pd
import fact_data
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(page_title="2026 월드컵 대시보드 V2", page_icon="⚽", layout="wide")

# 사이드바 BGM 플레이어
st.sidebar.header("🎵 2026 월드컵 공식 주제가")
st.sidebar.markdown("**Shakira, Burna Boy – Dai Dai (Official Song)**")
st.sidebar.audio("2026_anthem.m4a", format="audio/m4a")

st.sidebar.markdown("---")
st.sidebar.subheader("📺 라이브 중계 바로가기")
st.sidebar.markdown("""[🔗 JTBC 스포츠 생중계](https://jtbc.co.kr/)

[🔗 KBS 스포츠 생중계](https://sports.kbs.co.kr/)

[🔗 네이버 치지직 (CHZZK)](https://chzzk.naver.com/)""")

st.title("🏆 2026 북중미 월드컵 스페셜 대시보드 (PRO)")
st.markdown("데이터 분석, 조별리그 풀 시뮬레이션, 토너먼트 대진표까지 결합된 궁극의 월드컵 대시보드입니다.")

# 탭 생성 (7개 탭으로 구성)
tabs = st.tabs([
    "📋 48개국 조편성 (A~L조)",
    "🇰🇷 조별리그 시뮬레이터",
    "🌍 개최 도시 맵",
    "🏆 서바이벌 토너먼트",
    "⭐ 선수 프로필 & 비교",
    "⏱️ 시차 변환기",
    "📰 뉴스 & 퀴즈 예측",
    "📋 한국 스쿼드 & 전술",
    "🏟️ 드림팀 베스트 11"
])

# ==========================================
# 1. 🌍 개최 도시 맵
# ==========================================
with tabs[2]:
    st.header("🌍 2026 북중미 3개국 16개 개최 도시 네트워크")
    st.markdown("결승전이 열리는 뉴욕/뉴저지를 중심으로 북중미 전역을 연결하는 거대한 월드컵 3D 네트워크입니다. (우클릭 드래그로 3D 회전 가능)")
    
    import pydeck as pdk
    
    cities_data = {
        'City': ['New York/NJ (Final)', 'Los Angeles', 'Dallas', 'Miami', 'Toronto', 'Vancouver', 'Mexico City', 'Monterrey', 'Seattle', 'San Francisco', 'Houston', 'Atlanta', 'Philadelphia', 'Boston', 'Kansas City', 'Guadalajara'],
        'Country': ['US', 'US', 'US', 'US', 'Canada', 'Canada', 'Mexico', 'Mexico', 'US', 'US', 'US', 'US', 'US', 'US', 'US', 'Mexico'],
        'Stadium': ['MetLife Stadium', 'SoFi Stadium', 'AT&T Stadium', 'Hard Rock Stadium', 'BMO Field', 'BC Place', 'Estadio Azteca', 'Estadio BBVA', 'Lumen Field', "Levi's Stadium", 'NRG Stadium', 'Mercedes-Benz Stadium', 'Lincoln Financial Field', 'Gillette Stadium', 'Arrowhead Stadium', 'Estadio Akron'],
        'lat': [40.8136, 33.9534, 32.7473, 25.9580, 43.6332, 49.2768, 19.3029, 25.6700, 47.6062, 37.7749, 29.7604, 33.7490, 39.9526, 42.3601, 39.0997, 20.6597],
        'lon': [-74.0744, -118.3387, -97.0945, -80.2389, -79.4186, -123.1118, -99.1505, -100.2444, -122.3321, -122.4194, -95.3698, -84.3880, -75.1652, -71.0589, -94.5786, -103.3496],
        'Stadium Capacity': [82500, 70240, 80000, 64767, 30000, 54500, 87523, 51000, 69000, 68500, 72220, 71000, 69796, 65878, 76416, 49850],
        'Image': ['https://upload.wikimedia.org/wikipedia/commons/0/04/Metlife_stadium_%28Aerial_view%29.jpg', 'https://upload.wikimedia.org/wikipedia/commons/b/b3/SoFi_Stadium_2023.jpg', 'https://upload.wikimedia.org/wikipedia/commons/1/11/Arlington_June_2020_4_%28AT%26T_Stadium%29.jpg', 'https://upload.wikimedia.org/wikipedia/commons/c/ce/Hard_Rock_Stadium_for_Super_Bowl_LIV_%2849606710103%29.jpg', 'https://upload.wikimedia.org/wikipedia/commons/9/91/Toronto_BMO_Field_in_2024.jpg', 'https://upload.wikimedia.org/wikipedia/commons/f/ff/BC_Place_2015_Women%27s_FIFA_World_Cup.jpg', 'https://upload.wikimedia.org/wikipedia/commons/0/07/Vista_a%C3%A9rea_del_Estadio_Azteca_-_2026_-_02.jpg', 'https://upload.wikimedia.org/wikipedia/commons/5/57/Mexico_Guadalupe_Monterrey_Estadio_BBVA_Bancomer_fifa_world_cup_2026_6.JPG', 'https://upload.wikimedia.org/wikipedia/commons/c/c8/2026_FIFA_World_Cup_-_Belgium_v._Egypt_in_Seattle_-_04.jpg', 'https://upload.wikimedia.org/wikipedia/commons/a/a6/Levi%27s_Stadium_in_February_2016_prior_to_Super_Bowl_50_%2824398261729%29.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Nrg_stadium.jpg/960px-Nrg_stadium.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Mercedes_Benz_Stadium_time_lapse_capture_2017-08-13.jpg/960px-Mercedes_Benz_Stadium_time_lapse_capture_2017-08-13.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Lincoln_Financial_Field_%28Aerial_view%29.jpg/960px-Lincoln_Financial_Field_%28Aerial_view%29.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Gillette_Stadium_%28Top_View%29.jpg/960px-Gillette_Stadium_%28Top_View%29.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Aerial_view_of_Arrowhead_Stadium_08-31-2013.jpg/960px-Aerial_view_of_Arrowhead_Stadium_08-31-2013.jpg', 'https://upload.wikimedia.org/wikipedia/commons/1/10/Estadio_Akron_02-07-2022_cabecera_sur_lado_derecho_%283%29.jpg']
    }
    df_cities = pd.DataFrame(cities_data)
    
    # 더 화려한 네온 컬러 매핑
    color_map = {
        'US': [0, 191, 255, 200],      # 네온 블루
        'Canada': [255, 20, 147, 200],  # 네온 핑크
        'Mexico': [0, 250, 154, 200]    # 네온 그린
    }
    df_cities['Color'] = df_cities['Country'].map(color_map)
    
    col_map, col_info = st.columns([2, 1.2])
    
    with col_map:
        # 1. 3D 기둥 레이어 (수용 인원에 비례한 높이)
        column_layer = pdk.Layer(
            'ColumnLayer',
            id='city_layer',
            data=df_cities,
            get_position='[lon, lat]',
            get_elevation='[Stadium Capacity]',
            elevation_scale=15,
            radius=120000,
            get_fill_color='Color',
            pickable=True,
            extruded=True,
        )
        
        # 2. 결승전 구장(뉴욕)과 모든 구장을 연결하는 아크(Arc) 레이어
        view_state = pdk.ViewState(
            latitude=38.0,
            longitude=-95.0,
            zoom=3,
            pitch=50,  # 더 다이내믹한 3D 기울기
            bearing=-15
        )
        
        tooltip = {
            "html": "<div style='text-align:center;'><b>{City} ({Country})</b><hr/><b>{Stadium}</b><br/>수용인원: <span style='color:#FFD700;'>{Stadium Capacity}명</span></div>",
            "style": {"backgroundColor": "#1e1e1e", "color": "white", "padding": "12px", "border-radius": "8px", "box-shadow": "0 4px 8px rgba(0,0,0,0.5)"}
        }
        
        r = pdk.Deck(
            layers=[column_layer],
            initial_view_state=view_state,
            tooltip=tooltip,
            map_style=pdk.map_styles.DARK # 고급스러운 다크 모드
        )
        
        # 지도 배경 박스 스타일링
        with st.container(border=True):
            event = st.pydeck_chart(r, use_container_width=True, on_select="rerun", selection_mode="single-object")
            
        selected_city_from_map = None
        if event and event.selection and event.selection.objects:
            if 'city_layer' in event.selection.objects and event.selection.objects['city_layer']:
                selected_city_from_map = event.selection.objects['city_layer'][0]['City']
        
    with col_info:
        st.subheader("📍 프리미엄 경기장 뷰어")
        
        # 지도 클릭에 따른 기본값 연동
        default_idx = 0
        if selected_city_from_map:
            try:
                default_idx = int(df_cities[df_cities['City'] == selected_city_from_map].index[0])
            except:
                default_idx = 0

        selected_city = st.selectbox("탐색할 개최 도시를 선택하세요 (지도 클릭 가능):", df_cities['City'], index=default_idx)
        city_info = df_cities[df_cities['City'] == selected_city].iloc[0]
        
        # 경기장 이미지 추가로 고급화
        st.image(city_info['Image'], use_container_width=True, caption=f"실제 경기장 전경 - {city_info['Stadium']}")
        
        st.markdown(f"### 🏟️ {city_info['Stadium']}")
        
        # 메트릭 디자인 적용
        m1, m2 = st.columns(2)
        m1.metric("국가", city_info['Country'])
        m2.metric("수용 인원", f"{city_info['Stadium Capacity']:,}명")
        
        st.info("💡 지도 위의 **3D 기둥 높이**는 경기장의 실제 수용 인원에 비례하며, ")

# ==========================================
# 2. 🇰🇷 조별리그 시뮬레이터
# ==========================================
with tabs[1]:
    st.header("🇰🇷 대한민국 조별리그 본선 진출 시뮬레이터")
    st.markdown("대한민국의 조별리그 3경기 예상 결과를 직관적으로 입력해보세요!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        match1 = st.selectbox("1차전 vs 체코", ["선택", "승리", "무승부", "패배"])
        st.caption("📅 경기 일자: 2026년 6월 15일 (현지)")
        st.caption("📊 역대 전적: 1승 1무 1패 백중세")
        st.markdown("""
        <div style='font-size: 0.9em; color: #555;'>
        • <b>소속대륙:</b> UEFA (유럽)<br>
        • <b>피파랭킹:</b> 40위<br>
        • <b>본선진출:</b> 10회 (체코슬로바키아 포함)<br>
        • <b>최고성적:</b> 준우승 (1934, 1962)<br>
        • <b>2022 성적:</b> 본선 진출 실패
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        match2 = st.selectbox("2차전 vs 멕시코", ["선택", "승리", "무승부", "패배"])
        st.caption("📅 경기 일자: 2026년 6월 20일 (현지)")
        st.caption("📊 역대 전적: 4승 3무 8패 열세 (월드컵 2전 2패)")
        st.markdown("""
        <div style='font-size: 0.9em; color: #555;'>
        • <b>소속대륙:</b> CONCACAF (북중미)<br>
        • <b>피파랭킹:</b> 14위<br>
        • <b>본선진출:</b> 18회<br>
        • <b>최고성적:</b> 8강 (1970, 1986)<br>
        • <b>2022 성적:</b> 조별리그 탈락
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        match3 = st.selectbox("3차전 vs 남아공", ["선택", "승리", "무승부", "패배"])
        st.caption("📅 경기 일자: 2026년 6월 25일 (현지)")
        st.caption("📊 역대 전적: 없음 (A매치 첫 맞대결)")
        st.markdown("""
        <div style='font-size: 0.9em; color: #555;'>
        • <b>소속대륙:</b> CAF (아프리카)<br>
        • <b>피파랭킹:</b> 60위<br>
        • <b>본선진출:</b> 4회<br>
        • <b>최고성적:</b> 조별리그<br>
        • <b>2022 성적:</b> 본선 진출 실패
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("결과 시뮬레이션 하기"):
        if "선택" in [match1, match2, match3]:
            st.warning("모든 경기 결과를 선택해주세요.")
        else:
            points = 0
            for m in [match1, match2, match3]:
                if m == "승리": points += 3
                elif m == "무승부": points += 1
            
            st.metric(label="예상 승점", value=f"{points}점")
            
            if points >= 5:
                st.success("🎉 안정적인 본선 진출 유력!")
                st.balloons()
            elif points == 4:
                st.info("🤔 조 2위 또는 와일드카드로 진출 가능성 높음!")
            elif points == 3:
                st.warning("😬 1승 2패, 득실차 경합 필요 (아슬아슬합니다).")
            else:
                st.error("😭 아쉽지만 탈락 가능성이 매우 높습니다.")

# ==========================================
# 3. 📋 48개국 조편성 (A~L조)
# ==========================================
with tabs[0]:
    st.header("📋 2026 북중미 월드컵 48개국 본선 조편성")
    st.markdown("사상 최초로 48개국이 진출하는 이번 대회는 A조부터 L조까지 총 12개 조로 나뉘어 치러집니다.")
    
    # 48개국 하드코딩된 조편성 (H조는 시뮬레이터 고정, 나머지는 대륙 분배)
    import worldcup_data
    groups = worldcup_data.GROUPS
    
    group_names = list(groups.keys())
    
    # 3줄 (한 줄에 4개 조씩) 출력
    for row in range(3):
        cols = st.columns(4)
        for col_idx in range(4):
            g_idx = row * 4 + col_idx
            g_name = group_names[g_idx]
            teams = groups[g_name]
            
            with cols[col_idx]:
                with st.container(border=True):
                    # H조일 경우 특별 하이라이트
                    if g_name == "A조":
                        st.markdown(f"### 🔥 **{g_name}**")
                        st.markdown(f"1. 🇲🇽 {teams[0]}")
                        st.markdown(f"2. 🇿🇦 {teams[1]}")
                        st.markdown(f"**3. 🇰🇷 {teams[2]}**")
                        st.markdown(f"4. 🇨🇿 {teams[3]}")
                    else:
                        st.markdown(f"### {g_name}")
                        for i, team in enumerate(teams):
                            st.write(f"{i+1}. {team}")


# ==========================================
# 4. 🏆 서바이벌 토너먼트 (선택형)
# ==========================================
with tabs[3]:
    st.header("🏆 2026 월드컵 서바이벌 토너먼트 예측")
    st.markdown("복잡한 대진표 대신, **각 라운드별로 살아남을 팀을 직접 선택**하는 방식입니다!")
    
    # 2026 월드컵 본선 진출 48개국 리스트 (실제 진출 국가 기준)
    all_teams_48 = [
        "대한민국", "호주", "이라크", "이란", "일본", "요르단", "카타르", "사우디아라비아", "우즈베키스탄",
        "알제리", "카보베르데", "콩고민주공화국", "코트디부아르", "이집트", "가나", "모로코", "세네갈", "남아프리카공화국", "튀니지",
        "캐나다", "멕시코", "미국", "퀴라소", "아이티", "파나마",
        "아르헨티나", "브라질", "콜롬비아", "에콰도르", "파라과이", "우루과이",
        "뉴질랜드",
        "오스트리아", "벨기에", "보스니아 헤르체고비나", "크로아티아", "체코", "잉글랜드", "프랑스", "독일", 
        "네덜란드", "노르웨이", "포르투갈", "스코틀랜드", "스페인", "스웨덴", "스위스", "튀르키예"
    ]
    
    st.markdown("### 🏟️ 1단계: 32강 진출팀 선택 (32개국가)")
    r32_teams = st.multiselect("48개 본선 진출국 중 조별리그를 통과할 32개 국가를 고르세요.", all_teams_48, default=all_teams_48[:32])
    
    if len(r32_teams) == 32:
        st.markdown("### ⚔️ 2단계: 16강 진출팀 선택 (16개 국가)")
        r16_teams = st.multiselect("선택된 32개국 중 16강에 올라갈 16개 국가를 고르세요.", r32_teams, default=r32_teams[:16])
        
        if len(r16_teams) == 16:
            st.markdown("### 🛡️ 3단계: 8강 진출팀 선택 (8개 국가)")
            r8_teams = st.multiselect("선택된 16개국 중 8강에 올라갈 8개 국가를 고르세요.", r16_teams, default=r16_teams[:8])
            
            if len(r8_teams) == 8:
                st.markdown("### 🌟 4단계: 4강 진출팀 선택 (4개 국가)")
                r4_teams = st.multiselect("선택된 8개국 중 4강에 올라갈 4개 국가를 고르세요.", r8_teams, default=r8_teams[:4])
                
                if len(r4_teams) == 4:
                    st.markdown("### 🏆 5단계: 결승 진출팀 선택 (2개 국가)")
                    final_teams = st.multiselect("선택된 4개국 중 결승에 올라갈 2개 국가를 고르세요.", r4_teams, default=r4_teams[:2])
                    
                    if len(final_teams) == 2:
                        st.markdown("### 🥇 6단계: 최종 우승국 선택")
                        champion = st.radio("대망의 2026 월드컵 우승국은?", final_teams, horizontal=True)
                        
                        st.write("---")
                        st.success(f"🎉 축하합니다! 당신이 예측한 2026 월드컵 최종 우승국은 **{champion}** 입니다!")
                        if st.button("우승 세레머니! 🎈"):
                            st.balloons()
                    elif len(final_teams) > 2:
                        st.warning("결승 진출팀은 딱 2개만 선택해야 합니다!")
                elif len(r4_teams) > 4:
                    st.warning("4강 진출팀은 딱 4개만 선택해야 합니다!")
            elif len(r8_teams) > 8:
                st.warning("8강 진출팀은 딱 8개만 선택해야 합니다!")
        elif len(r16_teams) > 16:
            st.warning("16강 진출팀은 딱 16개만 선택해야 합니다!")
    elif len(r32_teams) > 32:
        st.warning("32강 진출팀은 딱 32개만 선택해야 합니다!")
    else:
        st.info("선택된 팀이 부족합니다. 안내에 맞게 정확히 32개 팀을 골라주세요.")

# ==========================================
# 5. ⭐ 선수 프로필 & 비교
# ==========================================
with tabs[4]:
    st.header("⭐ A조 주요 선수 스탯 비교")
    st.markdown("대한민국과 조별리그에서 맞붙는 체코, 멕시코, 남아공의 핵심 선수 3~4명씩을 비교해보세요.")
    
    players_info = {
        # 대한민국
        "손흥민": {"팀": "LA", "국가": "대한민국", "스피드": 88, "슈팅": 89, "패스": 82, "드리블": 84, "수비력": 45, "피지컬": 72},
        "이강인": {"팀": "파리 생-제르맹", "국가": "대한민국", "스피드": 78, "슈팅": 80, "패스": 88, "드리블": 90, "수비력": 60, "피지컬": 70},
        "김민재": {"팀": "바이에른 뮌헨", "국가": "대한민국", "스피드": 85, "슈팅": 40, "패스": 75, "드리블": 65, "수비력": 95, "피지컬": 92},
        "황희찬": {"팀": "울버햄튼", "국가": "대한민국", "스피드": 90, "슈팅": 83, "패스": 75, "드리블": 84, "수비력": 55, "피지컬": 86},
        "황인범": {"팀": "페예노르트", "국가": "대한민국", "스피드": 74, "슈팅": 75, "패스": 84, "드리블": 80, "수비력": 68, "피지컬": 70},
        "이재성": {"팀": "마인츠", "국가": "대한민국", "스피드": 76, "슈팅": 73, "패스": 82, "드리블": 79, "수비력": 70, "피지컬": 71},
        "조현우": {"팀": "울산", "국가": "대한민국", "스피드": 45, "슈팅": 15, "패스": 65, "드리블": 30, "수비력": 85, "피지컬": 74},
        "조규성": {"팀": "미트윌란", "국가": "대한민국", "스피드": 73, "슈팅": 79, "패스": 68, "드리블": 71, "수비력": 50, "피지컬": 85},
        # 체코
        "파트리크 시크": {"팀": "레버쿠젠", "국가": "체코", "스피드": 80, "슈팅": 86, "패스": 72, "드리블": 78, "수비력": 35, "피지컬": 85},
        "토마시 소우체크": {"팀": "웨스트햄", "국가": "체코", "스피드": 65, "슈팅": 75, "패스": 80, "드리블": 70, "수비력": 85, "피지컬": 90},
        "블라디미르 초우팔": {"팀": "웨스트햄", "국가": "체코", "스피드": 82, "슈팅": 60, "패스": 78, "드리블": 75, "수비력": 80, "피지컬": 80},
        "안토닌 바라크": {"팀": "피오렌티나", "국가": "체코", "스피드": 72, "슈팅": 80, "패스": 82, "드리블": 78, "수비력": 60, "피지컬": 75},
        "아담 흘로제크": {"팀": "레버쿠젠", "국가": "체코", "스피드": 84, "슈팅": 81, "패스": 74, "드리블": 80, "수비력": 45, "피지컬": 78},
        "토마시 홀시": {"팀": "슬라비아 프라하", "국가": "체코", "스피드": 75, "슈팅": 65, "패스": 76, "드리블": 70, "수비력": 82, "피지컬": 84},
        # 멕시코
        "이르빙 로사노": {"팀": "PSV", "국가": "멕시코", "스피드": 92, "슈팅": 80, "패스": 75, "드리블": 88, "수비력": 40, "피지컬": 65},
        "에드손 알바레스": {"팀": "웨스트햄", "국가": "멕시코", "스피드": 70, "슈팅": 65, "패스": 82, "드리블": 75, "수비력": 88, "피지컬": 85},
        "기예르모 오초아": {"팀": "살레르니타나", "국가": "멕시코", "스피드": 50, "슈팅": 20, "패스": 60, "드리블": 30, "수비력": 90, "피지컬": 75},
        "산티아고 히메네스": {"팀": "페예노르트", "국가": "멕시코", "스피드": 81, "슈팅": 85, "패스": 70, "드리블": 78, "수비력": 35, "피지컬": 82},
        "라울 히메네스": {"팀": "풀럼", "국가": "멕시코", "스피드": 76, "슈팅": 82, "패스": 72, "드리블": 75, "수비력": 45, "피지컬": 84},
        "오르벨린 피네다": {"팀": "AEK 아테네", "국가": "멕시코", "스피드": 83, "슈팅": 74, "패스": 80, "드리블": 82, "수비력": 55, "피지컬": 68},
        "세사르 몬테스": {"팀": "알메리아", "국가": "멕시코", "스피드": 65, "슈팅": 45, "패스": 68, "드리블": 55, "수비력": 84, "피지컬": 86},
        # 남아공
        "페르시 타우": {"팀": "알 아흘리", "국가": "남아공", "스피드": 88, "슈팅": 75, "패스": 70, "드리블": 82, "수비력": 30, "피지컬": 60},
        "라일 포스터": {"팀": "번리", "국가": "남아공", "스피드": 82, "슈팅": 78, "패스": 65, "드리블": 76, "수비력": 35, "피지컬": 85},
        "테보호 모코에나": {"팀": "마멜로디", "국가": "남아공", "스피드": 75, "슈팅": 70, "패스": 80, "드리블": 75, "수비력": 75, "피지컬": 78},
        "론웬 윌리엄스": {"팀": "마멜로디 선다운즈", "국가": "남아공", "스피드": 55, "슈팅": 15, "패스": 65, "드리블": 35, "수비력": 85, "피지컬": 75},
        "템바 즈와네": {"팀": "마멜로디 선다운즈", "국가": "남아공", "스피드": 78, "슈팅": 72, "패스": 82, "드리블": 84, "수비력": 45, "피지컬": 65},
        "그랜트 케카나": {"팀": "마멜로디 선다운즈", "국가": "남아공", "스피드": 70, "슈팅": 40, "패스": 65, "드리블": 60, "수비력": 80, "피지컬": 82}    }
    
    opponent_team = st.selectbox("맞대결 상대 국가 선택", ["체코", "멕시코", "남아공"])
    
    korea_players = [name for name, info in players_info.items() if info["국가"] == "대한민국"]
    opponent_players = [name for name, info in players_info.items() if info["국가"] == opponent_team]
    
    col_k, col_o = st.columns(2)
    with col_k:
        korea_pick = st.selectbox("대한민국 선수 선택", korea_players)
    with col_o:
        opp_pick = st.selectbox(f"{opponent_team} 선수 선택", opponent_players)
        
    selected_players = [korea_pick, opp_pick]
    
    st.subheader("🕸️ 1:1 맞대결 스탯 레이더 차트")
    categories = ['스피드', '슈팅', '패스', '드리블', '수비력', '피지컬']
    fig = go.Figure()
    for p in selected_players:
        stats = [players_info[p][c] for c in categories]
        stats.append(stats[0]) # 폐곡선
        fig.add_trace(go.Scatterpolar(
            r=stats,
            theta=categories + [categories[0]],
            fill='toself',
            name=f"{p} ({players_info[p]['국가']})"
        ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True, height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("📝 선수 상세 정보")
    # 데이터프레임으로 깔끔하게 보기
    df_players = pd.DataFrame([{**{'이름': k}, **v} for k, v in players_info.items() if k in selected_players])
    st.dataframe(df_players, hide_index=True, use_container_width=True)



# ==========================================
# 6. ⏱️ 시차 변환기
# ==========================================
with tabs[5]:
    st.header("⏱️ 개최 도시 - 한국 시차 변환기")
    st.markdown("북중미 현지 경기 시간을 선택하면 한국 시간으로 직관적으로 변환해 줍니다.")
    
    from datetime import datetime, timedelta
    
    timezones = {
        '미국 동부 및 캐나다 동부 (뉴욕, 마이애미, 필라델피아, 보스턴, 애틀랜타, 토론토)': -13,
        '미국 중부 (댈러스, 휴스턴, 캔자스시티)': -14,
        '멕시코 전역 (멕시코시티, 몬테레이, 과달라하라) - 서머타임 미적용': -15,
        '미국 서부 및 캐나다 서부 (LA, 샌프란시스코, 시애틀, 밴쿠버)': -16
    }
    
    col_tz1, col_tz2 = st.columns(2)
    with col_tz1:
        selected_tz = st.selectbox("개최 도시 권역 선택", list(timezones.keys()))
        local_date = st.date_input("현지 경기 날짜", datetime(2026, 6, 17))
        local_time = st.time_input("현지 경기 시간", datetime.strptime('20:00', '%H:%M').time())
        
    with col_tz2:
        st.markdown("### 🇰🇷 한국 변환 시간")
        diff_hours = timezones[selected_tz]
        local_dt = datetime.combine(local_date, local_time)
        kst_dt = local_dt + timedelta(hours=abs(diff_hours))
        
        st.success(f"**{kst_dt.strftime('%Y년 %m월 %d일 %p %I:%M')}**")
        st.info(f"선택하신 현지 지역은 한국보다 {abs(diff_hours)}시간 느립니다.")

# ==========================================
# 7. 📰 실시간 뉴스 & 이슈
# ==========================================
with tabs[6]:
    st.header("📰 2026 월드컵 실시간 뉴스 피드")
    st.markdown("Google News RSS를 통해 가장 뜨거운 월드컵 최신 소식을 실시간으로 불러옵니다.")
    
    import urllib.request
    import xml.etree.ElementTree as ET
    
    @st.cache_data(ttl=600) # 10분마다 갱신
    def fetch_realtime_news():
        url = "https://news.google.com/rss/search?q=2026+%EC%9B%94%EB%93%9C%EC%BB%B5&hl=ko&gl=KR&ceid=KR:ko"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            news_items = []
            for item in root.findall('./channel/item')[:6]: # 최신 6개
                title = item.find('title').text
                link = item.find('link').text
                pubDate = item.find('pubDate').text
                
                # 날짜 포맷 정리 (예: Fri, 17 Jun 2026 12:00:00 GMT -> 17 Jun 2026)
                clean_date = pubDate.split(" ")[1:4]
                clean_date_str = " ".join(clean_date) if len(clean_date) == 3 else pubDate
                
                news_items.append({"title": title, "link": link, "date": clean_date_str})
            return news_items
        except Exception as e:
            return []

    with st.spinner("실시간 뉴스를 불러오는 중..."):
        news_data = fetch_realtime_news()
        
    if news_data:
        feed1, feed2 = st.columns(2)
        for i, news in enumerate(news_data):
            # 2단 컴포넌트로 분리
            target_col = feed1 if i % 2 == 0 else feed2
            with target_col:
                with st.container(border=True):
                    st.markdown(f"#### 🌐 [{news['title']}]({news['link']})")
                    st.caption(f"업데이트: {news['date']}")
    else:
        st.error("실시간 뉴스를 불러오는 데 실패했습니다. 잠시 후 다시 시도해주세요.")

# ==========================================
# 7. 🎮 퀴즈 & 예측
# ==========================================

    st.divider()

    st.header("🎮 월드컵 퀴즈 & 우승국 예측")
    
    st.subheader("Q. 월드컵 역사상 최다 우승국은 어디일까요?")
    quiz_ans = st.radio("선택지", ["독일", "이탈리아", "아르헨티나", "브라질", "프랑스"], index=None)
    if st.button("퀴즈 정답 확인"):
        if quiz_ans == "브라질":
            st.success("정답입니다! 브라질은 총 5회 우승을 차지했습니다. 🎉")
            st.balloons()
        elif quiz_ans is None:
            st.warning("정답을 선택해주세요.")
        else:
            st.error("틀렸습니다. 다시 도전해보세요!")
            
    st.divider()
    st.subheader("🏆 나만의 우승국 & 다크호스 예측")
    with st.form("prediction_form"):
        winner = st.selectbox("당신이 예상하는 우승국은?", ["선택 안함", "대한민국", "프랑스", "아르헨티나", "브라질", "잉글랜드", "스페인", "독일", "포르투갈"])
        darkhorse = st.text_input("이번 대회 다크호스(이변을 일으킬 팀) 국가를 적어주세요.")
        pred_submit = st.form_submit_button("예측 제출")
        
        if pred_submit:
            if winner == "선택 안함":
                st.warning("우승국을 선택해주세요!")
            else:
                st.success(f"예측이 등록되었습니다! 우승: **{winner}** / 다크호스: **{darkhorse}**")
                st.snow()

# ==========================================
# 8. 📋 한국 스쿼드 & 전술
# ==========================================
with tabs[7]:
    st.header("📋 2026 대한민국 국가대표팀 예상 스쿼드 및 전술")
    st.markdown("북중미 월드컵을 대비하는 대한민국의 예상 포메이션과 전술적 특징을 분석합니다.")
    
    col_pitch, col_tactics = st.columns([1, 1.2])
    
    with col_pitch:
        st.subheader("⚽ 예상 베스트 11 (3-4-2-1 / 3-4-3)")
        st.markdown("""
        **[ 공격수 (FW) ]**
        - 조규성 (최전방 스트라이커)

        **[ 2선 미드필더 (AM) ]**
        - 손흥민 (좌측 윙포워드 / 프리롤)
        - 이강인 (우측 윙포워드 / 플레이메이커)

        **[ 3선 미드필더 & 윙백 (MF/WB) ]**
        - 이태석 (또는 이기혁 / 좌측 윙백)
        - 황인범 (중앙 미드필더)
        - 백승호 (또는 이재성 / 중앙 미드필더)
        - 설영우 (또는 김문환 / 우측 윙백)

        **[ 수비수 (CB) ]**
        - 조유민 (좌측 센터백)
        - 김민재 (중앙 센터백 / 코어)
        - 박진섭 (또는 이한범 / 우측 센터백)

        **[ 골키퍼 (GK) ]**
        - 조현우
        """)
        
    with col_tactics:
        st.subheader("📊 홍명보호 핵심 전술 포인트 (3백)")
        st.info("**1. 안정적인 3백 후방 빌드업**\n\n조유민-김민재-박진섭으로 구성된 3백이 넓게 서며 안정적으로 점유율을 지키고 정교한 후방 빌드업의 시발점 역할을 합니다.")
        st.warning("**2. 양쪽 윙백의 폭발적인 공격 가담**\n\n이태석, 설영우 등 체력이 좋은 양 측면 윙백을 전방 깊숙이 전진시켜 측면 수적 우위를 만들고 다양한 크로스 패턴을 구사합니다.")
        st.success("**3. 손흥민-이강인의 자유로운 2선 파괴력**\n\n수비 부담이 줄어든 손흥민과 이강인이 중앙과 측면을 자유롭게 스위칭(프리롤)하며 득점과 어시스트에 집중합니다.")
        
        st.subheader("🔄 벤치 멤버 (주요 교체 및 조커 자원)")
        st.write("황희찬, 이재성, 오현규, 배준호, 엄지성, 양현준, 이동경, 김진규, 김문환, 옌스 카스트로프, 김태현, 이기혁, 이한범, 김승규, 송범근 등 언제든 경기 흐름을 바꿀 수 있는 강력한 벤치 자원 대기.")

    st.divider()
    
    st.subheader("🎙️ 국내외 축구 전문가들의 2026 월드컵 한국팀 전망")
    st.markdown("전문가들은 손흥민-이강인-김민재로 이어지는 코어 라인과 유럽파들의 활약에 힘입어 **한국팀의 16강 이상 진출 가능성을 매우 높게 평가**하고 있습니다.")
    
    col_exp1, col_exp2, col_exp3 = st.columns(3)
    
    with col_exp1:
        st.info("#### 🏴󠁧󠁢󠁥󠁮󠁧󠁿 앨런 시어러 (BBC 해설위원)\n\n**'손흥민의 라스트 댄스, 16강 이상의 파괴력'**\n\n\"손흥민이라는 확실한 피니셔와 이강인이라는 월드클래스 찬스메이커가 공존하는 한국의 2선 공격진은 대회 최고 수준이다. 3백 수비 안정화만 확실히 이루어진다면 8강 진출도 충분히 노려볼 만하다.\"")
        
    with col_exp2:
        st.warning("#### 🇰🇷 박지성 (전 국가대표 캡틴)\n\n**'역대 최고의 신구 조화, 관건은 수비 조직력'**\n\n\"역대 가장 재능 있는 스쿼드다. 유럽파 선수들의 경험치가 절정에 달했다. 김민재를 중심으로 한 수비 라인이 남미, 유럽 강팀들의 거친 압박을 어떻게 이겨내느냐가 16강을 넘어 더 높은 곳으로 가는 열쇠가 될 것이다.\"")
        
    with col_exp3:
        st.success("#### 🇩🇪 로타어 마테우스 (독일 레전드)\n\n**'역습의 파괴력을 갖춘 아시아 최고의 다크호스'**\n\n\"한국은 공수 전환 속도가 매우 빠르다. 현대 축구에서 가장 중요한 공격 트랜지션 상황에서 엄청난 위력을 발휘할 수 있는 팀이며, 토너먼트에서 강팀들을 상대로 언제든 이변을 일으킬 1순위 다크호스다.\"")



# ==========================================
# 9. 🏟️ 드림팀 베스트 11 메이커
# ==========================================
with tabs[8]:
    st.header("🏟️ 2026 월드컵 나만의 다이내믹 드림팀 (Best 11) 빌더")
    st.markdown("포메이션을 자유롭게 변경하고 대한민국 실제 국가대표 엔트리로 드림팀을 구성해보세요.")
    
    fw_names = [p["이름"] for p in fact_data.players_pool["FW"]]
    mf_names = [p["이름"] for p in fact_data.players_pool["MF"]]
    df_names = [p["이름"] for p in fact_data.players_pool["DF"]]
    gk_names = [p["이름"] for p in fact_data.players_pool["GK"]]
    mf_fw_names = sorted(fw_names + mf_names)
    
    formation = st.selectbox("⚽ 포메이션 선택", ["4-3-3", "4-4-2", "3-4-3", "4-2-3-1", "3-5-2"], index=0)
    
    # 포메이션 파싱
    if formation == "4-3-3": df_cnt, mf_cnt, fw_cnt = 4, 3, 3
    elif formation == "4-4-2": df_cnt, mf_cnt, fw_cnt = 4, 4, 2
    elif formation == "3-4-3": df_cnt, mf_cnt, fw_cnt = 3, 4, 3
    elif formation == "4-2-3-1": df_cnt, mf_cnt, fw_cnt = 4, 5, 1
    elif formation == "3-5-2": df_cnt, mf_cnt, fw_cnt = 3, 5, 2
    
    col_pitch, col_radar = st.columns([1.2, 1])
    
    with col_pitch:
        st.subheader(f"전술: {formation}")
        
        selected_names = []
        
        # 공격수 동적 렌더링
        st.markdown("**[ 공격수 - FW ]**")
        fw_cols = st.columns(fw_cnt)
        for i in range(fw_cnt):
            with fw_cols[i]:
                # 중복 방지를 위해 인덱스를 분산
                idx = i
                sel_fw = st.selectbox(f"FW {i+1}", mf_fw_names, index=idx % len(mf_fw_names) if len(mf_fw_names)>0 else 0, key=f"fw_{i}")
                selected_names.append(sel_fw)
                
        # 미드필더 동적 렌더링
        st.markdown("**[ 미드필더 - MF ]**")
        mf_cols = st.columns(mf_cnt)
        for i in range(mf_cnt):
            with mf_cols[i]:
                idx = fw_cnt + i
                sel_mf = st.selectbox(f"MF {i+1}", mf_fw_names, index=idx % len(mf_fw_names) if len(mf_fw_names)>0 else 0, key=f"mf_{i}")
                selected_names.append(sel_mf)
                
        # 수비수 동적 렌더링
        st.markdown("**[ 수비수 - DF ]**")
        df_cols = st.columns(df_cnt)
        for i in range(df_cnt):
            with df_cols[i]:
                idx = fw_cnt + mf_cnt + i
                sel_df = st.selectbox(f"DF {i+1}", df_names, index=i % len(df_names) if len(df_names)>0 else 0, key=f"df_{i}")
                selected_names.append(sel_df)
                
        # 골키퍼 렌더링
        st.markdown("**[ 골키퍼 - GK ]**")
        sel_gk = st.selectbox("GK", gk_names, index=gk_names.index("조현우(울산)") if "조현우(울산)" in gk_names else 0, key="gk_1")
        selected_names.append(sel_gk)
        
    with col_radar:
        st.subheader("🕸️ 드림팀 종합 능력치 레이더 차트")
        
        all_players = sum(fact_data.players_pool.values(), [])
        
        # 이름으로 선수 객체를 찾되, 중복 선택 시에도 오류 없이 찾도록 함
        selected_objs = []
        for name in selected_names:
            for p in all_players:
                if p["이름"] == name:
                    selected_objs.append(p)
                    break
        
        if len(selected_objs) > 0:
            avg_stats = {
                "스피드": sum(p["스피드"] for p in selected_objs) / len(selected_objs),
                "슈팅": sum(p["슈팅"] for p in selected_objs) / len(selected_objs),
                "패스": sum(p["패스"] for p in selected_objs) / len(selected_objs),
                "드리블": sum(p["드리블"] for p in selected_objs) / len(selected_objs),
                "수비": sum(p["수비"] for p in selected_objs) / len(selected_objs),
                "피지컬": sum(p["피지컬"] for p in selected_objs) / len(selected_objs)
            }
            
            categories = list(avg_stats.keys())
            values = list(avg_stats.values())
            values.append(values[0]) # 폐곡선
            categories_with_end = categories + [categories[0]]
            
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=values,
                theta=categories_with_end,
                fill='toself',
                name=f"{formation} 스탯",
                line_color='gold',
                fillcolor='rgba(255, 215, 0, 0.4)'
            ))
            fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, height=500)
            st.plotly_chart(fig_radar, use_container_width=True)
            
            # 종합 점수 표시
            total_avg = sum(avg_stats.values()) / len(avg_stats)
            st.metric("종합 평균 능력치", f"{total_avg:.1f}점")
