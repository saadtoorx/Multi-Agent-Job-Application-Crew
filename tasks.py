from crewai import Task
from agents import create_agents

def agent_tasks():
    
    # Create agents inside the function after API keys are set
    researcher, profiler, resume_strategist, interview_preparer = create_agents()

    # Task 1: Deep Job Requirements Intelligence Analysis
    research_task = Task(
        description=(
            """CONDUCT COMPREHENSIVE JOB POSTING INTELLIGENCE ANALYSIS

            **PRIMARY MISSION**: Extract and analyze every detail from the job posting URL ({job_posting_url}) to create a complete intelligence profile that enables perfect candidate-job alignment.

            **SYSTEMATIC ANALYSIS FRAMEWORK**:

            1. **TECHNICAL REQUIREMENTS EXTRACTION**:
               - Programming languages (required vs preferred with proficiency levels)
               - Frameworks, libraries, and development tools (with version specificity)
               - System architectures and design patterns mentioned
               - Database technologies and data management requirements
               - Cloud platforms and DevOps tools specified
               - Security, performance, and scalability considerations

            2. **EXPERIENCE & QUALIFICATION ANALYSIS**:
               - Years of experience required (minimum vs ideal)
               - Industry domain experience preferences
               - Project scale and complexity indicators
               - Team leadership and collaboration requirements
               - Educational background expectations and certifications

            3. **ROLE RESPONSIBILITIES DEEP-DIVE**:
               - Day-to-day technical responsibilities and ownership areas
               - Collaboration patterns (team size, stakeholder interaction)
               - Problem-solving scope and technical challenges
               - Innovation and research expectations
               - Mentorship and knowledge-sharing responsibilities

            4. **COMPANY CULTURE & ENVIRONMENT INTELLIGENCE**:
               - Work style preferences (remote, hybrid, on-site)
               - Team dynamics and collaboration philosophy
               - Growth mindset and learning culture indicators
               - Innovation approach and technical risk tolerance
               - Diversity, equity, and inclusion commitments

            5. **STRATEGIC PRIORITIZATION MATRIX**:
               - CRITICAL (Must-have): Non-negotiable requirements for candidacy
               - IMPORTANT (Strongly preferred): Significant advantages but not disqualifying if absent
               - PREFERRED (Nice-to-have): Additional qualifications that provide competitive edge
               - GROWTH AREAS (Learnable on-job): Skills mentioned as development opportunities

            **CRITICAL ANALYSIS PROTOCOLS**:
            - Extract exact terminology and keywords used in posting
            - Identify implicit requirements suggested by role responsibilities
            - Analyze job level indicators (junior, mid, senior, lead, principal)
            - Note any unique or specialized requirements that distinguish this role
            - Document salary, benefits, and growth opportunity mentions
            """
        ),
        expected_output=(
            """**COMPREHENSIVE JOB REQUIREMENTS INTELLIGENCE REPORT**

            ## 🎯 ROLE OVERVIEW
            **Position Title**: [Exact title from posting]
            **Company**: [Organization name]
            **Location**: [Work location and arrangement]
            **Experience Level**: [Required years and seniority level]

            ## 💻 TECHNICAL REQUIREMENTS MATRIX

            ### **CRITICAL TECHNICAL SKILLS** (Must-Have)
            | Technology | Requirement Level | Proficiency Expected | Usage Context |
            |------------|------------------|---------------------|---------------|
            | [Tech 1] | Required | [Years/Level] | [How it's used in role] |

            ### **IMPORTANT TECHNICAL SKILLS** (Strongly Preferred)
            | Technology | Preference Level | Value-Add | Application Area |
            |------------|------------------|-----------|------------------|
            | [Tech 2] | Preferred | [Advantage gained] | [Role application] |

            ### **PREFERRED TECHNICAL SKILLS** (Competitive Advantage)
            - [Additional technologies that provide competitive edge]

            ## 🎓 QUALIFICATIONS & EXPERIENCE

            ### **Educational Requirements**:
            - **Required**: [Degree requirements as stated]
            - **Preferred**: [Additional qualifications mentioned]
            - **Certifications**: [Professional certifications valued]

            ### **Experience Expectations**:
            - **Minimum Experience**: [Years required]
            - **Domain Experience**: [Industry/area specificity]
            - **Project Scale**: [Complexity and scope expectations]
            - **Leadership**: [Team/project leadership requirements]

            ## 📋 CORE RESPONSIBILITIES ANALYSIS

            ### **Primary Technical Duties**:
            1. [Responsibility 1 as listed in posting]
            2. [Responsibility 2 as listed in posting]
            [Continue with all listed responsibilities]

            ### **Collaboration & Communication**:
            - **Team Interaction**: [How role interfaces with team members]
            - **Stakeholder Engagement**: [External collaboration requirements]
            - **Documentation**: [Communication and documentation expectations]

            ## 🏢 COMPANY CULTURE & WORK ENVIRONMENT

            ### **Work Style & Philosophy**:
            - **Work Arrangement**: [Remote/hybrid/on-site policies]
            - **Team Culture**: [Collaboration style and team dynamics]
            - **Learning Culture**: [Growth and development emphasis]
            - **Innovation Approach**: [R&D and experimentation tolerance]

            ### **Growth & Development**:
            - **Career Progression**: [Advancement opportunities mentioned]
            - **Learning Support**: [Training and development programs]
            - **Mentorship**: [Knowledge sharing and mentoring culture]

            ## 💰 COMPENSATION & BENEFITS
            - [Only information explicitly provided in posting]

            ## 🔍 KEY RESPONSIBILITIES
            1. [Responsibility 1 as listed]
            2. [Responsibility 2 as listed]
            [Continue with actual responsibilities from posting]

            ## 📊 REQUIREMENT PRIORITY ANALYSIS
            - **Critical/Must-Have**: [Requirements clearly marked as essential]
            - **Important**: [Requirements emphasized but not marked as critical]
            - **Preferred**: [Items listed as preferred or nice-to-have]

            ## 🎯 STRATEGIC KEYWORDS FOR OPTIMIZATION
            **Primary Keywords**: [Most frequently mentioned technical terms]
            **Secondary Keywords**: [Important but less frequent terms]
            **Industry Keywords**: [Domain-specific terminology used]

            ## 📈 ROLE POSITIONING INSIGHTS
            - **Seniority Level**: [Junior/Mid/Senior/Lead indicators]
            - **Growth Trajectory**: [Implied career progression from role]
            - **Challenge Areas**: [Key technical/business challenges to address]
            - **Success Metrics**: [How success in role would be measured]

            **SOURCE VERIFICATION**: All information extracted directly from job posting at {job_posting_url}**"""
        ),
        agent = researcher,
        async_execution= True
    )

    #Task 2: Comprehensive Candidate Data Extraction & Analysis
    profile_task = Task(
        description=(
            """CONDUCT SYSTEMATIC CANDIDATE DATA EXTRACTION FROM ALL SOURCES

            **PRIMARY OBJECTIVE**: Create the most comprehensive candidate intelligence profile possible by systematically extracting, cataloging, and analyzing EVERY piece of information from all provided sources.

            **MULTI-SOURCE DATA EXTRACTION PROTOCOL**:

            1. **RESUME DOCUMENT COMPREHENSIVE ANALYSIS**:
               - Extract complete employment history (exact titles, companies, dates, responsibilities)
               - Document ALL technical skills listed with any proficiency indicators
               - Catalog educational background, certifications, and academic achievements
               - Identify quantified achievements and performance metrics (exact numbers/percentages)
               - Extract project details, technologies used, and documented outcomes
               - Note awards, recognitions, professional development activities

            2. **GITHUB PROFILE DEEP TECHNICAL ANALYSIS**: {github_url}
               - Systematically review ALL repositories for comprehensive technology usage
               - Extract programming languages with usage frequency and complexity assessment
               - Identify frameworks, libraries, and development tools implemented
               - Analyze project types, architectural patterns, and technical approaches
               - Review README files for project descriptions and technology explanations
               - Assess code quality indicators: documentation, testing, structure
               - Document collaboration evidence: contributors, issues, pull requests

            3. **PERSONAL WRITEUP NARRATIVE ANALYSIS**: {personal_writeup}
               - Extract career goals, professional aspirations, and motivation drivers
               - Identify self-described strengths, skills, and competencies
               - Document mentioned experiences, achievements, and learning journeys
               - Catalog stated interests, passion areas, and professional focus
               - Note career transition points, growth experiences, and challenges overcome
               - Extract communication style, personality indicators, and values

            **SYSTEMATIC ORGANIZATION FRAMEWORK**:

            1. **TECHNICAL SKILLS COMPREHENSIVE INVENTORY**:
               - Programming Languages: [Source verification and usage context]
               - Frameworks & Libraries: [Implementation evidence and project usage]
               - Development Tools: [Mentioned tools and demonstrated usage]
               - Methodologies: [Stated experience or observable implementation]
               - Domain Expertise: [Industry knowledge and specialized areas]

            2. **EXPERIENCE & ACHIEVEMENT DOCUMENTATION**:
               - Professional Employment: [Complete history with detailed responsibilities]
               - Project Portfolio: [Technical projects with outcomes and technologies]
               - Leadership Evidence: [Team roles, management experience, mentoring]
               - Problem-Solving Examples: [Challenges addressed and solutions implemented]
               - Innovation Indicators: [Creative approaches and novel implementations]

            3. **LEARNING & GROWTH EVIDENCE**:
               - Skill Development Timeline: [Technologies learned and progression]
               - Educational Journey: [Formal education and continuous learning]
               - Certification Achievements: [Professional development and qualifications]
               - Career Progression: [Role advancement and responsibility growth]

            **AUTHENTICITY & VERIFICATION PROTOCOLS**:
            - Document exact source for every piece of extracted information
            - Maintain clear distinction between stated claims and observable evidence
            - Identify information gaps where details are not provided
            - Cross-reference information across sources for consistency validation
            - Ensure 100% traceability of all claims to original materials
            """
        ),
        expected_output=(
            """**COMPREHENSIVE CANDIDATE INTELLIGENCE PROFILE**

            ## 📋 CANDIDATE OVERVIEW
            **Full Name**: [From resume/materials]
            **Professional Title**: [Current/target role as stated]
            **Location**: [If provided]
            **Contact Information**: [As available]
            **LinkedIn/Portfolio**: [If mentioned]

            ## 🎯 PROFESSIONAL NARRATIVE & OBJECTIVES

            ### **Career Summary** (From Personal Writeup):
            [Comprehensive summary based on candidate's self-description]

            ### **Professional Goals & Aspirations**:
            - **Primary Objective**: [Main career goal as stated]
            - **Secondary Goals**: [Additional aspirations mentioned]
            - **Motivation Drivers**: [What drives the candidate professionally]
            - **Growth Areas**: [Areas candidate wants to develop]

            ### **Core Professional Values**:
            [Values and principles evidenced in candidate's narrative]

            ## 💼 COMPLETE EMPLOYMENT HISTORY

            ### **[JOB TITLE]** | [COMPANY NAME] | [EXACT DATES]
            **Key Responsibilities**:
            - [Responsibility 1 as documented in resume]
            - [Responsibility 2 as documented in resume]
            - [Continue with all listed responsibilities]

            **Documented Achievements**:
            - [Achievement 1 with exact metrics provided]
            - [Achievement 2 with quantified results]
            - [Additional achievements as documented]

            **Technologies Used**: [Technical stack mentioned for this role]
            **Team Context**: [Team size, collaboration details if provided]

            [Repeat this section for ALL employment positions]

            ## 🎓 EDUCATION & PROFESSIONAL DEVELOPMENT

            ### **Formal Education**:
            - **[DEGREE TYPE]**: [Institution] | [Graduation Date] | [GPA if provided]
            - **Relevant Coursework**: [If mentioned]
            - **Academic Projects**: [If described]
            - **Academic Achievements**: [Honors, awards if mentioned]

            ### **Certifications & Training**:
            - **[Certification Name]**: [Issuing Organization] | [Date]
            - **[Training Program]**: [Provider] | [Completion details]

            ### **Continuous Learning Evidence**:
            [Self-directed learning initiatives mentioned by candidate]

            ## 🛠️ COMPREHENSIVE TECHNICAL SKILLS ANALYSIS

            ### **Programming Languages** (Evidence-Based Assessment):
            | Language | Source Evidence | Usage Context | Proficiency Indicators |
            |----------|----------------|---------------|----------------------|
            | [Language 1] | [Resume/GitHub/Writeup] | [Projects/Work usage] | [Observable skill level] |
            | [Language 2] | [Source of evidence] | [Application context] | [Proficiency evidence] |

            ### **Frameworks & Technologies**:
            | Technology | Implementation Evidence | Projects Used | Complexity Level |
            |------------|------------------------|---------------|------------------|
            | [Framework 1] | [Specific usage proof] | [Project names] | [Assessed level] |
            | [Framework 2] | [Evidence source] | [Usage context] | [Skill indication] |

            ### **Development Tools & Platforms**:
            - **Version Control**: [Git usage evidence from GitHub]
            - **Development Environments**: [IDEs/editors mentioned or observed]
            - **Cloud Platforms**: [AWS/Azure/GCP experience documented]
            - **Databases**: [Database technologies used in projects]
            - **DevOps & CI/CD**: [Automation tools evidenced in projects]

            ### **Methodologies & Best Practices**:
            - **Development Approaches**: [Agile, TDD, etc. - if mentioned or evidenced]
            - **Code Quality Practices**: [Testing, documentation patterns observed]
            - **Collaboration Tools**: [Team development tools used]

            ## 📁 DETAILED PROJECT PORTFOLIO ANALYSIS

            ### **GitHub Repository Analysis**:

            #### **[Repository Name 1]**
            - **Description**: [From README or repository description]
            - **Primary Technologies**: [Languages and frameworks identified]
            - **Key Features Implemented**: [Functionality evidenced in code]
            - **Architecture Approach**: [Design patterns and structure observed]
            - **Code Quality Indicators**: [Documentation, testing, organization]
            - **Collaboration Evidence**: [Contributors, issues, PR activity]
            - **Complexity Assessment**: [Technical sophistication level]
            - **Last Updated**: [Activity recency]

            [Continue for ALL significant repositories]

            ### **Professional Projects** (From Resume/Experience):

            #### **[Project Name]**
            - **Context**: [Work/academic/personal project context]
            - **Role & Responsibilities**: [Candidate's specific role]
            - **Technologies Implemented**: [Tech stack used]
            - **Challenges Addressed**: [Problems solved]
            - **Outcomes Achieved**: [Results as documented by candidate]
            - **Duration & Scale**: [Timeline and project scope]

            ## 📊 QUANTIFIED ACHIEVEMENTS & IMPACT METRICS

            ### **Performance Indicators**:
            - **[Metric Category 1]**: [Exact numbers as provided by candidate]
            - **[Metric Category 2]**: [Quantified results documented]
            - **[Additional Metrics]**: [Performance data as stated]

            ### **Project Impact Measurements**:
            - **Technical Impact**: [System improvements, performance gains]
            - **Business Impact**: [Revenue, efficiency, user improvements]
            - **Team Impact**: [Collaboration improvements, knowledge sharing]

            ### **Recognition & Awards**:
            - **[Award/Recognition]**: [Context and year]
            - **[Achievement]**: [Organization and details]

            ## 🚀 PROFESSIONAL GROWTH & DEVELOPMENT TIMELINE

            ### **Recent Skill Development** (Past 2 Years):
            - **[New Technology/Skill]**: [Evidence of recent adoption]
            - **[Learning Initiative]**: [How skill was developed]

            ### **Career Progression Patterns**:
            - **Role Advancement**: [Career growth trajectory observed]
            - **Responsibility Expansion**: [Increasing scope and complexity]
            - **Technical Evolution**: [Technology stack progression]

            ## 🔍 SPECIALIZATION & EXPERTISE AREAS

            ### **Domain Expertise**:
            - **[Domain 1]**: [Evidence of specialized knowledge]
            - **[Domain 2]**: [Industry experience and depth]

            ### **Technical Depth Indicators**:
            - **[Deep Skill 1]**: [Advanced usage evidence]
            - **[Deep Skill 2]**: [Sophisticated implementation examples]

            ## 💡 UNIQUE VALUE PROPOSITIONS & DIFFERENTIATORS

            ### **Distinctive Combinations**:
            - **[Skill Combination]**: [Unique blend of capabilities]
            - **[Experience Mix]**: [Uncommon background elements]

            ### **Innovation & Problem-Solving Evidence**:
            - **[Creative Solution]**: [Novel approach documented]
            - **[Technical Innovation]**: [Unique implementation or idea]

            ## ⚠️ INFORMATION GAPS & ENHANCEMENT OPPORTUNITIES

            ### **Areas Not Specified**:
            - **[Gap 1]**: [Information not provided in materials]
            - **[Gap 2]**: [Could be enhanced with additional details]

            ### **Potential Clarifications**:
            - **[Area for Expansion]**: [Where more detail would be valuable]

            ## 📋 DATA SOURCE QUALITY ASSESSMENT

            ### **Information Completeness**:
            - **Resume Data**: [Comprehensive/Adequate/Limited assessment]
            - **GitHub Activity**: [Repository count, quality, recency]
            - **Personal Narrative**: [Depth and informativeness]
            - **Overall Profile Strength**: [Assessment for job matching capability]

            ### **Source Attribution Summary**:
            - **Resume-Sourced Information**: [Major data points from resume]
            - **GitHub-Evidenced Capabilities**: [Technical skills from code analysis]
            - **Writeup-Derived Insights**: [Goals and narrative from personal statement]

            **EXTRACTION VERIFICATION STATEMENT**: Every piece of information in this profile is directly sourced from candidate-provided materials with complete traceability maintained. No assumptions, inferences, or fabrications have been added.**"""
        ),
        agent = profiler,
        async_execution= True
    )

    #Task 3: Strategic Resume Architecture & Optimization
    resume_strategy_task = Task(
        description=(
            """TRANSFORM CANDIDATE DATA INTO STRATEGICALLY OPTIMIZED RESUME

            **PRIMARY MISSION**: Using the comprehensive candidate profile and job requirements analysis, create a strategically optimized resume that maximizes job alignment while maintaining 100% authenticity and complete source traceability.

            **STRATEGIC OPTIMIZATION METHODOLOGY**:

            1. **INTELLIGENT CONTENT ARCHITECTURE**:
               - Design information hierarchy to prioritize job-critical elements first
               - Structure sections to create maximum impact flow and readability
               - Optimize section ordering based on candidate's strongest job alignments
               - Create strategic emphasis through formatting and positioning

            2. **PRECISION KEYWORD INTEGRATION**:
               - Map job posting keywords to candidate's actual experience contexts
               - Integrate required terminology naturally within authentic content
               - Align technical language with job posting standards and expectations
               - Enhance relevance scoring while maintaining authenticity

            3. **ACHIEVEMENT AMPLIFICATION & QUANTIFICATION**:
               - Strategically present documented achievements using job-relevant language
               - Emphasize metrics and results that align with role success criteria
               - Reframe accomplishments to highlight transferable value to target role
               - Position quantified results for maximum impact and relevance

            4. **EXPERIENCE NARRATIVE OPTIMIZATION**:
               - Rewrite experience descriptions to emphasize job-relevant aspects
               - Lead with responsibilities and achievements most applicable to target role
               - Integrate job posting language naturally into existing experience descriptions
               - Create compelling professional story that demonstrates clear value proposition

            **STRICT AUTHENTICITY SAFEGUARDS**:

            1. **PRESERVATION PROTOCOLS** (NEVER MODIFY):
               - Educational credentials, institutions, degrees, graduation dates, GPAs
               - Employment dates, company names, official job titles
               - Personal contact information and professional identifiers
               - Actual metrics, percentages, and quantified achievements as provided
               - Certification names, issuing organizations, and dates

            2. **PERMISSIBLE OPTIMIZATIONS** (STRATEGIC ENHANCEMENTS):
               - Skills section reorganization by job relevance priority
               - Experience bullet point reordering for maximum impact
               - Project selection and emphasis based on job alignment
               - Language enhancement using job posting terminology
               - Section structure optimization for ATS compatibility

            3. **CONTENT ENHANCEMENT GUIDELINES**:
               - Rephrase existing content using job-aligned language without changing meaning
               - Emphasize documented skills that directly match job requirements
               - Highlight projects and technologies most relevant to target role
               - Reorganize information hierarchy to showcase strongest alignments first

            **QUALITY ASSURANCE FRAMEWORK**:
            - Verify every statement against original candidate materials
            - Ensure all technical claims are supported by documented evidence
            - Validate that all achievements use exact metrics provided by candidate
            - Confirm job requirement alignment without authenticity compromise
            - Document all optimization decisions for complete transparency

            **ATS OPTIMIZATION STANDARDS**:
            - Implement clean, scannable formatting structure
            - Integrate job posting keywords naturally within context
            - Optimize section headers and content organization
            - Ensure compatibility with standard ATS parsing systems
            - Maintain professional formatting that enhances readability
            """
        ),
        expected_output=(
            """**STRATEGICALLY OPTIMIZED PROFESSIONAL RESUME**

            # [CANDIDATE'S FULL NAME]
            [Complete contact information exactly as provided]
            [LinkedIn/Portfolio/GitHub links as available]

            ## 🎯 PROFESSIONAL SUMMARY
            [Strategic synthesis of candidate's experience, skills, and goals optimized for job requirements - using only documented background information to create compelling 3-4 line summary that positions candidate as ideal fit for target role]

            ## 🛠️ CORE TECHNICAL COMPETENCIES

            ### **[PRIMARY SKILL CATEGORY - JOB CRITICAL]**
            [Candidate's documented skills organized by job relevance, with evidence levels]
            • **[Skill 1]**: [Proficiency evidence] - [Context from candidate materials]
            • **[Skill 2]**: [Usage documentation] - [Application in projects/work]
            • **[Skill 3]**: [Implementation evidence] - [Specific usage context]

            ### **[SECONDARY SKILL CATEGORY - JOB RELEVANT]**
            [Additional verified skills that complement role requirements]
            • **[Skill 4]**: [Source documentation] - [Usage context]
            • **[Skill 5]**: [Evidence type] - [Application area]

            ### **[METHODOLOGIES & PRACTICES]**
            [Development approaches and practices candidate has demonstrated]
            • **[Methodology 1]**: [Evidence of application]
            • **[Practice 2]**: [Implementation context]

            ## 💼 PROFESSIONAL EXPERIENCE

            ### **[EXACT JOB TITLE]** | [EXACT COMPANY NAME] | [EXACT DATES]
            [Strategic role description emphasizing job-relevant aspects using enhanced language]

            **Impact & Achievements**:
            • [Achievement 1 with exact metrics, repositioned for job relevance using enhanced language]
            • [Responsibility highlighting transferable skills applicable to target role]
            • [Project/initiative demonstrating capabilities required for job, using job-aligned terminology]
            • [Technology implementation relevant to job requirements, with impact context]
            • [Leadership/collaboration evidence applicable to role requirements]

            **Key Technologies**: [Tech stack from this role, prioritized by job relevance]

            [Repeat optimized format for ALL employment positions]

            ## 🎓 EDUCATION & CERTIFICATIONS
            [Exactly as provided - NO MODIFICATIONS PERMITTED]

            **[DEGREE TYPE]** in [FIELD] | [INSTITUTION] | [GRADUATION DATE]
            [GPA, honors, relevant coursework exactly as provided]

            **Professional Certifications**:
            • **[Certification 1]**: [Issuing Organization] | [Date]
            • **[Certification 2]**: [Provider] | [Date]

            ## 📁 FEATURED TECHNICAL PROJECTS

            ### **[PROJECT NAME 1]** - [Relevance to Target Role: High/Medium]
            **Overview**: [Project description emphasizing job-applicable technologies and approaches]
            **Technologies**: [Tech stack highlighting job-required technologies first]
            **Key Implementations**: [Technical approaches demonstrating required capabilities]
            **Results**: [Outcomes as documented by candidate, presented with impact context]
            **Repository**: [GitHub link if applicable]

            ### **[PROJECT NAME 2]** - [Relevance Level]
            [Same detailed format optimized for additional high-relevance projects]

            ## 🚀 ADDITIONAL QUALIFICATIONS

            ### **Open Source & Community Involvement** (if applicable):
            [GitHub contributions and community activity relevant to role]

            ### **Professional Development** (if documented):
            [Learning initiatives and skill development mentioned by candidate]

            ### **Awards & Recognition** (if provided):
            [Exactly as documented in candidate materials]

            ---

            ## 📊 RESUME OPTIMIZATION INTELLIGENCE REPORT

            ### **Strategic Enhancements Applied**:

            #### **1. Content Architecture Optimization**:
            - **Section Prioritization**: [How information was reordered for maximum job relevance]
            - **Skills Hierarchy**: [Tier 1 job-critical skills emphasized first]
            - **Experience Emphasis**: [Most relevant responsibilities and achievements highlighted]
            - **Project Curation**: [Selection criteria for featured projects]

            #### **2. Keyword Integration Strategy**:
            - **Primary Keywords Integrated**: [Job posting terms naturally incorporated]
            - **Technical Language Alignment**: [How terminology matches job expectations]
            - **ATS Optimization**: [Specific formatting and keyword choices for ATS compatibility]
            - **Relevance Enhancement**: [Language improvements made for job fit]

            #### **3. Achievement Amplification Techniques**:
            - **Impact Positioning**: [How documented achievements were repositioned for maximum relevance]
            - **Metric Emphasis**: [Quantified results highlighted using job-relevant context]
            - **Value Proposition**: [How candidate's accomplishments demonstrate target role capabilities]

            #### **4. Experience Narrative Enhancement**:
            - **Responsibility Reframing**: [How duties were repositioned to align with job requirements]
            - **Technology Emphasis**: [Which technical skills were prioritized and why]
            - **Transferable Skills**: [How experience translates to target role success]

            ### **Authenticity Verification Matrix**:
            ✅ **Educational Information**: Preserved exactly as provided
            ✅ **Employment History**: Dates, titles, companies unchanged
            ✅ **Quantified Achievements**: All metrics maintained as candidate provided
            ✅ **Technical Skills**: Only documented capabilities included
            ✅ **Project Information**: Only verified projects featured
            ✅ **Contact Information**: Maintained exactly as provided
            ✅ **Source Traceability**: Every claim traceable to original materials

            ### **Job Alignment Assessment**:

            #### **Strong Alignment Areas** (90-100% Match):
            - **[Requirement Area 1]**: [How candidate's documented experience strongly aligns]
            - **[Requirement Area 2]**: [Specific evidence of capability match]

            #### **Good Alignment Areas** (70-89% Match):
            - **[Requirement Area 3]**: [Where candidate has relevant but not exact experience]
            - **[Requirement Area 4]**: [Transferable skills application]

            #### **Development Opportunities** (Areas for Growth):
            - **[Skill/Experience Gap]**: [Job requirement not fully evidenced in candidate materials]
            - **[Learning Area]**: [Skills mentioned in job posting for future development]

            #### **Competitive Advantages** (Unique Strengths):
            - **[Distinctive Capability 1]**: [What sets candidate apart beyond basic requirements]
            - **[Unique Experience]**: [Uncommon background elements that add value]

            ### **Strategic Recommendations**:
            - **Interview Focus Areas**: [Experiences candidate should emphasize in interviews]
            - **Skill Development**: [Areas for continued learning based on job requirements]
            - **Portfolio Enhancements**: [Suggested project additions for stronger alignment]

            **FINAL AUTHENTICITY STATEMENT**: This optimized resume represents a strategic enhancement of the candidate's documented experience, skills, and achievements. Every statement, metric, and claim is directly sourced from candidate-provided materials. No fictional content, inflated achievements, or unsubstantiated claims have been added. All optimization decisions maintain complete transparency and source traceability.**"""
        ),
        output_file= "tailored_resume.md",
        context=[research_task, profile_task],
        agent = resume_strategist
    )

    #Task 4: Master Interview Preparation & Strategic Positioning
    interview_preparation_task = Task(
        description=(
            """CREATE COMPREHENSIVE EVIDENCE-BASED INTERVIEW PREPARATION FRAMEWORK

            **PRIMARY MISSION**: Develop an exhaustive interview preparation strategy that positions the candidate optimally using only documented experiences, achievements, and skills to demonstrate perfect job-role alignment.

            **STRATEGIC PREPARATION ARCHITECTURE**:

            1. **PRECISION QUESTION PREDICTION & PREPARATION**:
               - Analyze job requirements to predict specific technical questions likely to be asked
               - Map behavioral competencies from job posting to relevant STAR story frameworks
               - Anticipate company culture and role-specific scenario questions
               - Prepare responses using candidate's documented experiences and actual project examples

            2. **EVIDENCE-BASED RESPONSE DEVELOPMENT**:
               - Create compelling technical discussion points grounded in candidate's GitHub projects
               - Develop behavioral story bank using candidate's documented achievements and experiences
               - Build confidence-enhancing talking points around candidate's verified strengths
               - Prepare authentic examples that directly address job requirements

            3. **STRATEGIC POSITIONING & DIFFERENTIATION**:
               - Identify candidate's unique value propositions based on documented experience combinations
               - Develop authentic responses for addressing skill gaps honestly while emphasizing growth mindset
               - Create memorable achievement narratives using candidate's quantified results
               - Position candidate's learning trajectory as evidence of adaptability and growth potential

            4. **COMPREHENSIVE SCENARIO PLANNING**:
               - Technical deep-dive preparation for discussing candidate's actual code and projects
               - Behavioral interview mastery using real examples from candidate's professional experience
               - Company research integration with candidate's stated career goals and interests
               - Salary discussion framework based on candidate's experience level and market positioning

            **CRITICAL AUTHENTICITY PROTOCOLS**:
            - Use ONLY candidate's documented experiences, projects, and achievements
            - Reference ONLY technologies, skills, and accomplishments the candidate has actually demonstrated
            - Base all examples on candidate's real background and verified experiences
            - Never suggest discussing experiences, skills, or achievements not evidenced in candidate materials
            - Maintain complete transparency about preparation recommendations and their evidence sources

            **STRATEGIC DIFFERENTIATION FRAMEWORK**:
            - Leverage candidate's unique skill combinations and experience patterns
            - Highlight documented innovations, creative solutions, and problem-solving approaches
            - Emphasize authentic career progression and learning demonstrated in candidate's background
            - Position candidate's documented achievements as indicators of future performance potential
            """
        ),
        expected_output=(
            """**COMPREHENSIVE INTERVIEW MASTERY PREPARATION GUIDE**

            ## 🎯 INTERVIEW STRATEGIC OVERVIEW
            **Target Position**: [Exact job title from posting]
            **Company**: [Organization name]
            **Interview Focus Themes**: [Key areas based on job requirements and candidate strengths]
            **Positioning Strategy**: [How to present candidate as ideal fit using documented background]

            ## 💻 TECHNICAL INTERVIEW PREPARATION

            ### **Core Technical Competency Questions**

            #### **[PRIMARY TECHNICAL AREA - HIGH PROBABILITY]**
            **Anticipated Question**: "[Specific technical question based on job requirements]"
            **Response Strategy**: [How to answer using candidate's documented experience]
            **Evidence to Share**: [Specific project/code example from candidate's GitHub]
            **Key Points to Emphasize**: [Technical depth demonstrated in candidate's work]
            **Follow-up Preparedness**: [Additional details candidate can discuss about implementation]

            #### **[SECONDARY TECHNICAL AREA - MEDIUM PROBABILITY]**
            **Anticipated Question**: "[Technical question related to job requirements]"
            **Authentic Response Approach**: [Framework using candidate's actual experience]
            **Project Reference**: [Specific repository or work project demonstrating skill]
            **Technical Details Ready**: [Code architecture, challenges solved, technologies used]

            [Continue with 8-10 technical questions mapped to job requirements]

            ### **System Design & Architecture Discussion**
            **Scenario**: "[Design question likely based on role responsibilities]"
            **Preparation Strategy**: [Using candidate's documented architectural decisions]
            **Reference Projects**: [Specific examples from candidate's portfolio]
            **Technical Approach**: [How to walk through design thinking using real examples]

            ### **Code Review & Technical Deep-Dive Readiness**
            **Repository Focus**: [2-3 best repositories for potential code discussion]
            #### **[Featured Repository 1]**:
            - **Core Functionality**: [What it does and why it was built]
            - **Technical Challenges**: [Problems solved and approaches taken]
            - **Technology Decisions**: [Why specific technologies were chosen]
            - **Code Organization**: [Architecture and design patterns used]
            - **Potential Discussion Points**: [Areas interviewer might explore]

            ## 🗣️ BEHAVIORAL INTERVIEW MASTERY

            ### **Leadership & Initiative** (If relevant to role)
            **Likely Question**: "Tell me about a time when you led a project or took initiative"
            **STAR Response Framework**:
            - **Situation**: [Specific context from candidate's documented experience]
            - **Task**: [Actual responsibility candidate had]
            - **Action**: [Specific actions candidate took, using documented details]
            - **Result**: [Actual outcome with candidate's exact metrics/achievements]
            **Key Message**: [What this demonstrates about candidate's capabilities for target role]

            ### **Problem-Solving & Innovation**
            **Likely Question**: "Describe a challenging technical problem you solved"
            **Authentic Example**: [Using candidate's documented project challenges]
            **Technical Story Arc**: [Problem → Analysis → Solution → Implementation → Results]
            **Evidence References**: [Code, documentation, or project outcomes candidate can reference]

            ### **Collaboration & Teamwork**
            **Likely Question**: "How do you handle working with cross-functional teams?"
            **Experience-Based Response**: [Using candidate's documented team experiences]
            **Specific Examples**: [Actual collaboration scenarios from candidate's background]

            ### **Learning & Adaptability**
            **Likely Question**: "Tell me about a time you had to learn a new technology quickly"
            **Real Learning Journey**: [Documented skill development from candidate's timeline]
            **Specific Example**: [Actual technology adoption story from candidate's experience]

            [Continue with 8-10 behavioral scenarios using candidate's documented experiences]

            ## 🏢 COMPANY & ROLE-SPECIFIC PREPARATION

            ### **Role Understanding & Motivation**
            **Question**: "Why are you interested in this specific role?"
            **Authentic Response**: [Connecting job requirements to candidate's documented career goals]
            **Specific Alignment**: [How role matches candidate's stated objectives and experience]

            ### **Company Culture & Values Alignment**
            **Research-Based Talking Points**: [Company information from job posting]
            **Personal Alignment**: [How candidate's stated values and goals match company culture]

            ### **Technical Challenge Discussion**
            **Role-Specific Scenarios**: [Technical challenges likely faced in position]
            **Preparation Approach**: [How candidate's experience prepares them for these challenges]

            ## 🤔 STRATEGIC QUESTIONS FOR INTERVIEWER

            ### **Role & Team Dynamics**:
            1. "[Thoughtful question about day-to-day responsibilities based on job posting]"
            2. "[Question about team structure that shows candidate's collaboration interest]"
            3. "[Growth and development question aligned with candidate's stated career goals]"

            ### **Technical Environment**:
            1. "[Question about technology stack showing candidate's technical curiosity]"
            2. "[Question about technical challenges specific to role/company]"
            3. "[Question about code review, testing, or development practices]"

            ### **Growth & Development**:
            1. "[Question about learning opportunities that aligns with candidate's growth interests]"
            2. "[Question about mentorship or knowledge sharing culture]"

            ## 📖 KEY TALKING POINTS & ACHIEVEMENT HIGHLIGHTS

            ### **Signature Project Narratives**:

            #### **[Candidate's Most Relevant Project]**:
            - **Elevator Pitch**: [30-second compelling description]
            - **Technical Deep-Dive Ready**: [Detailed implementation discussion prep]
            - **Challenge & Solution**: [Problem solved and approach taken]
            - **Impact & Results**: [Outcomes achieved using candidate's documentation]
            - **Relevance to Role**: [Direct connection to job requirements]

            #### **[Secondary Strong Project]**:
            [Same structure for additional high-impact projects]

            ### **Professional Achievement Stories**:
            - **[Achievement 1]**: [Documented accomplishment with context and metrics]
            - **[Achievement 2]**: [Another significant achievement from candidate's background]
            - **[Learning Success]**: [Growth or skill development story from candidate's experience]

            ## 🎪 AUTHENTIC POSITIONING STRATEGIES

            ### **Unique Value Proposition**:
            - **Core Strength 1**: [Based on candidate's documented expertise]
            - **Distinctive Experience**: [Unique combination of skills/background]
            - **Problem-Solving Approach**: [Demonstrated through candidate's projects]

            ### **Growth Mindset Demonstration**:
            - **Learning Trajectory**: [Documented skill development over time]
            - **Adaptation Examples**: [Times candidate successfully learned new technologies]
            - **Future Development**: [Areas candidate wants to grow, aligned with role]

            ### **Honest Gap Management**:
            #### **[Skill mentioned in job posting but not fully demonstrated]**:
            **Honest Response**: "I haven't worked extensively with [technology], but I have significant experience with [related technology from candidate's background]. Based on my track record of quickly mastering [specific examples], I'm confident I can become productive with [new technology] rapidly."
            **Evidence**: [Specific examples of candidate's learning agility]

            ## 📅 INTERVIEW PREPARATION TIMELINE

            ### **1 Week Before Interview**:
            - [ ] Review all featured projects and practice explaining technical decisions
            - [ ] Practice STAR method responses using documented experiences
            - [ ] Prepare specific metrics and outcomes from verified achievements
            - [ ] Research company culture and role context from job posting

            ### **2-3 Days Before Interview**:
            - [ ] Conduct mock technical discussions of key projects
            - [ ] Practice behavioral stories using real examples
            - [ ] Prepare thoughtful questions about role and company
            - [ ] Review salary discussion framework

            ### **Day of Interview**:
            - [ ] Review key project repositories and be ready for code discussion
            - [ ] Have specific achievement examples and metrics ready
            - [ ] Focus on authentic enthusiasm for role based on career goals
            - [ ] Prepare to discuss learning objectives aligned with role growth

            ## 🎯 CONFIDENCE-BUILDING FRAMEWORK

            ### **Evidence-Based Confidence**:
            - **Technical Competence**: [Documented through actual projects and code]
            - **Achievement History**: [Track record of success using verified accomplishments]
            - **Learning Ability**: [Demonstrated through documented skill development]
            - **Problem-Solving**: [Evidenced through project challenges overcome]

            ### **Authenticity as Strength**:
            - **Genuine Interest**: [Based on candidate's stated career goals]
            - **Real Experience**: [All examples grounded in documented background]
            - **Growth Mindset**: [Evidenced through candidate's learning trajectory]

            ## 📊 INTERVIEW SUCCESS METRICS

            ### **Preparation Completeness Checklist**:
            - [ ] Technical questions prepared with real project examples
            - [ ] Behavioral stories ready using documented experiences
            - [ ] Company research completed and connected to personal goals
            - [ ] Questions for interviewer prepared and relevant
            - [ ] Gap management strategies ready with honest, growth-oriented responses

            ### **Post-Interview Follow-up Strategy**:
            - **Thank You Note**: [Template acknowledging specific discussion points]
            - **Additional Information**: [Relevant project details or examples mentioned in interview]
            - **Continued Interest**: [Reinforcement of authentic enthusiasm for role]

            **AUTHENTICITY COMMITMENT**: Every example, story, and talking point in this preparation guide is derived exclusively from the candidate's documented experiences, achievements, and background. No fictional scenarios, inflated capabilities, or unsubstantiated claims have been included. All preparation recommendations maintain complete transparency and can be traced to original candidate materials.**"""
        ),
        output_file= "interview_preparation.md",
        context= [
            research_task,
            profile_task,
            resume_strategy_task
        ],
        agent = interview_preparer
    )

    return research_task, profile_task, resume_strategy_task, interview_preparation_task