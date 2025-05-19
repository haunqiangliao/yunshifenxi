import streamlit as st
import random

# 配置页面
st.set_page_config(
    page_title="🌟 多维运势分析站",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 星座数据库（已补全所有星座）
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
    "双子座": {
        "运势": "思维活跃，适合学习新知识或开展新项目，社交活动增多。",
        "lucky": "幸运色: 黄色 | 幸运数字: 3",
        "tips": "宜: 沟通交流 | 忌: 犹豫不决"
    },
    "巨蟹座": {
        "运势": "家庭关系和睦，但需注意调节情绪，避免过度敏感。",
        "lucky": "幸运色: 银色 | 幸运数字: 2",
        "tips": "宜: 家庭聚会 | 忌: 胡思乱想"
    },
    "狮子座": {
        "运势": "事业上有机会展现才华，获得认可，但需注意别太自我中心。",
        "lucky": "幸运色: 金色 | 幸运数字: 1",
        "tips": "宜: 领导活动 | 忌: 独断专行"
    },
    "处女座": {
        "运势": "适合处理繁琐事务，工作效率高，但容易给自己压力过大。",
        "lucky": "幸运色: 灰色 | 幸运数字: 4",
        "tips": "宜: 精细工作 | 忌: 吹毛求疵"
    },
    "天秤座": {
        "运势": "人际关系融洽，可能会有浪漫际遇，需注意在抉择时别犹豫不决。",
        "lucky": "幸运色: 淡蓝色 | 幸运数字: 7",
        "tips": "宜: 社交活动 | 忌: 优柔寡断"
    },
    "天蝎座": {
        "运势": "近期会有深刻的自我反思，适合挖掘潜力，但要避免猜疑过度。",
        "lucky": "幸运色: 黑色 | 幸运数字: 8",
        "tips": "宜: 自我提升 | 忌: 猜疑他人"
    },
    "射手座": {
        "运势": "适合旅行或学习新技能，拓展视野，可能会有意外的学习机会。",
        "lucky": "幸运色: 紫色 | 幸运数字: 9",
        "tips": "宜: 探索未知 | 忌: 半途而废"
    },
    "摩羯座": {
        "运势": "事业上会有稳步进展，适合制定长期目标，但需注意劳逸结合。",
        "lucky": "幸运色: 棕色 | 幸运数字: 0",
        "tips": "宜: 长期规划 | 忌: 过度劳累"
    },
    "水瓶座": {
        "运势": "灵感迸发，适合创新项目或团队合作，但可能会有些特立独行。",
        "lucky": "幸运色: 蓝色 | 幸运数字: 4",
        "tips": "宜: 创新思考 | 忌: 脱离群体"
    },
    "双鱼座": {
        "运势": "艺术灵感涌现，适合创作或表达情感，但需注意别过于幻想。",
        "lucky": "幸运色: 粉色 | 幸运数字: 6",
        "tips": "宜: 艺术创作 | 忌: 空想不行动"
    }
}

# MBTI数据库（已补全所有类型）
mbti_types = {
    "ISTJ": {
        "运势": "适合处理复杂任务，工作效率高，但可能会因过于固执错过新机会。",
        "lucky": "幸运色: 深蓝色 | 幸运数字: 3",
        "tips": "宜: 按计划执行 | 忌: 频繁变动"
    },
    "ISFJ": {
        "运势": "人际关系良好，适合帮助他人，但需注意别过度牺牲自己。",
        "lucky": "幸运色: 暖绿色 | 幸运数字: 2",
        "tips": "宜: 团队协作 | 忌: 委屈自己"
    },
    "INFJ": {
        "运势": "灵感丰富，适合创作或策划，但可能会因追求完美而拖延。",
        "lucky": "幸运色: 靛蓝色 | 幸运数字: 9",
        "tips": "宜: 创意工作 | 忌: 过度追求完美"
    },
    "INTJ": {
        "运势": "适合进行深入研究或规划，可能会有突破性的想法。",
        "lucky": "幸运色: 深紫色 | 幸运数字: 8",
        "tips": "宜: 战略规划 | 忌: 忽视细节"
    },
    "ISTP": {
        "运势": "适合处理实际问题，可能会有意外的冒险机会。",
        "lucky": "幸运色: 橄榄绿 | 幸运数字: 5",
        "tips": "宜: 动手实践 | 忌: 缺乏耐心"
    },
    "ISFP": {
        "运势": "艺术灵感涌现，适合表达自我，但需注意别过于情绪化。",
        "lucky": "幸运色: 珊瑚色 | 幸运数字: 7",
        "tips": "宜: 艺术表达 | 忌: 情绪波动"
    },
    "INFP": {
        "运势": "适合思考人生方向，可能会有新的感悟，但需注意别过于空想。",
        "lucky": "幸运色: 薰衣草紫 | 幸运数字: 4",
        "tips": "宜: 哲学思考 | 忌: 脱离现实"
    },
    "INTP": {
        "运势": "适合学习新知识或研究新领域，可能会有意外的发现。",
        "lucky": "幸运色: 薄荷绿 | 幸运数字: 1",
        "tips": "宜: 学术研究 | 忌: 过度理论化"
    },
    "ESTP": {
        "运势": "适合参与社交活动或竞争，可能会有意外的机遇。",
        "lucky": "幸运色: 橙色 | 幸运数字: 6",
        "tips": "宜: 挑战自我 | 忌: 鲁莽行事"
    },
    "ESFP": {
        "运势": "社交活动丰富，可能会有浪漫际遇，但需注意别过于冲动。",
        "lucky": "幸运色: 亮粉色 | 幸运数字: 2",
        "tips": "宜: 社交聚会 | 忌: 冲动消费"
    },
    "ENFP": {
        "运势": "适合开展新项目或合作，可能会有新的人脉资源。",
        "lucky": "幸运色: 亮紫色 | 幸运数字: 7",
        "tips": "宜: 创业合作 | 忌: 三分钟热度"
    },
    "ENTP": {
        "运势": "适合参与讨论或竞争，可能会有新的想法或机会。",
        "lucky": "幸运色: 绿松石色 | 幸运数字: 3",
        "tips": "宜: 辩论谈判 | 忌: 过于争论"
    },
    "ESTJ": {
        "运势": "适合领导团队或处理事务，可能会有晋升机会。",
        "lucky": "幸运色: 深灰色 | 幸运数字: 8",
        "tips": "宜: 管理职位 | 忌: 过于严格"
    },
    "ESFJ": {
        "运势": "人际关系良好，适合协调或帮助他人，但需注意别过于迁就。",
        "lucky": "幸运色: 金色 | 幸运数字: 9",
        "tips": "宜: 组织协调 | 忌: 失去自我"
    },
    "ENFJ": {
        "运势": "适合领导团队或组织活动，可能会获得他人认可。",
        "lucky": "幸运色: 紫红色 | 幸运数字: 1",
        "tips": "宜: 团队领导 | 忌: 过度付出"
    },
    "ENTJ": {
        "运势": "适合制定战略或领导团队，可能会有重要的决策要做。",
        "lucky": "幸运色: 藏青色 | 幸运数字: 4",
        "tips": "宜: 高层管理 | 忌: 独断专行"
    }
}

# 年龄分类运势（确保包含所有可能的年龄组）
age_fortunes = {
    "少年": {
        "运势": "学习方面会有新的突破，可能会遇到良师益友。",
        "lucky": "幸运色: 橙色 | 幸运数字: 9",
        "tips": "宜: 参加社团 | 忌: 闭门造车"
    },
    "青年": {
        "运势": "事业和爱情都有发展机会，要勇敢追求自己的目标。",
        "lucky": "幸运色: 红色 | 幸运数字: 7",
        "tips": "宜: 职业规划 | 忌: 犹豫不决"
    },
    "中年": {
        "运势": "事业稳定，家庭幸福，但需注意身体健康。",
        "lucky": "幸运色: 绿色 | 幸运数字: 5",
        "tips": "宜: 健康管理 | 忌: 过度劳累"
    },
    "老年": {
        "运势": "享受生活，安度晚年，可能会有一些回忆涌上心头。",
        "lucky": "幸运色: 紫色 | 幸运数字: 3",
        "tips": "宜: 休闲活动 | 忌: 操心过多"
    }
}

# 主程序
def main():
    st.title("🌟 多维运势分析站 🌟")
    st.write("✨ 结合星座、MBTI、年龄的深度运势解析")
    
    # 侧边栏装饰
    with st.sidebar:
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
            # 移除动画相关代码
        
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
        
        # MBTI 运势
        st.subheader("🧠 MBTI 专属指引")
        st.write(f"**性格优势**：{mbti_types[mbti]['运势'].split('，')[0]}")
        st.write(f"**潜在挑战**：{mbti_types[mbti]['运势'].split('，')[1]}")
        st.info(mbti_types[mbti]['tips'])
        
        # 年龄运势（添加错误处理）
        st.subheader("📅 年龄阶段运势")
        st.write(f"**当前阶段**：{age_group}（{age}岁）")
        
        # 确保年龄组存在于数据库中
        if age_group in age_fortunes:
            st.write(f"**阶段特征**：{age_fortunes[age_group]['运势']}")
            st.write(f"**幸运信息**：{age_fortunes[age_group]['lucky']}")
        else:
            st.warning(f"暂未收录 {age_group} 阶段的运势信息，敬请期待更新！")
        
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
