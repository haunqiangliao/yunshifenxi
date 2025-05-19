import streamlit as st
from streamlit_lottie import st_lottie
import requests
import random

# 配置页面
st.set_page_config(
    page_title="🌟 多维运势分析站",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------------------------
# 动画加载函数
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 加载不同运势对应的动画
lottie_fortune = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_8oahuefx.json")  # 好运动画
lottie_warning = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_8x8mxjfi.json")  # 提醒动画

# ------------------------------
# 数据库扩展
constellations = {
    "白羊座": {
        "运势": "近期可能会有意外惊喜，适合主动出击，展现个人魅力。",
        "lucky": "幸运色: 红色 | 幸运数字: 5",
        "tips": "宜: 运动健身 | 忌: 久坐不动"
    },
    "金牛座": {
        "运势": "财运稳定增长，适合进行长期投资规划，但需注意人际关系。",
        "lucky": "幸运色: 绿色 | 幸运数字: 6",
        "tips": "宜: 理财规划 | 忌: 冲动消费"
    },
    # 其他星座数据...
}

mbti_types = {
    "ISTJ": {
        "运势": "适合处理复杂任务，工作效率高，但可能会因过于固执错过新机会。",
        "lucky": "幸运色: 蓝色 | 幸运数字: 3",
        "tips": "宜: 按计划执行 | 忌: 频繁变动"
    },
    # 其他MBTI类型数据...
}

age_fortunes = {
    "少年": {
        "运势": "学习方面会有新的突破，可能会遇到良师益友。",
        "lucky": "幸运色: 橙色 | 幸运数字: 9",
        "tips": "宜: 参加社团 | 忌: 闭门造车"
    },
    # 其他年龄组数据...
}

# ------------------------------
# 主程序
def main():
    st.title("🌟 多维运势分析站 🌟")
    st.write("✨ 结合星座、MBTI、年龄的深度运势解析")
    
    # 侧边栏装饰
    with st.sidebar:
        st_lottie(lottie_fortune, height=150, key="sidebar-animation")
        st.write("---")
        st.write("made with ❤️ by Streamlit")
    
    # 输入表单
    with st.form("analysis_form", clear_on_submit=True):
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.subheader("基础信息")
            constellation = st.selectbox(
                "选择你的星座", 
                list(constellations.keys()),
                placeholder="请选择你的星座..."
            )
            
            mbti = st.selectbox(
                "输入你的MBTI类型", 
                list(mbti_types.keys()),
                placeholder="例如: INTJ"
            )
            
            # 年龄改为数字输入框
            age = st.number_input(
                "输入你的年龄", 
                min_value=0, 
                max_value=120, 
                value=25,
                step=1,
                help="用于匹配专属年龄运势"
            )
            
        with col2:
            st.subheader("✨ 今日幸运签")
            st_lottie(lottie_fortune, height=200, key="main-animation")
        
        submitted = st.form_submit_button(
            "🔮 生成运势报告",
            type="primary",
            use_container_width=True
        )
    
    # 结果展示
    if submitted and constellation and mbti:
        # 计算年龄组
        if age < 18:
            age_group = "少年"
        elif age < 35:
            age_group = "青年"
        elif age < 60:
            age_group = "中年"
        else:
            age_group = "老年"
        
        # 生成报告
        st.divider()
        st.header("📜 运势分析报告")
        
        # 星座运势
        st.subheader("🌟 星座运势解析")
        st.write(f"**核心运势**：{constellations[constellation]['运势']}")
        st.write(f"**今日幸运**：{constellations[constellation]['lucky']}")
        st.success("宜：" + constellations[constellation]['tips'].split('|')[0].strip())
        st.warning("忌：" + constellations[constellation]['tips'].split('|')[1].strip())
        st_lottie(lottie_fortune, height=180, key="horoscope-animation")
        
        # MBTI 运势
        st.subheader("🧠 MBTI 专属指引")
        st.write(f"**性格优势**：{mbti_types[mbti]['运势'].split('，')[0]}")
        st.write(f"**潜在挑战**：{mbti_types[mbti]['运势'].split('，')[1]}")
        st.info(mbti_types[mbti]['tips'])
        st_lottie(lottie_warning, height=180, key="mbti-animation")
        
        # 年龄运势
        st.subheader("📅 年龄阶段运势")
        st.write(f"**当前阶段**：{age_group}（{age}岁）")
        st.write(f"**阶段特征**：{age_fortunes[age_group]['运势']}")
        st.write(f"**幸运信息**：{age_fortunes[age_group]['lucky']}")
        st_lottie(lottie_fortune, height=180, key="age-animation")
        
        # 彩蛋：随机鼓励语
        st.divider()
        st.subheader("💡 今日特别提醒")
        encouragements = [
            "今天的你比昨天更接近梦想！",
            "所有的努力都在积累属于你的奇迹",
            "别担心，一切都是最好的安排",
            "勇气是此刻最亮的光芒"
        ]
        st.success(random.choice(encouragements), icon="✨")

if __name__ == "__main__":
    main()
