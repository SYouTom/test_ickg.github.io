import os

# 1. Create the folder
folder_name = "ickg2026_website"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 2. Define the CSS
css_content = """
:root {
    --primary-color: #0056b3;
    --secondary-color: #333;
    --bg-light: #f9f9f9;
    --text-color: #444;
    --accent-color: #e74c3c;
}
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0; padding: 0; color: var(--text-color); line-height: 1.6;
    display: flex; flex-direction: column; min-height: 100vh;
}
header {
    background-color: var(--primary-color); color: white; padding: 4rem 0; text-align: center;
    background-image: linear-gradient(rgba(0, 40, 85, 0.7), rgba(0, 40, 85, 0.8)), url('banner.jpg');
    background-size: cover; background-position: center;
}
header h1 { margin: 0; font-size: 3rem; letter-spacing: 1px; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
header h2 { margin: 10px 0 0; font-weight: 400; font-size: 1.5rem; opacity: 0.95; text-shadow: 1px 1px 3px rgba(0,0,0,0.5); }

/* NAVIGATION & DROPDOWN */
nav { background: #2c3e50; position: sticky; top: 0; z-index: 1000; }
nav ul { list-style: none; padding: 0; margin: 0; display: flex; justify-content: center; flex-wrap: wrap; }
nav ul li { position: relative; }
nav ul li a { 
    display: block; padding: 15px 25px; color: white; text-decoration: none; 
    font-weight: 600; transition: background 0.3s; text-transform: uppercase; font-size: 0.9rem; 
}
nav ul li a:hover, nav ul li a.active { background: #34495e; border-bottom: 4px solid var(--accent-color); }

.dropdown-content {
    display: none; position: absolute; background-color: #2c3e50;
    min-width: 220px; box-shadow: 0 8px 16px rgba(0,0,0,0.2); z-index: 1001; top: 100%; left: 0; text-align: left;
}
.dropdown-content li { width: 100%; }
.dropdown-content li a { padding: 12px 20px; text-transform: none; border-bottom: 1px solid #34495e; font-size: 0.95rem; }
.dropdown-content li a:hover { background-color: #3e5871; }
nav ul li:hover .dropdown-content { display: block; }

/* LAYOUT */
.container { display: flex; flex-wrap: wrap; max-width: 1200px; margin: 40px auto; padding: 0 20px; gap: 40px; flex: 1; }
.main-content { flex: 3; min-width: 60%; }
.sidebar { flex: 1; min-width: 250px; }
h2.section-title { color: var(--primary-color); border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 0; }
h3 { color: var(--secondary-color); margin-top: 25px; }
ul.topic-list { padding-left: 20px; margin-bottom: 20px; }
ul.topic-list li { margin-bottom: 8px; }
.sidebar-box { background: var(--bg-light); padding: 25px; border-radius: 8px; border: 1px solid #eee; margin-bottom: 30px; }
.sidebar-box h3 { color: var(--primary-color); margin-top: 0; border-bottom: 1px solid #ddd; padding-bottom: 10px; }
.date-item { margin-bottom: 15px; display: flex; justify-content: space-between; }
.date-value { color: var(--accent-color); font-weight: 700; }
footer { background: #2c3e50; color: #ccc; text-align: center; padding: 30px 20px; margin-top: auto; }

/* ORGANIZER LOGOS */
.organizer-section { margin-top: 40px; border-top: 2px solid #eee; padding-top: 20px; }
.organizer-logos { display: flex; gap: 30px; align-items: center; flex-wrap: wrap; }
.organizer-logo-link { display: block; border: 1px solid #ddd; padding: 10px; border-radius: 5px; transition: transform 0.2s; background: white; }
.organizer-logo-link:hover { transform: scale(1.05); border-color: var(--primary-color); }
.organizer-img { height: 60px; width: auto; display: block; }

/* COMMITTEE MEMBER STYLES */
.committee-group { margin-bottom: 40px; }
.committee-role-title { 
    font-size: 1.3rem; font-weight: bold; color: var(--secondary-color); 
    border-left: 5px solid var(--primary-color); padding-left: 15px; margin-bottom: 20px; background: #f0f4f8; padding: 10px 15px;
}
.member-grid { display: flex; flex-wrap: wrap; gap: 25px; }
.member-card { 
    display: flex; align-items: center; gap: 20px; width: 100%; max-width: 480px; 
    background: white; border: 1px solid #eee; padding: 20px; border-radius: 8px; 
    box-shadow: 0 2px 5px rgba(0,0,0,0.05); transition: transform 0.2s;
}
.member-card:hover { transform: translateY(-3px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); border-color: var(--primary-color); }
.member-photo { 
    width: 90px; height: 90px; border-radius: 50%; object-fit: cover; 
    border: 3px solid #eef; background-color: #ddd; flex-shrink: 0;
}
.member-info { display: flex; flex-direction: column; }
.member-name { font-size: 1.15rem; font-weight: bold; color: var(--primary-color); text-decoration: none; margin-bottom: 5px; }
.member-name:hover { text-decoration: underline; }
.member-affil { font-size: 0.95rem; color: #555; font-style: italic; }
"""

# 3. Define Common HTML Components
header_html = """
    <header>
        <div style="max-width: 1200px; margin: 0 auto;">
            <h1>ICKG 2026</h1>
            <h2>The 17th IEEE International Conference on Knowledge Graphs</h2>
            <p style="font-size: 1.2rem; margin-top: 15px; font-weight: 500;">November 12-13, 2026 | Shenyang, China</p>
        </div>
    </header>
"""
sidebar_html = """
        <aside class="sidebar">
            <div class="sidebar-box">
                <h3>Important Dates</h3>
                <p style="font-size:0.9rem; color:#666; margin-top:-10px; margin-bottom:15px; font-style:italic;">(All deadlines are AOE)</p>
                <div class="date-item"><span>Paper Submission:</span><span class="date-value">Jun 19, 2026</span></div>
                <div class="date-item"><span>Notification:</span><span class="date-value">Aug 31, 2026</span></div>
                <div class="date-item"><span>Camera-Ready:</span><span class="date-value">Sep 18, 2026</span></div>
                <div class="date-item"><span>Conference:</span><span class="date-value">Nov 12-13, 2026</span></div>
            </div>
            <div class="sidebar-box">
                <h3>Latest News</h3>
                <p><strong>Nov 2025:</strong> Website launched. Preparation for ICKG 2026 in Shenyang has begun.</p>
            </div>
        </aside>
"""
footer_html = """
    <footer>
        <p>&copy; 2026 ICKG. All Rights Reserved.</p>
        <p>Organized by IEEE Computer Society & Local Committee</p>
    </footer>
</body></html>
"""

def get_page(title, active_link, content):
    def active(link): return ' class="active"' if link == active_link else ''
    prog_active = ' class="active"' if active_link in ['program.html', 'keynote-speakers.html', 'schedule.html'] else ''
    
    nav_html = f"""
    <nav>
        <ul>
            <li><a href="index.html"{active('index.html')}>Home</a></li>
            <li><a href="call-for-papers.html"{active('call-for-papers.html')}>Call for Papers</a></li>
            <li class="dropdown">
                <a href="program.html"{prog_active}>Program &#9662;</a>
                <ul class="dropdown-content">
                    <li><a href="program.html">Program Overview</a></li>
                    <li><a href="keynote-speakers.html">Keynote Speakers</a></li>
                    <li><a href="schedule.html">Schedule</a></li>
                </ul>
            </li>
            <li><a href="organization.html"{active('organization.html')}>Organization</a></li>
            <li><a href="registration.html"{active('registration.html')}>Registration</a></li>
            <li><a href="venue.html"{active('venue.html')}>Venue</a></li>
        </ul>
    </nav>
    """
    
    # Logic to remove sidebar for Organization, Registration, AND all Program pages
    full_width_pages = [
        'organization.html', 
        'registration.html', 
        'program.html', 
        'keynote-speakers.html', 
        'schedule.html'
    ]
    is_full_width = active_link in full_width_pages
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - ICKG 2026</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {header_html} {nav_html}
    <div class="container">
        <div class="main-content" style="{ 'width:100%;' if is_full_width else '' }">
            {content}
        </div>
        { '' if is_full_width else sidebar_html }
    </div>
    {footer_html}
"""

# --- PAGE CONTENT ---

# Home
content_home = """
    <h2 class="section-title">Welcome to ICKG 2026</h2>
    
    <p>The annual IEEE International Conference on Knowledge Graph (ICKG) provides a premier international forum for presentation of original research results in knowledge discovery and graph learning, discussion of opportunities and challenges, as well as exchange and dissemination of innovative, practical development experiences. The conference covers all aspects of knowledge discovery from data, with a strong focus on graph learning and knowledge graph, including algorithms, software, platforms.</p>
    
    <p>ICKG 2026 will be held in <strong>Shenyang, China</strong> on <strong>November 12-13, 2026</strong>. We invite researchers and practitioners to submit their latest work and join us for this exciting event.</p>

    <div class="organizer-section">
        <h3 style="margin-top:0; margin-bottom:20px; color:#555;">Organized By</h3>
        <div class="organizer-logos">
             <a href="https://www.ieee.org/" target="_blank" class="organizer-logo-link" title="IEEE">
                <img src="logo_ieee.png" alt="IEEE Logo" class="organizer-img" onerror="this.style.display='none';this.parentElement.innerHTML='<b>IEEE</b>'">
            </a>
            <a href="https://lab.zhonghuapu.com/" target="_blank" class="organizer-logo-link" title="BigKE Lab">
                <img src="logo_bigke.png" alt="BigKE Lab Logo" class="organizer-img" onerror="this.style.display='none';this.parentElement.innerHTML='<b>BigKE Lab</b>'">
            </a>
            <a href="https://www.wnmc.edu.cn/" target="_blank" class="organizer-logo-link" title="Wannan Medical College">
                <img src="logo_wnmc.png" alt="Wannan Medical College Logo" class="organizer-img" onerror="this.style.display='none';this.parentElement.innerHTML='<b>Wannan Medical College</b>'">
            </a>
        </div>
    </div>
"""

# Call for Papers
content_cfp = """
    <h2 class="section-title">Call for Papers</h2>
    
    <p>The annual IEEE International Conference on Knowledge Graph (ICKG) provides a premier international forum for presentation of original research results in knowledge discovery and graph learning, discussion of opportunities and challenges, as well as exchange and dissemination of innovative, practical development experiences. The conference covers all aspects of knowledge discovery from data, with a strong focus on graph learning and knowledge graph, including algorithms, software, platforms.</p>
    
    <p>ICKG 2026 intends to draw researchers and application developers from a wide range of areas such as knowledge engineering, representation learning, big data analytics, statistics, machine learning, pattern recognition, data mining, knowledge visualization, high performance computing, and World Wide Web etc. By promoting novel, high quality research findings, and innovative solutions to address challenges in handling all aspects of learning from data with dependency relationship.</p>
    
    <p>All accepted papers will be published in the conference proceedings by the IEEE Computer Society.</p>
    
    <p><strong>Awards</strong>, including Best Paper, Best Paper Runner up, Best Student Paper, Best Student Paper Runner up, will be conferred at the conference, with a check and a certificate for each award.</p>
    
    <p>The conference also features a <strong>survey track</strong> to accept survey papers reviewing recent studies in all aspects of knowledge discovery and graph learning.</p>

    <h3>Topics of Interest</h3>
    <p>Topics of interest include, but are not limited to:</p>
    <ul class="topic-list">
        <li>Foundations, algorithms, models, and theory of knowledge discovery and graph learning</li>
        <li>Knowledge engineering with big data</li>
        <li>Machine learning, data mining, and statistical methods for data science and engineering</li>
        <li>Acquisition, representation and evolution of fragmented knowledge</li>
        <li>Fragmented knowledge modeling and online learning</li>
        <li>Knowledge graphs and knowledge maps</li>
        <li>Graph learning security, privacy, fairness, and trust</li>
        <li>Interpretation, rule, and relationship discovery in graph learning</li>
        <li>Geospatial and temporal knowledge discovery and graph learning</li>
        <li>Ontologies and reasoning</li>
        <li>Topology and fusion on fragmented knowledge</li>
        <li>Visualization, personalization, and recommendation of Knowledge Graph navigation and interaction</li>
        <li>Knowledge Graph systems and platforms, and their efficiency, scalability, and privacy</li>
        <li>Applications and services of knowledge discovery and graph learning in all domains including web, medicine, education, healthcare, and business</li>
        <li>Big knowledge systems and applications</li>
        <li>Crowdsourcing, deep learning and edge computing for graph mining</li>
        <li>Large language models and applications</li>
        <li>Open source platforms and systems supporting knowledge and graph learning</li>
        <li>Datasets and benchmarks for graphs</li>
        <li>Neurosymbolic & Hybrid AI systems</li>
        <li>Graph Retrieval Augmented Generation</li>
        <li><strong>Survey Track:</strong> Survey paper reviewing recent study in key aspects of knowledge discovery and graph learning.</li>
    </ul>

    <h3>Special Track Topics</h3>
    <p>Each special track is handled by respective special track chairs, and the papers are also included in the conference proceedings.</p>
    <ul class="topic-list">
        <li><strong>Special Track 01:</strong> KGC and Knowledge Graph Building</li>
        <li><strong>Special Track 02:</strong> KR and KG Reasoning</li>
        <li><strong>Special Track 03:</strong> KG and Large Language Model</li>
        <li><strong>Special Track 04:</strong> GNN and Graph Learning</li>
        <li><strong>Special Track 05:</strong> QA and Graph Database</li>
        <li><strong>Special Track 06:</strong> KG and Multi-modal Learning</li>
        <li><strong>Special Track 07:</strong> KG and Knowledge Fusion</li>
        <li><strong>Special Track 08:</strong> Industry and Applications</li>
    </ul>

    <h3>Submission Guidelines</h3>
    <p>Paper submissions should be no longer than <strong>8 pages</strong>, in the <a href="https://www.ieee.org/conferences/publishing/templates.html" target="_blank">IEEE 2-column format</a>, including the bibliography and any possible appendices. Submissions longer than 8 pages will be rejected without review. All submissions will be reviewed by the Program Committee based on technical quality, originality, significance, and clarity.</p>
    
    <p><strong>For Survey Track Papers:</strong> Please preface the descriptive paper title with “<strong>Survey:</strong>”, followed by the actual paper title. For example, a paper entitled “A Literature Review of Streaming Knowledge Graph”, should be changed as “Survey: A Literature Review of Streaming Knowledge Graph”. This is for the reviewers and chairs to clearly bid and handle the papers. Once the paper is accepted, the word, such as “Survey:”, can be removed from the camera-ready copy.</p>

    <p><strong>For Special Track Papers:</strong> Please preface the descriptive paper title with “<strong>SS##:</strong>”, where “##” is the two digits special track ID. For example, a paper entitled “Incremental Knowledge Graph Learning”, intended to target Special Track 01 (Machine learning and knowledge graph) should be changed as “SS01: Incremental Knowledge Graph Learning”.</p>

    <p>All manuscripts are submitted as full papers and are reviewed based on their scientific merit. The reviewing process is <strong>single blind</strong>, meaning that each submission should list all authors and affiliations. There is no separate abstract submission step. There are no separate industrial, application, or poster tracks. Manuscripts must be submitted electronically in the online submission system. No email submission is accepted.</p>
"""

# Organization
content_org = """
    <h2 class="section-title">Organizing Committee</h2>

    <div class="committee-group">
        <div class="committee-role-title">General Co-Chairs</div>
        <div class="member-grid">
            <div class="member-card">
                <img src="photo_shirui.jpg" alt="Shirui Pan" class="member-photo" onerror="this.src='https://via.placeholder.com/150?text=Photo'">
                <div class="member-info">
                    <a href="https://experts.griffith.edu.au/37935-shirui-pan" target="_blank" class="member-name">Shirui Pan</a>
                    <span class="member-affil">Griffith University, Australia</span>
                </div>
            </div>
            <div class="member-card">
                <img src="photo_steffen.jpg" alt="Steffen Staab" class="member-photo" onerror="this.src='https://via.placeholder.com/150?text=Photo'">
                <div class="member-info">
                    <a href="https://scholar.google.com/citations?user=QvpcUn8AAAAJ&hl=en" target="_blank" class="member-name">Steffen Staab</a>
                    <span class="member-affil">University of Stuttgart, Germany</span>
                </div>
            </div>
        </div>
    </div>

    <div class="committee-group">
        <div class="committee-role-title">Program Co-Chairs</div>
        <div class="member-grid">
            <div class="member-card">
                <img src="photo_chuan.jpg" alt="Chuan Shi" class="member-photo" onerror="this.src='https://via.placeholder.com/150?text=Photo'">
                <div class="member-info">
                    <a href="https://scholar.google.com/citations?user=tUq_v90AAAAJ&hl=en" target="_blank" class="member-name">Chuan Shi</a>
                    <span class="member-affil">Beijing University of Posts and Telecommunications, China</span>
                </div>
            </div>
        </div>
    </div>

    <div class="committee-group">
        <div class="committee-role-title">Finance Chair</div>
        <div class="member-grid">
            <div class="member-card">
                <img src="photo_rocky.jpg" alt="Rocky Chen" class="member-photo" onerror="this.src='https://via.placeholder.com/150?text=Photo'">
                <div class="member-info">
                    <a href="https://scholar.google.com/citations?user=07cqSMsAAAAJ&hl=en" target="_blank" class="member-name">Rocky Chen</a>
                    <span class="member-affil">The University of Queensland, Australia</span>
                </div>
            </div>
        </div>
    </div>

    <div class="committee-group">
        <div class="committee-role-title">Local Arrangements Chair</div>
        <div class="member-grid">
            <div class="member-card">
                <img src="photo_mingquan.jpg" alt="Mingquan Ye" class="member-photo" onerror="this.src='https://via.placeholder.com/150?text=Photo'">
                <div class="member-info">
                    <a href="https://yxxxxy.wnmc.edu.cn/info/1009/4711.htm" target="_blank" class="member-name">Mingquan Ye</a>
                    <span class="member-affil">Wannan Medical College, China</span>
                </div>
            </div>
        </div>
    </div>

    <div class="committee-group">
        <div class="committee-role-title">Steering Committee Chair</div>
        <div class="member-grid">
            <div class="member-card">
                <img src="photo_xindong.jpg" alt="Xindong Wu" class="member-photo" onerror="this.src='https://via.placeholder.com/150?text=Photo'">
                <div class="member-info">
                    <a href="https://xwu.zhonghuapu.com/" target="_blank" class="member-name">Xindong Wu</a>
                    <span class="member-affil">Hefei University of Technology, China</span>
                </div>
            </div>
        </div>
    </div>
"""

# Other Content
content_prog = """<h2 class="section-title">Conference Program</h2><p>The detailed conference schedule will be announced closer to the conference date.</p><p>Please check the sub-menus for <strong>Keynote Speakers</strong> and the detailed <strong>Schedule</strong>.</p>"""
content_keynote = """<h2 class="section-title">Keynote Speakers</h2><p><em>Distinguished keynote speakers for ICKG 2026 will be announced shortly.</em></p>"""
content_schedule = """<h2 class="section-title">Conference Schedule</h2><p><em>The full technical program and schedule will be available here after the notification date.</em></p><h3>Tentative Overview</h3><ul><li><strong>Nov 12:</strong> Opening Ceremony, Keynotes, Technical Sessions.</li><li><strong>Nov 13:</strong> Technical Sessions, Workshops, Closing Ceremony.</li></ul>"""
content_venue = """<h2 class="section-title">Conference Venue</h2><p><strong>City:</strong> Shenyang, China</p><p>Shenyang is the capital of Liaoning Province and a major industrial and cultural hub in Northeast China.</p><h3>Local Attractions</h3><ul><li><strong>Mukden Palace:</strong> A UNESCO World Heritage site.</li><li><strong>Zhaoling Tomb:</strong> The tomb of the second Qing emperor.</li></ul><h3>Hotel Information</h3><p><em>Recommended hotels will be posted here later.</em></p>"""
content_reg = """
    <h2 class="section-title">Registration</h2>
    <p>Registration for ICKG 2026 is not yet open. Detailed registration fees and instructions will be updated here shortly.</p>
    <h3>Important Registration Deadlines</h3>
    <ul>
        <li><strong>Author Registration:</strong> September 18, 2026 (AOE)</li>
        <li><strong>Early Bird Registration:</strong> October 9, 2026 (AOE)</li>
    </ul>
    <h3>Registration Fees</h3>
    <p><em>(To be announced)</em></p>
"""

# Write files
files = {
    "style.css": css_content,
    "index.html": get_page("Home", "index.html", content_home),
    "call-for-papers.html": get_page("Call for Papers", "call-for-papers.html", content_cfp),
    "program.html": get_page("Program", "program.html", content_prog),
    "keynote-speakers.html": get_page("Keynote Speakers", "keynote-speakers.html", content_keynote),
    "schedule.html": get_page("Schedule", "schedule.html", content_schedule),
    "organization.html": get_page("Organization", "organization.html", content_org),
    "registration.html": get_page("Registration", "registration.html", content_reg),
    "venue.html": get_page("Venue", "venue.html", content_venue)
}

for fname, data in files.items():
    with open(os.path.join(folder_name, fname), "w", encoding="utf-8") as f:
        f.write(data)

print(f"SUCCESS! Website updated: Sidebar removed from ALL Program pages in folder: {os.path.abspath(folder_name)}")