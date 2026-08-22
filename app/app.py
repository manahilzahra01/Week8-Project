
import streamlit as st
from sentence_transformers import SentenceTransformer, util

st.set_page_config(page_title="AI Resume Matcher", layout="wide")

st.title("🤖 AI-Powered Resume Analyzer & Job Matcher")
st.write("Upload or paste resume text and job requirements to analyze semantic fit and skill gaps.")

col1, col2 = st.columns(2)

with col1:
    jd_input = st.text_area("📄 Job Description:", height=200)
    skills_input = st.text_input("🔑 Required Skills (comma-separated):", "Python, Machine Learning, SQL, AWS")

with col2:
    resume_input = st.text_area("👤 Resume Text:", height=200)

if st.button("🚀 Analyze Match"):
    if jd_input and resume_input:
        with st.spinner("Analyzing semantic similarity..."):
            model = SentenceTransformer('all-MiniLM-L6-v2')
            jd_emb = model.encode(jd_input, convert_to_tensor=True)
            res_emb = model.encode(resume_input, convert_to_tensor=True)
            similarity = util.cos_sim(jd_emb, res_emb).item() * 100
            
            st.markdown("---")
            st.subheader(f"📊 Overall Semantic Match Score: **{similarity:.2f}%**")
            
            if skills_input:
                required_skills = [s.strip() for s in skills_input.split(",") if s.strip()]
                matched = [s for s in required_skills if s.lower() in resume_input.lower()]
                missing = [s for s in required_skills if s.lower() not in resume_input.lower()]
                
                c1, c2 = st.columns(2)
                with c1:
                    st.success(f"✅ **Matched Skills ({len(matched)}):**
" + (", ".join(matched) if matched else "None"))
                with c2:
                    st.error(f"❌ **Missing Skills Gap ({len(missing)}):**
" + (", ".join(missing) if missing else "None"))
    else:
        st.warning("⚠️ Please provide both Job Description and Resume Text.")
