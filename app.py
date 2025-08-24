# Importing Libraries
import streamlit as st
import warnings
import os
import tempfile
from pathlib import Path
from crewai import Crew

from agents import create_agents
from tasks import agent_tasks
from app_utils import enter_and_set_api_keys, pretty_print_result

# Optional imports with fallbacks
try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
try:
    import docx
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# Warning Control
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="AI-Powered Job Application Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for improved UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .input-container {
        # background: #36454F;
        padding: 0rem,2rem;
        # border-radius: 10px;
        # border: 1px solid #e9ecef;
        # margin-bottom: 2rem;
    }
    .result-container {
        background: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .agent-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .footer {
        font-size: 1rem;
        color: #666;
        text-align: center;
        padding: 0.5rem 0;
        margin: 2rem 0 1rem 0;
    }
    .success-box {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }

</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'api_keys_configured' not in st.session_state:
    st.session_state.api_keys_configured = False
if 'resume_content' not in st.session_state:
    st.session_state.resume_content = ""
if 'resume_uploaded' not in st.session_state:
    st.session_state.resume_uploaded = False

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    
    if not PDF_AVAILABLE:
        st.error("PyPDF2 is not installed. Please install it to read PDF files: pip install PyPDF2")
        return ""
    
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return ""

def extract_text_from_docx(docx_file):
    """Extract text from uploaded Word document"""
    if not DOCX_AVAILABLE:
        st.error("python-docx is not installed. Please install it to read Word files: pip install python-docx")
        return ""
    
    try:
        doc = docx.Document(docx_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading Word document: {str(e)}")
        return ""

def extract_text_from_txt(txt_file):
    """Extract text from uploaded text file"""
    try:
        return txt_file.read().decode('utf-8')
    except Exception as e:
        st.error(f"Error reading text file: {str(e)}")
        return ""

def save_resume_content(content, filename="resume.md"):
    """Save resume content to a temporary file"""
    try:
        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path
    except Exception as e:
        st.error(f"Error saving resume: {str(e)}")
        return None

def run_job_application_crew(job_url, github_url, personal_writeup, resume_path):
    """Run the job application crew with user inputs"""
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Initialize progress
        status_text.text("🔄 Initializing AI agents...")
        progress_bar.progress(20)
        
        # Create agents
        researcher, profiler, resume_strategist, interview_preparer = create_agents()
        
        status_text.text("📋 Creating tasks...")
        progress_bar.progress(40)
        
        # Create tasks
        research_task, profile_task, resume_strategy_task, interview_preparation_task = agent_tasks()
        
        status_text.text("🤖 Setting up crew...")
        progress_bar.progress(60)
        
        # Create crew
        job_application_crew = Crew(
            agents=[researcher, profiler, resume_strategist, interview_preparer],
            tasks=[research_task, profile_task, resume_strategy_task, interview_preparation_task],
            verbose=True,
            memory=True
        )
        
        status_text.text("🚀 Processing your application...")
        progress_bar.progress(80)
        
        # Prepare inputs
        inputs = {
            'job_posting_url': job_url,
            'github_url': github_url,
            'personal_writeup': personal_writeup
        }
        
        # Execute crew
        result = job_application_crew.kickoff(inputs=inputs)
        
        progress_bar.progress(100)
        status_text.text("✅ Complete!")
        
        return result
        
    except Exception as e:
        progress_bar.progress(0)
        status_text.text("❌ Error occurred")
        raise e

def main():
    # Header
    st.markdown('<h1 class="main-header">💼 Elite AI Career Intelligence System</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Advanced Multi-Agent AI for Strategic Job Application Optimization & Interview Mastery</p>', unsafe_allow_html=True)

    # Sidebar for configuration and agent info
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")

        with st.expander("🔑 API Key Configuration", expanded=True):
            st.write("Set your API keys below to enable the AI agents.")
            
            # API Key Configuration
            openai_api_key = st.text_input("OpenAI API Key", type="password", placeholder="Enter your OpenAI API key here", help="Enter your OpenAI API key")
            serper_api_key = st.text_input("Serper API Key", type="password", placeholder="Your Serper API key", help="Enter your Serper API key for web search")
            
            # Add button to confirm API key configuration
            if st.button("Connect API Keys", use_container_width=True, type="primary", key="connect_api_button"):
                if not openai_api_key or not serper_api_key:
                    # st.error("❌ Please enter both API keys to proceed.")
                    st.session_state.api_keys_configured = False
                else:
                    st.session_state.api_keys_configured = True
                    st.success("✅ API keys configured successfully!")
                    
                    # Set environment variables
                    os.environ["OPENAI_API_KEY"] = openai_api_key
                    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
                    os.environ["SERPER_API_KEY"] = serper_api_key
                    
                    st.rerun()  # Refresh to show the main application

        st.markdown("---")
        
        
        # Agent Information
        with st.expander("🤖 Elite AI Agents & 🛠️ Advanced Tools", expanded=False):
            st.markdown("""
            **Elite AI Specialist Agents:**
            - **🔍 Job Requirements Intelligence Analyst**: Deep-dive analysis of job postings with precision requirement extraction
            - **📊 Master Data Extraction Analyst**: Comprehensive candidate intelligence profiling from all sources  
            - **🎯 Strategic Resume Architecture Specialist**: Advanced resume optimization with ATS compatibility
            - **🎤 Master Interview Strategist**: Evidence-based interview preparation and authentic positioning

            **Advanced Capabilities & Tools:**
            - **🌐 Intelligent Web Scraping**: Precision job posting analysis and requirements extraction
            - **📄 Multi-Format Resume Processing**: PDF, DOCX, TXT, MD with comprehensive text extraction
            - **🔍 Semantic Content Analysis**: Deep understanding of skills, experiences, and achievements
            - **⚡ Strategic Content Generation**: Tailored resumes and interview materials with authenticity guarantee
            - **🎯 ATS Optimization**: Keyword integration and formatting for maximum compatibility
            - **📈 Job Alignment Intelligence**: Precise matching of candidate capabilities to role requirements
            """)

        st.markdown("---")
        st.markdown('<div style="text-align:center;"><strong>Need help?</strong> Contact Now</div>', unsafe_allow_html=True)

        st.markdown("""
        <div style="display: flex; justify-content: center; gap: 10px; align-items: center; margin-top: 12px;">
            <a href="https://github.com/saadtoorx" target="_blank" title="GitHub">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="22" height="22" style="vertical-align: middle;">
            </a>
            <a href="https://twitter.com/saadtoorx" target="_blank" title="Twitter">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/twitter/twitter-original.svg" alt="Twitter" width="22" height="22" style="vertical-align: middle;">
            </a>
            <a href="https://huggingface.co/saadtoorx" target="_blank" title="HuggingFace">
            <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="HuggingFace" width="22" height="22" style="vertical-align: middle;">
            </a>
        </div>
        """, unsafe_allow_html=True)

    # Main content area - conditional display based on API key configuration
    if not st.session_state.api_keys_configured:
        # Show welcome/info screen when API keys are not configured
        st.markdown("---")
        
        # Main welcome section
        col1, col2, col3, col4, col5 = st.columns([2, 6, 1, 6, 2])

        with col2:
            st.markdown(
                """
                <div class="input-container">
                <h3>ℹ️ AI Career Intelligence System</h3>
                <p style="text-align: justify;">
                This advanced multi-agent AI system provides comprehensive job application optimization using cutting-edge artificial intelligence. Our elite AI specialists conduct deep analysis to maximize your interview success while maintaining 100% authenticity.
                </p>
                
                <h4>🎯 Advanced Capabilities:</h4>
                <ul>
                    <li><b>Comprehensive Data Extraction</b> - Systematically analyze resume, GitHub, and personal profile</li>
                    <li><b>Strategic Job Intelligence</b> - Deep-dive analysis of job requirements and company culture</li>
                    <li><b>Elite Resume Optimization</b> - ATS-compatible resumes with strategic keyword integration</li>
                    <li><b>Master Interview Preparation</b> - Evidence-based positioning and authentic storytelling</li>
                    <li><b>100% Authenticity Guarantee</b> - Only your documented skills and experiences used</li>
                </ul>

                <div class="input-container">
                <h4>🔒 Security & Privacy:</h4>
                <ul>
                    <li><b>Data Encryption</b> - All user data is encrypted and secure</li>
                    <li><b>Privacy Compliance</b> - Adheres to all relevant data protection regulations</li>
                </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        with col4:
            # Application preview image
            image_path = "images/image_start.png"
            if os.path.exists(image_path):
                st.image(image_path, width=400)
            else:
                st.markdown(
                    """
                    <div class="input-container" style="text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
                    <h3>🚀 AI Application Assistant</h3>
                    <p>Visual Preview Coming Soon</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            st.markdown(
                """
                <div class="input-container">
                <h3>✅ Elite Features</h3>
                <ul>
                <li><b>Job Requirements Analysis</b> - Deep insights into postings</li>
                <li><b>ATS Resume Optimization</b> - Strategic, authentic formatting</li>
                <li><b>Interview Prep Mastery</b> - Evidence-based positioning</li>
                <li><b>Comprehensive Data Mining</b> - Systematic source analysis</li>
                <li><b>Authenticity Guarantee</b> - No fabrication, only facts</li>
                <li><b>Semantic Skill Mapping</b> - Advanced matching of skills to job criteria</li>
                <li><b>Personalized Action Plan</b> - Step-by-step guidance for application success</li>
                </ul>
                """,
                unsafe_allow_html=True
            )
        
        st.markdown("---")
        st.markdown('<h6 class="footer">Developed and Designed by Saad Toor | saadtoorx</h6>', unsafe_allow_html=True)
        
        return  # Exit function here to show only welcome content

    # Show application tabs when API keys are configured
    else:
        # Create tabs for better organization
        tab1, tab2, = st.tabs(["📄 Upload & Input", "📊 Results"])

        with tab1:
            st.markdown("### 📄 Resume Upload")
            
            # Resume upload section
            col1, col2, col3, col4, col5 = st.columns([2, 6, 1, 6, 2])
            
            with col2:
                st.markdown("#### Upload Your Resume")
                uploaded_file = st.file_uploader(
                    "Choose your resume file",
                    type=['pdf', 'txt', 'docx', 'md'],
                    help="Supported formats: PDF, TXT, DOCX, MD"
                )
                
                if uploaded_file is not None:
                    file_extension = uploaded_file.name.split('.')[-1].lower()
                    
                    # Extract text based on file type
                    if file_extension == 'pdf':
                        if not PDF_AVAILABLE:
                            st.error("PyPDF2 not installed. Please install it to read PDF files.")
                            resume_text = ""
                        else:
                            resume_text = extract_text_from_pdf(uploaded_file)
                    elif file_extension == 'docx':
                        if not DOCX_AVAILABLE:
                            st.error("python-docx not installed. Please install it to read Word files.")
                            resume_text = ""
                        else:
                            resume_text = extract_text_from_docx(uploaded_file)
                    elif file_extension in ['txt', 'md']:
                        resume_text = extract_text_from_txt(uploaded_file)
                    else:
                        st.error("Unsupported file format")
                        resume_text = ""
                    
                    if resume_text:
                        st.session_state.resume_content = resume_text
                        st.session_state.resume_uploaded = True
                        st.success(f"✅ Resume uploaded successfully! ({len(resume_text)} characters)")
                        
                        # Save resume content to file
                        resume_path = save_resume_content(resume_text)
                        if resume_path:
                            st.session_state.resume_path = resume_path
                
                job_posting_url = st.text_input(
                    "Job Posting URL",
                    placeholder="https://example.com/job-posting",
                    help="Enter the URL of the job posting you're applying for"
                )
                
                github_url = st.text_input(
                    "GitHub Profile URL",
                    placeholder="https://github.com/yourusername",
                    help="Enter your GitHub profile URL (optional but recommended)"
                )

                personal_writeup = st.text_area(
                    "Personal Summary/Bio",
                    placeholder="Write a brief summary about yourself, your experience, skills, and career goals...",
                    height=150,
                    help="Provide a comprehensive writeup about yourself"
                )

            with col4:
                st.markdown("#### Resume Preview")
                st.markdown("Here's a preview of your uploaded resume:")
                if st.session_state.resume_uploaded:
                    with st.expander("View Resume Content", expanded=False):
                        st.text_area(
                            "Resume Content",
                            value=st.session_state.resume_content[:1000] + "..." if len(st.session_state.resume_content) > 1000 else st.session_state.resume_content,
                            height=200,
                            disabled=True
                        )
                else:
                    st.info("Upload your resume to see preview here")
                
                if not all([st.session_state.resume_uploaded, job_posting_url, personal_writeup]):
                    st.warning("⚠️ Please complete all required fields before processing.")
                    st.markdown("### ✅ Application Checklist")
                    col4a, col4b, col4c, col4d = st.columns(4)
                    with col4a:
                        if st.session_state.resume_uploaded:
                            st.success("✅ **Resume Uploaded**")
                        else:
                            st.error("❌ **Resume Required**")
                    
                    with col4b:
                        if job_posting_url:
                            st.success("✅ **Job URL Provided**")
                        else:
                            st.error("❌ **Job URL Required**")
                    
                    with col4c:
                        if personal_writeup:
                            st.success("✅ **Bio Provided**")
                        else:
                            st.error("❌ **Bio Required**")
                    
                    with col4d:
                        if github_url:
                            st.success("✅ **Git URL Provided**")
                        else:
                            st.warning("⚠️ **Git URL Optional**")

                else:
                    st.markdown("### 🎯 Process Your Application")
                    st.markdown("#### Ready to Process!")
                    st.info("All required information has been provided. Click the button below to start processing your job application.")
                    
                    if st.button("🚀 Launch Elite AI Processing", type="primary", use_container_width=True):
                        try:
                            with st.spinner("Elite AI specialists are strategically optimizing your application..."):
                                result = run_job_application_crew(
                                    job_posting_url,
                                    github_url if github_url else "https://github.com",
                                    personal_writeup,
                                    st.session_state.get('resume_path', '')
                                )
                                
                                st.session_state.processing_result = result
                                st.success("✅ Elite optimization completed successfully!")
                                st.balloons()
                                
                        except Exception as e:
                            st.error(f"❌ Error during processing: {str(e)}")
                            st.info("Please check your inputs and try again.")

            st.markdown("---")
            
        # with tab2:

        with tab2:
            st.markdown("### 📊 Results & Outputs")
            
            if 'processing_result' in st.session_state:
                st.markdown("#### 🎉 Your AI-Generated Application Materials")
                
                # Display results in expandable sections
                with st.expander("📋 Complete Results", expanded=True):
                    st.markdown("**Full AI Analysis and Recommendations:**")
                    st.write(st.session_state.processing_result)
                
                with st.expander("📄 Pretty Formatted Results", expanded=False):
                    st.code(pretty_print_result(str(st.session_state.processing_result)))
                
                # Check if output files were created
                st.markdown("#### 📁 Generated Files")
                
                col9, col10 = st.columns(2)
                
                with col9:
                    if os.path.exists("tailored_resume.md"):
                        st.markdown("##### ✅ Tailored Resume")
                        with open("tailored_resume.md", "r", encoding="utf-8") as f:
                            resume_content = f.read()
                        st.download_button(
                            label="📄 Download Tailored Resume",
                            data=resume_content,
                            file_name="tailored_resume.md",
                            mime="text/markdown"
                        )
                        with st.expander("View Tailored Resume"):
                            st.markdown(resume_content)
                    else:
                        st.warning("Tailored resume file not found")
                
                with col10:
                    if os.path.exists("interview_preparation.md"):
                        st.markdown("##### ✅ Interview Preparation")
                        with open("interview_preparation.md", "r", encoding="utf-8") as f:
                            interview_content = f.read()
                        st.download_button(
                            label="🎤 Download Interview Prep",
                            data=interview_content,
                            file_name="interview_preparation.md",
                            mime="text/markdown"
                        )
                        with st.expander("View Interview Preparation"):
                            st.markdown(interview_content)
                    else:
                        st.warning("Interview preparation file not found")
                
                # Action buttons
                st.markdown("#### 🔄 Next Steps")
                col11, col12, col13 = st.columns(3)
                
                with col11:
                    if st.button("🔄 Process Another Application", use_container_width=True):
                        # Clear session state for new application
                        for key in ['processing_result', 'resume_content', 'resume_uploaded', 'resume_path']:
                            if key in st.session_state:
                                del st.session_state[key]
                        st.rerun()
                
                with col12:
                    if st.button("📧 Share Results", use_container_width=True):
                        st.info("Copy the results above to share with others!")
                
                with col13:
                    if st.button("💾 Save to Cloud", use_container_width=True):
                        st.info("Cloud save feature coming soon!")
            
            else:
                st.info("🎯 Process your application in the 'Process Application' tab to see results here.")

    # Footer
    st.markdown('<h6 class="footer">Developed & Designed by Saad Toor | saadtoorx</h6>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()