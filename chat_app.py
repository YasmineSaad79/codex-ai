import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="CodeX AI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: #ffffff;
    }
    
    .main .block-container {
        max-width: 100rem;
        padding: 0;
        padding-top: 3rem;
        padding-bottom: 8rem;
    }
    
    [data-testid="stSidebar"] {
        background: #f9f9f9;
        border-right: 1px solid #e5e5e5;
        padding: 0.75rem;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding: 0;
    }
    
    .stButton button {
        background: transparent !important;
        color: #202020 !important;
        border: 1px solid #d1d1d1 !important;
        border-radius: 0.5rem !important;
        padding: 0.5rem 0.75rem !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        width: 100% !important;
        transition: all 0.15s ease !important;
        margin: 0.125rem auto !important;
        text-align: center !important;
        display: block !important;
    }
    
    .stButton button:hover {
        background: #ececec !important;
        border-color: #b4b4b4 !important;
    }
    
    .stChatMessage {
        background: transparent !important;
        border: none !important;
        padding: 1.5rem 0 !important;
        margin: 0 !important;
    }
    
    .stChatMessage[data-testid*="user"] {
        background: #f7f7f8 !important;
        margin-left: -50vw !important;
        margin-right: -50vw !important;
        padding-left: 50vw !important;
        padding-right: 50vw !important;
    }
    
    [data-testid="stChatMessageContent"] {
        color: #202020 !important;
        font-size: 1rem !important;
        line-height: 1.75 !important;
        max-width: 100rem !important;
        margin: 0 auto !important;
    }
    
    .stChatInput {
        position: fixed !important;
        bottom: 0 !important;
        left: 260px !important;
        right: 0 !important;
        background: #ffffff !important;
        padding: 1rem 4rem !important;
        border-top: 1px solid #e5e5e5 !important;
        z-index: 1000 !important;
    }
    
    .stChatInput > div {
        max-width: none !important;
        margin: 0 !important;
    }
    
    .stChatInput textarea {
        background: #ffffff !important;
        border: 1px solid #d1d1d1 !important;
        border-radius: 1.5rem !important;
        color: #202020 !important;
        padding: 0.875rem 1rem !important;
        font-size: 1rem !important;
        transition: all 0.15s ease !important;
        box-shadow: 0 0 10px rgba(0,0,0,0.05) !important;
    }
    
    .stChatInput textarea:focus {
        border-color: #10a37f !important;
        background: #ffffff !important;
        outline: none !important;
        box-shadow: 0 0 0 3px rgba(16,163,127,0.1) !important;
    }
    
    .stSelectbox {
        margin-bottom: 0.25rem;
    }
    
    .stSelectbox label {
        font-size: 0.75rem !important;
        color: #6e6e80 !important;
        font-weight: 500 !important;
        margin-bottom: 0.25rem !important;
    }
    
    .stSelectbox > div > div {
        background: #ffffff !important;
        border: 1px solid #d1d1d1 !important;
        border-radius: 0.5rem !important;
        color: #202020 !important;
        font-size: 0.875rem !important;
        min-height: 2.5rem !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #b4b4b4 !important;
        background: #f5f5f5 !important;
        cursor: pointer !important;
    }
    
    .stSelectbox svg {
        cursor: pointer !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        cursor: pointer !important;
    }
    
    h1, h2, h3 {
        display: none !important;
    }
    
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    [data-testid="stToolbar"] {
        display: none !important;
    }
    
    #MainMenu {
        display: none !important;
    }
    
    header {
        display: none !important;
    }
    
    footer {
        display: none !important;
    }
    
    .empty-state {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh;
        text-align: center;
    }
    
    .empty-state-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .empty-state-title {
        color: #202020;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .empty-state-subtitle {
        color: #6e6e80;
        font-size: 1rem;
        text-align: center;
    }
    
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: transparent;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #d1d1d1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #b4b4b4;
    }
    
    .sidebar-divider {
        height: 1px;
        background: #e5e5e5;
        margin: 0.5rem 0;
    }
    
    .sidebar-section-title {
        color: #6e6e80;
        font-size: 0.6875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        padding: 0.25rem 0.5rem;
        margin: 0.25rem 0;
    }
    
    div[data-testid="column"] {
        padding: 0 !important;
    }
    
    div[data-testid="column"]:first-child {
        padding-right: 0.25rem !important;
    }
    
    div[data-testid="column"]:last-child {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding-left: 0 !important;
    }
    
    div[data-testid="column"]:last-child button {
        margin: 0 auto !important;
        width: auto !important;
        min-width: 2.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversations" not in st.session_state:
    st.session_state.conversations = {}

if "current_conversation_id" not in st.session_state:
    st.session_state.current_conversation_id = None

if "conversation_counter" not in st.session_state:
    st.session_state.conversation_counter = 0

if "language" not in st.session_state:
    st.session_state.language = "العربية"

def create_new_conversation():
    st.session_state.conversation_counter += 1
    conv_id = f"chat_{st.session_state.conversation_counter}"
    st.session_state.conversations[conv_id] = {
        "messages": [],
        "title": "New Chat" if st.session_state.language == "English" else "محادثة جديدة",
        "timestamp": datetime.now()
    }
    st.session_state.current_conversation_id = conv_id
    st.session_state.messages = []

def load_conversation(conv_id):
    st.session_state.current_conversation_id = conv_id
    st.session_state.messages = st.session_state.conversations[conv_id]["messages"]

def save_current_conversation():
    if st.session_state.current_conversation_id:
        st.session_state.conversations[st.session_state.current_conversation_id]["messages"] = st.session_state.messages
        
def delete_conversation(conv_id):
    if conv_id in st.session_state.conversations:
        del st.session_state.conversations[conv_id]
        if st.session_state.current_conversation_id == conv_id:
            st.session_state.current_conversation_id = None
            st.session_state.messages = []

def generate_response(user_input: str, lang: str) -> str:
    user_input_lower = user_input.lower()
    
    if lang == "العربية":
        if any(word in user_input_lower for word in ["مرحبا", "السلام", "أهلا", "هلا", "هاي", "صباح", "مساء"]):
            return "مرحباً بك، أنا CodeX AI مساعدك الذكي في عالم البرمجة والتطوير. كيف يمكنني مساعدتك اليوم ؟"        
        elif any(word in user_input_lower for word in ["من أنت", "ما اسمك", "تعريف", "عرف نفسك", "من انت", "شو اسمك"]):
            return "أنا **CodeX AI** 💻، مساعد ذكي متخصص في:\n\n• البرمجة والتطوير\n• حل المشاكل التقنية\n• تعلم لغات البرمجة\n• الاستشارات التقنية\n\nأنا هنا لمساعدتك في رحلتك البرمجية!"
        
        elif "python" in user_input_lower or "بايثون" in user_input_lower or "بايثن" in user_input_lower:
            return "**بايثون** 🐍 لغة رائعة!\n\nمميزاتها:\n✅ سهلة التعلم للمبتدئين\n✅ قوية للمحترفين\n✅ تستخدم في الذكاء الاصطناعي\n✅ تحليل البيانات والويب\n\nهل تريد:\n• البدء بتعلم بايثون؟\n• حل مشكلة معينة؟\n• أمثلة على الأكواد؟"
        
        elif "java" in user_input_lower or "جافا" in user_input_lower:
            return "**جافا** ☕ لغة قوية ومستقرة!\n\nتستخدم في:\n✅ تطبيقات الأندرويد\n✅ الأنظمة المؤسسية الكبيرة\n✅ تطبيقات الويب\n✅ الألعاب\n\nهل تحتاج مساعدة في جافا؟"
        
        elif "javascript" in user_input_lower or "جافاسكريبت" in user_input_lower or " js " in user_input_lower:
            return "**جافاسكريبت** ⚡ لغة الويب الأولى!\n\nتستخدم في:\n✅ تطوير المواقع التفاعلية\n✅ تطبيقات الموبايل (رياكت نيتيف)\n✅ تطبيقات سطح المكتب (إلكترون)\n✅ الباك إند (نود جي إس)\n\nما الذي تريد تعلمه في جافاسكريبت؟"
        
        elif any(word in user_input_lower for word in ["برمجة", "تعلم", "كيف ابدأ", "كيف أبدأ", "مبتدئ", "ابدا", "ابدأ"]):
            return "رائع! تريد البدء بالبرمجة! 🚀\n\n**خطوات البداية:**\n\n1️⃣ **اختر لغة:** بايثون (الأسهل) أو جافاسكريبت (للويب)\n2️⃣ **تعلم الأساسيات:** المتغيرات، الشروط، الحلقات\n3️⃣ **مارس يومياً:** اكتب كود كل يوم\n4️⃣ **اصنع مشاريع:** طبق ما تعلمته\n\nأي لغة تفضل؟"
        
        elif any(word in user_input_lower for word in ["مساعدة", "ساعدني", "محتاج", "أريد", "بدي", "عايز", "ممكن"]):
            return "بالتأكيد! يمكنني مساعدتك في:\n\n✅ **تعلم البرمجة** من الصفر\n✅ **حل الأخطاء** في الكود\n✅ **شرح المفاهيم** البرمجية\n✅ **اقتراح أفضل الممارسات**\n✅ **مساعدة في المشاريع**\n\nما الذي تحتاج مساعدة فيه بالتحديد؟"
        
        elif any(word in user_input_lower for word in ["خطأ", "error", "مشكلة", "ما يشتغل", "ما اشتغل", "عطل"]):
            return "لا تقلق! الأخطاء جزء من البرمجة 🐛\n\n**لحل المشكلة:**\n1. اقرأ رسالة الخطأ بعناية\n2. ابحث عن رقم السطر\n3. تحقق من الأقواس والفواصل\n4. جرب طباعة القيم للتأكد\n\nأخبرني عن الخطأ وسأساعدك!"
        
        elif any(word in user_input_lower for word in ["موقع", "ويب", "website", "web", "صفحة"]):
            return "تريد تطوير موقع؟ ممتاز! 🌐\n\n**تحتاج:**\n• **إتش تي إم إل** - الهيكل\n• **سي إس إس** - التصميم\n• **جافاسكريبت** - التفاعل\n\n**أطر عمل شهيرة:**\n• رياكت ⚛️\n• فيو جي إس 💚\n• أنجولار 🅰️\n\nهل تريد البدء بالأساسيات أم الأطر؟"
        
        elif any(word in user_input_lower for word in ["ذكاء اصطناعي", "ai", "machine learning", "تعلم آلي", "ذكاء"]):
            return "**الذكاء الاصطناعي** 🤖 مجال المستقبل!\n\n**لتعلم الذكاء الاصطناعي تحتاج:**\n1. بايثون (اللغة الأساسية)\n2. الرياضيات (جبر خطي، إحصاء)\n3. مكتبات: تنسرفلو، باي تورش\n4. فهم الخوارزميات\n\nهل تريد البدء ببايثون أولاً؟"
        
        elif any(word in user_input_lower for word in ["شكرا", "شكراً", "ممتاز", "رائع", "جميل", "تمام", "حلو", "كويس"]):
            return "العفو! 😊 سعيد جداً بمساعدتك.\n\nلا تتردد في سؤالي عن أي شيء آخر!\n\n💡 **نصيحة:** البرمجة تحتاج ممارسة يومية، استمر!"
        
        else:
            return "شكراً لسؤالك! 🤔\n\nيمكنني مساعدتك في:\n• **تعلم البرمجة** (Python, Java, JavaScript)\n• **حل المشاكل التقنية**\n• **شرح المفاهيم البرمجية**\n• **نصائح للمبتدئين**\n\nجرب أن تسألني:\n- \"كيف أبدأ بالبرمجة؟\"\n- \"ساعدني في تعلم Python\"\n- \"ما هي أفضل لغة برمجة؟\""
    
    else:
        if any(word in user_input_lower for word in ["hello", "hi", "hey", "greetings", "sup", "good morning", "good evening"]):
            return "Hello! 👋 I'm CodeX AI, your intelligent coding assistant. How can I help you today?"
        
        elif any(word in user_input_lower for word in ["who are you", "what is your name", "introduce", "about you", "what's your name"]):
            return "I'm **CodeX AI** 💻, an intelligent assistant specialized in:\n\n• Programming & Development\n• Technical Problem Solving\n• Learning Programming Languages\n• Technical Consulting\n\nI'm here to help you on your coding journey!"
        
        elif "python" in user_input_lower:
            return "**Python** 🐍 is an amazing language!\n\nBenefits:\n✅ Easy for beginners\n✅ Powerful for experts\n✅ Used in AI & Machine Learning\n✅ Data analysis & web development\n\nWould you like to:\n• Start learning Python?\n• Solve a specific problem?\n• See code examples?"
        
        elif "java" in user_input_lower and "javascript" not in user_input_lower:
            return "**Java** ☕ is a powerful and stable language!\n\nUsed for:\n✅ Android apps\n✅ Enterprise systems\n✅ Web applications\n✅ Games\n\nDo you need help with Java?"
        
        elif "javascript" in user_input_lower or " js " in user_input_lower:
            return "**JavaScript** ⚡ is the language of the web!\n\nUsed for:\n✅ Interactive websites\n✅ Mobile apps (React Native)\n✅ Desktop apps (Electron)\n✅ Backend (Node.js)\n\nWhat would you like to learn in JavaScript?"
        
        elif any(word in user_input_lower for word in ["learn", "start", "begin", "beginner", "how to", "getting started"]):
            return "Great! You want to start coding! 🚀\n\n**Steps to begin:**\n\n1️⃣ **Choose a language:** Python (easiest) or JavaScript (for web)\n2️⃣ **Learn basics:** Variables, conditions, loops\n3️⃣ **Practice daily:** Write code every day\n4️⃣ **Build projects:** Apply what you learn\n\nWhich language interests you?"
        
        elif any(word in user_input_lower for word in ["help", "assist", "need", "want", "can you", "could you"]):
            return "Of course! I can help you with:\n\n✅ **Learning to code** from scratch\n✅ **Debugging errors** in your code\n✅ **Explaining concepts**\n✅ **Best practices**\n✅ **Project assistance**\n\nWhat specifically do you need help with?"
        
        elif any(word in user_input_lower for word in ["error", "bug", "problem", "not working", "doesn't work", "issue"]):
            return "Don't worry! Errors are part of coding 🐛\n\n**To solve the problem:**\n1. Read the error message carefully\n2. Find the line number\n3. Check brackets and commas\n4. Try printing values to debug\n\nTell me about the error and I'll help!"
        
        elif any(word in user_input_lower for word in ["website", "web", "site", "webpage"]):
            return "Want to build a website? Excellent! 🌐\n\n**You need:**\n• **HTML** - Structure\n• **CSS** - Styling\n• **JavaScript** - Interactivity\n\n**Popular frameworks:**\n• React ⚛️\n• Vue.js 💚\n• Angular 🅰️\n\nStart with basics or frameworks?"
        
        elif any(word in user_input_lower for word in ["ai", "artificial intelligence", "machine learning", "ml"]):
            return "**Artificial Intelligence** 🤖 is the future!\n\n**To learn AI you need:**\n1. Python (main language)\n2. Math (linear algebra, statistics)\n3. Libraries: TensorFlow, PyTorch\n4. Understanding algorithms\n\nWant to start with Python first?"
        
        elif any(word in user_input_lower for word in ["thank", "thanks", "great", "awesome", "perfect", "good", "nice"]):
            return "You're welcome! 😊 Happy to help.\n\nFeel free to ask me anything else!\n\n💡 **Tip:** Coding requires daily practice, keep going!"
        
        else:
            return "Thanks for your question! 🤔\n\nI can help you with:\n• **Learning to code** (Python, Java, JavaScript)\n• **Solving technical problems**\n• **Explaining programming concepts**\n• **Tips for beginners**\n\nTry asking me:\n- \"How do I start coding?\"\n- \"Help me learn Python\"\n- \"What's the best programming language?\""

with st.sidebar:
    language = st.selectbox(
        "Language",
        ["العربية", "English"],
        key="language_selector",
        label_visibility="collapsed"
    )
    st.session_state.language = language
    
    settings_title = "الإعدادات" if language == "العربية" else "Settings"
    text_align = "right" if language == "العربية" else "left"
    direction = "rtl" if language == "العربية" else "ltr"
    st.markdown(f'<div style="color: #6e6e80; font-size: 1.5rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; padding: 0 0.5rem; margin: -8rem 0 0.5rem 0; text-align: {text_align}; direction: {direction};">{settings_title}</div>', unsafe_allow_html=True)
    
    if st.button("✏️ New Chat", key="new_chat_btn", use_container_width=True):
        create_new_conversation()
        st.rerun()
    
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    
    if st.session_state.conversations:
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-section-title">Recent Chats</div>', unsafe_allow_html=True)
        
        for conv_id, conv_data in reversed(list(st.session_state.conversations.items())):
            is_current = conv_id == st.session_state.current_conversation_id
            
            col1, col2 = st.columns([5, 1])
            
            with col1:
                if st.button(
                    f"💬 {conv_data['title']}", 
                    key=f"conv_{conv_id}",
                    use_container_width=True
                ):
                    load_conversation(conv_id)
                    st.rerun()
            
            with col2:
                if st.button("🗑️", key=f"del_{conv_id}"):
                    delete_conversation(conv_id)
                    st.rerun()

if len(st.session_state.messages) == 0:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-state-icon">💻</div>
        <div class="empty-state-title">CodeX AI</div>
        <div class="empty-state-subtitle">How can I help you today?</div>
    </div>
    """, unsafe_allow_html=True)
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Message CodeX AI..." if language == "English" else "أرسل رسالة إلى CodeX AI..."):
    if not st.session_state.current_conversation_id:
        create_new_conversation()
    
    user_message = {
        "role": "user",
        "content": prompt
    }
    st.session_state.messages.append(user_message)
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = generate_response(prompt, language)
        st.markdown(response)
    
    assistant_message = {
        "role": "assistant",
        "content": response
    }
    st.session_state.messages.append(assistant_message)
    
    save_current_conversation()
    
    if len(st.session_state.messages) == 2:
        first_message = st.session_state.messages[0]["content"][:30]
        st.session_state.conversations[st.session_state.current_conversation_id]["title"] = first_message
        st.rerun()
