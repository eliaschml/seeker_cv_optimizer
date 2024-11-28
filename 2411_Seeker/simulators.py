# this file holds all simulation functions used before
# setting up a real DB
import random
#%% create random ID
def gen_id(): return random.randint(1000,2000)

#%% simulate extacted content
def gen_content(): 
    content =  '''**Personal information**
        - Name: Elias Chemali
        - Date of Birth: 1993-09-20
        - Nationality: Lebanese/Mexican
        - Address: 23-11, World Cup buk-ro 9-gil, Mapo-gu, Seoul, Republic of Korea
        - Email: eliaschml@gmail.com
        - Phone: +82 010-44439676


        **Professional Experience**
        - Hyperconnect (Match Group Inc.) - Business Planning Manager (Hakuna) Seoul, Korea Sep ‘22 — Sep ‘24
            - Developed annual plan and performance tracking framework overachieving revenue targets
            - Developed and executed annual business plans aligning with corporate strategy, consistently exceeding revenue targets
            - Collaborated with major stakeholders to develop annual business strategies and set yearly business KPIs
            - Refined strategy and business plan through thorough competitor and market trend research
            - Created a financial forecast model to drive effective decision making and manage business performance
            - Translated corporate strategy into clear business actions and developed KPI tracking framework
            - Optimized project execution through cross-functional collaboration, meeting evolving business needs
            - Restructured monetization policies reducing revenue leakage by 25% with minimal impact on revenue
            - Optimized business operations and product features, maximizing Hakuna’s gross profit margin
            - Developed and managed a business intelligence framework, delivering 300+ reports, dashboards, and queries. Provided crucial findings allowing for informed and accurate business decision making
            - Analyzed user behavior and shared actionable insights to improve business and product initiative impact
        - Hyperconnect (Match Group Inc.) – Regional Marketing Manager Nov ’20 - Sep ‘22
            - Led MENA unit business improving competitiveness through video focused creator acquisition initiative
            - Improved user acquisition process covering digital and organic channels within set budgets
            - Owned and led the end-to-end process of MENA user acquisition for Hakuna
            - Managed creator acquisition initiative, improving recruited creator revenue by 165% in 3 months
            - Partnered with local creator agencies improving recruited creator revenue by 165% in 3 months
            - Designed creative pipeline increasing production to over 30 creatives/month and improving CTR by 40%
            - Collaborated with the creative team increasing output to 30 creatives/month and improving CTR by 40%
        - Seoul National University, Acoustics and Vibrations Lab - Assistant Researcher Seoul, Korea Aug ‘19 — Jul ‘20
            - Led a research project in Optimal Sensor Placement for Active Road Noise Control
            - Achieved a 90%- time reduction on algorithm run-time through signal pre-processing and elimination
            - Developed an algorithm to reconstruct felt fiber micro-structure from x-ray microtomography images
        - Hyundai Motors – Academic Researcher Seoul, Korea May ‘18 — Aug ‘19
            - Led a 1-year project in collaboration with Hyundai Motors at the SNU Acoustics and Vibrations Lab
            - Modeled the human response to various vibro-acoustic environments and stimuli through data analysis
            - Overcame data limitations through process design for modeling human response to armrest vibrations
        - Bildits (Educational Construction Kit Company)- Start-up Co-founder Beirut, Lebanon Mar '16 — Aug ‘16
            - Pitched value proposition and business plan to investors, securing first 20,000$ in initial investments
            - Advised Bildits directors on product design and updates until Bildits was acquired by external investors
            -Founded Bildits and continue to advise Bildits acquiring company on biz ops and business intelligence


        **Education**

        - Seoul National University-Mechanical & Aerospace Engineering Department Seoul, Korea Sep ‘17 - Aug ‘19
            - Masters’s Degree in Mechanical Engineering (Korean Government Scholarship Program)
            - Specialized in Acoustics and Vibrations at the SNU Acoustics and Vibrations Laboratory
            - Improved the vibro-acoustic performance of automotive structural systems
            - Focused on the modeling of human response to sound and vibrations (psychophysics)
        - Lebanese American University - Industrial and Mechanical Engineering Department Byblos, Lebanon Sep 11 — Jun ‘16
            - Bachelor of Engineering in Mechanical Engineering
            -Reduced the load of an Exoskeleton for paraplegic persons by 50%, through design improvements
        - Politecnico di Torino - Mechanical Engineering Department
            - Exchange Student for One Semester (Erasmus Mundus Scholarship) Sep 13 — Feb ‘14
            - Designed a Fiat gearbox that conforms with industrial standards using Solidworks


        **Other**
        **Skills**
        - Experience with Python, Bigquery SQL, Jira and dashboard tools (Tableau, Looker Studio)

        **Languages**
        - Arabic (Native)
        - French (Native)
        - English (Native)
        -Korean (Fluent)
        - Italian (Conversational)

        ** Papers**
        - Co-authored a paper to model the acoustic properties of felt using Al featured in JASA

        **Music**
        - Guitar player (15 years)
        - Partner and producer at “textures.seoul” (released 2 tracks on major streaming platforms)

        **Additional**
        - Keen traveler: Lived in three different countries, traveled and organized trips to more than 15 countries
        - Extra-curricular: Chosen to represent Lebanon in the Global Model UN conference in Philadelphia
        - Social Engagement: Chef de Troupe at the Boy Scouts of Lebanon, organized social activities for scouts between 12-25
        '''
    return content

# retrieve target content from db
def retrieve_record():
    return gen_content()