
import streamlit as st

# --- Cấu hình ---
questions = {
    1: [
        # --- DẠNG 1: TRẮC NGHIỆM KHÁCH QUAN ---
        {
            'type': 'mc', 
            'question': 'Đường lối của Đảng Cộng sản Việt Nam về bảo vệ Tổ quốc xã hội chủ nghĩa là:',
            'options': [
                'Những định hướng chiến lược nhằm đưa ra mục tiêu, phương châm, phương thức, sức mạnh, lực lượng để bảo vệ Tổ quốc',
                'Những định hướng chiến lược trong xác định mục tiêu, đề ra quan điểm, phương châm, phương thức, sức mạnh, lực lượng để bảo vệ Tổ quốc',
                'Những định hướng, xác định phương châm, phương thức, sức mạnh, lực lượng để bảo vệ Tổ quốc',
                'Xác định mục tiêu, đề ra quan điểm, phương thức, sức mạnh, lực lượng để bảo vệ Tổ quốc'
            ],
            'answer': 1  # B
        },
        {
            'type': 'mc',
            'question': 'Bảo vệ Tổ quốc xã hội chủ nghĩa là:',
            'options': [
                'Bảo vệ toàn diện cả mặt lịch sử - tự nhiên cùng mặt chính trị - xã hội của Tổ quốc',
                'Bảo vệ thành quả của cách mạng, giữ vững độc lập, chủ quyền, toàn vẹn lãnh thổ của Tổ quốc',
                'Bảo vệ lãnh thổ, cộng đồng dân cư và thể chế chính trị xã hội',
                'Bảo vệ Đảng, bảo vệ Nhà nước, bảo vệ nhân dân và toàn vẹn lãnh thổ của Tổ quốc'
            ],
            'answer': 0  # A
        },
        {
            'type': 'mc',
            'question': 'Học thuyết Mác - Lênin về bảo vệ Tổ quốc, xuất phát:',
            'options': [
                'Yêu cầu xây dựng chủ nghĩa xã hội và bảo vệ Tổ quốc xã hội chủ nghĩa hiện nay',
                'Từ quy luật xây dựng chủ nghĩa xã hội phải đi đôi với bảo vệ Tổ quốc xã hội chủ nghĩa',
                'Từ mục đích xây dựng chủ nghĩa xã hội đi đôi với bảo vệ Tổ quốc xã hội chủ nghĩa',
                'Từ sự cần thiết trong xây dựng chủ nghĩa xã hội và bảo vệ Tổ quốc xã hội chủ nghĩa'
            ],
            'answer': 1  # B
        },
        {
            'type': 'mc',
            'question': 'Học thuyết Mác - Lênin, tư tưởng Hồ Chí Minh về bảo vệ Tổ quốc xã hội chủ nghĩa là:',
            'options': [
                'Tổng hợp các quan điểm về bảo vệ Tổ quốc xã hội chủ nghĩa',
                'Tổng họp các tư tưởng về bảo vệ Tổ quốc xã hội chủ nghĩa',
                'Bộ phận hợp thành lý luận cách mạng xã hội chủ nghĩa',
                'Hệ thống các quan điểm về tính tất yếu, nhiệm vụ và nội dung bảo vệ Tổ quốc xã hội chủ nghĩa'
            ],
            'answer': 2  # C
        },
        {
            'type': 'mc',
            'question': 'Đường lối của Đảng Cộng sản Việt Nam về bảo vệ Tổ quốc trong văn kiện đại hội lần thứ XIII của Đảng xác định:',
            'options': [
                'Phát huy có hiệu quả sức mạnh tổng hợp, tranh thủ tối đa sự đồng tình, ủng hộ của cộng đồng quốc tế',
                'Phát huy sức mạnh của cả hệ thống chính trị tranh thủ tối đa sự đồng tình, ủng hộ của cộng đồng quốc tế',
                'Huy động sức mạnh tổng hợp của cả dân tộc kết hợp với sức mạnh thời đại và sự đồng tình, ủng hộ của cộng đồng quốc tế',
                'Phát huy cao nhất sức mạnh tổng hợp của toàn dân tộc, của cả hệ thống chính trị kết hợp với sức mạnh thời đại, tranh thủ tối đa sự đồng tình, ủng hộ của cộng đồng quốc tế'
            ],
            'answer': 3  # D
        },
        {
            'type': 'mc',
            'question': 'Đường lối của Đảng Cộng sản Việt Nam về bảo vệ Tổ quốc trong văn kiện đại hội lần thứ XIII của Đảng xác định:',
            'options': [
                'Giữ độc lập, chủ quyền, thống nhất, toàn vẹn lãnh thổ của Tổ quốc',
                'Bảo vệ vững chắc độc lập, chủ quyền, toàn vẹn lãnh thổ của Tổ quốc, bảo vệ Đảng, Nhà nước, nhân dân',
                'Bảo vệ vững chắc độc lập, chủ quyền, thống nhất, toàn vẹn lãnh thổ của Tổ quốc, bảo vệ Đảng, Nhà nước, nhân dân, chế độ xã hội chủ nghĩa, nền văn hoá và lợi ích quốc gia - dân tộc',
                'Bảo vệ vững chắc chủ quyền biển đảo của Tổ quốc, bảo vệ Đảng, Nhà nước, nhân dân, chế độ xã hội chủ nghĩa, nền văn hoá và lợi ích quốc gia dân tộc'
            ],
            'answer': 2  # C
        },
        # Các câu hỏi tiếp theo tương tự...
    ]
}

# --- Giao diện Streamlit ---
st.title('Hệ thống ôn thi: Quốc phòng An ninh')
st.subheader('Lớp K76.A05 - XmanLC')
st.markdown('### Thời gian: 45 phút | Số lượng: 45 câu')

# Khởi tạo biến theo dõi tiến trình và câu trả lời
if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 0
    st.session_state['answers'] = []

# Hàm hiển thị câu hỏi và các lựa chọn
def display_question(q):
    st.markdown(f"**{q['question']}**")
    for idx, option in enumerate(q['options']):
        if st.radio(f"Option {idx + 1}", options=[option], index=-1, key=f"q{st.session_state['current_question']}_option{idx}"):
            st.session_state['answers'].append(idx)

# --- Logic Quiz ---
if st.button('Start Quiz'):
    display_question(questions[1][st.session_state['current_question']])

if st.button('Next Question'):
    if st.session_state['current_question'] < len(questions[1]) - 1:
        st.session_state['current_question'] += 1
        display_question(questions[1][st.session_state['current_question']])
    else:
        st.write("Quiz Completed!")
