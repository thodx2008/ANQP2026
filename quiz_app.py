import streamlit as st
import random

# --- Cấu hình ---
questions = {
    1: [
        # --- Trắc nghiệm khách quan (20 câu) ---
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
        # Các câu hỏi khác sẽ được thêm vào tương tự
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
    options = q['options']
    selected_option = st.radio("Chọn đáp án", options=options, index=-1, key=f"q{st.session_state['current_question']}")
    st.session_state['answers'].append(selected_option)

# Chức năng "Bắt đầu thi"
if st.button('Start Quiz'):
    display_question(questions[1][st.session_state['current_question']])

# Điều hướng qua các câu hỏi
if st.button('Next Question'):
    if st.session_state['current_question'] < len(questions[1]) - 1:
        st.session_state['current_question'] += 1
        display_question(questions[1][st.session_state['current_question']])
    else:
        st.write("Quiz Completed!")

# Hiển thị tiến độ
st.write(f"Câu {st.session_state['current_question'] + 1} / {len(questions[1])}")
