import os
import shutil

# 1. Define the folder name
folder_name = "Aegis_Website"
os.makedirs(folder_name, exist_ok=True)

# 2. Define the file contents with ALL FIXES (Logo size, Brian Smith, Phone, Header Height)
files = {}

# --- STYLES.CSS ---
files["styles.css"] = """/* --- VARIABLES & RESET --- */
:root {
    --primary: #0052CC; /* Royal Blue */
    --accent: #FF8800;  /* Orange */
    --accent-hover: #e07b00;
    --text-dark: #2C3E50;
    --text-light: #5f6c7b;
    --white: #ffffff;
    --bg-light: #f4f7f9;
    --border-radius: 8px;
    --shadow: 0 4px 6px rgba(0,0,0,0.1);
    --transition: all 0.3s ease;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    color: var(--text-dark);
    line-height: 1.6;
    background-color: var(--white);
    padding-top: 100px; /* UPDATED: Space for taller header */
}

a {
    text-decoration: none;
    color: inherit;
}

ul {
    list-style: none;
}

img {
    max-width: 100%;
    height: auto;
}

/* --- TYPOGRAPHY --- */
h1, h2, h3, h4 {
    color: var(--text-dark);
    font-weight: 700;
    margin-bottom: 1rem;
}

h1 { font-size: 2.5rem; line-height: 1.2; }
h2 { font-size: 2rem; text-align: center; margin-bottom: 2rem; color: var(--primary); }
h3 { font-size: 1.5rem; }

.text-center { text-align: center; }
.highlight { color: var(--accent); }

/* --- UTILITIES --- */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.section {
    padding: 80px 0;
}

.bg-light {
    background-color: var(--bg-light);
}

/* --- BUTTONS --- */
.btn {
    display: inline-block;
    padding: 12px 24px;
    border-radius: var(--border-radius);
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition);
    border: none;
    font-size: 1rem;
    text-align: center;
}

.btn-primary {
    background-color: var(--accent);
    color: var(--white);
}

.btn-primary:hover {
    background-color: var(--accent-hover);
    transform: translateY(-2px);
}

.btn-secondary {
    background-color: var(--primary);
    color: var(--white);
}

.btn-secondary:hover {
    background-color: #0042a3;
    transform: translateY(-2px);
}

/* --- HEADER & NAV --- */
.header {
    background-color: var(--white);
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
    height: 100px; /* UPDATED: Taller header */
    display: flex;
    align-items: center;
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* --- LOGO STYLES --- */
.logo {
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--text-dark);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 15px;
}

.logo img {
    height: 80px; /* UPDATED: Larger logo size */
    width: auto;
}

.nav-links {
    display: flex;
    gap: 30px;
}

.nav-links a {
    font-weight: 600;
    color: var(--text-dark);
    transition: var(--transition);
}

.nav-links a:hover, .nav-links a.active {
    color: var(--primary);
}

.header-cta {
    display: block;
}

.mobile-toggle {
    display: none;
    font-size: 1.5rem;
    cursor: pointer;
}

/* --- HERO SECTION --- */
.hero {
    background: linear-gradient(135deg, var(--primary), #003380);
    color: var(--white);
    padding: 100px 0;
    text-align: center;
}

.hero h1 { color: var(--white); }
.hero p { font-size: 1.25rem; margin-bottom: 2rem; opacity: 0.9; }
.hero-btns { display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; }

/* --- TRUST BADGES --- */
.trust-bar {
    background: var(--bg-light);
    padding: 40px 0;
    border-bottom: 1px solid #e1e8ed;
}

.trust-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    text-align: center;
}

.trust-item i { font-size: 2rem; color: var(--accent); margin-bottom: 10px; }
.trust-item h4 { font-size: 1.1rem; margin: 0; }

/* --- CARDS & SERVICES --- */
.grid-2 {
    display: grid;
    grid-template-columns: 1fr;
    gap: 40px;
}

.grid-3 {
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;
}

.card {
    background: var(--white);
    padding: 30px;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow);
    transition: var(--transition);
    border-top: 4px solid var(--primary);
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}

.service-list li {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px solid #eee;
}

.price {
    font-weight: 700;
    color: var(--accent);
}

/* --- PACKAGES --- */
.package-card {
    text-align: center;
    border: 1px solid #eee;
    padding: 40px 20px;
    position: relative;
    background: var(--white);
}

.package-card.featured {
    border: 2px solid var(--accent);
    transform: scale(1.05);
    z-index: 2;
}

.package-price {
    font-size: 2.5rem;
    color: var(--primary);
    font-weight: 800;
    margin: 20px 0;
}

.package-card ul { margin-bottom: 30px; text-align: left; }
.package-card li { margin-bottom: 10px; padding-left: 20px; position: relative; }
.package-card li::before {
    content: "✓";
    color: var(--accent);
    position: absolute;
    left: 0;
}

/* --- SPECIAL OFFERS --- */
.offers-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.offer-card {
    background: var(--primary);
    color: var(--white);
    padding: 20px;
    border-radius: var(--border-radius);
    text-align: center;
}

.offer-card h3 { color: var(--white); margin-bottom: 10px; }
.offer-val { font-size: 1.5rem; font-weight: 800; color: var(--accent); display: block; margin-top: 10px; }

/* --- CONTACT & FORM --- */
.contact-wrapper {
    display: grid;
    grid-template-columns: 1fr;
    gap: 40px;
}

.contact-info-item {
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
}

.form-control {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: inherit;
    font-size: 1rem;
}

textarea.form-control {
    resize: vertical;
    min-height: 120px;
}

/* --- FOOTER --- */
footer {
    background: var(--text-dark);
    color: var(--white);
    padding: 60px 0 20px;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 40px;
    margin-bottom: 40px;
}

.footer-col h4 { color: var(--white); margin-bottom: 20px; }
.footer-links li { margin-bottom: 10px; }
.footer-links a:hover { color: var(--accent); }
.copyright { text-align: center; border-top: 1px solid #3d5166; padding-top: 20px; font-size: 0.9rem; }

/* --- RESPONSIVE MEDIA QUERIES --- */
@media (min-width: 768px) {
    .grid-2 { grid-template-columns: 1fr 1fr; }
    .grid-3 { grid-template-columns: repeat(3, 1fr); }
    .contact-wrapper { grid-template-columns: 1fr 1fr; }
    .header-cta { display: block; }
}

@media (max-width: 768px) {
    .nav-links {
        position: absolute;
        top: 100px; /* Updated for taller header */
        left: 0;
        width: 100%;
        background: var(--white);
        flex-direction: column;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        display: none;
    }

    .nav-links.active { display: flex; }
    .mobile-toggle { display: block; }
    .package-card.featured { transform: scale(1); }
    h1 { font-size: 2rem; }
}
"""

# --- INDEX.HTML ---
files["index.html"] = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Aegis IT Solutions - Professional, affordable IT support and computer repair in Cedartown, GA. Residential and business services.">
    <title>Aegis IT Solutions | IT Support Made Simple</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&amp;display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <header class="header">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="logo.jpg" alt="Aegis IT Solutions Logo" style="height: 80px; width: auto;">
                <span>Aegis IT Solutions</span>
            </a>
            <div class="mobile-toggle" id="mobile-menu">☰</div>
            <nav>
                <ul class="nav-links">
                    <li><a href="index.html" class="active">Home</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li class="header-cta"><a href="tel:7063148748" class="btn btn-primary">Call (706) 314-8748</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>Computer Problems? <br>We Make IT Simple.</h1>
            <p>Professional, reliable IT support for homes and businesses in Cedartown & surrounding areas.</p>
            <div class="hero-btns">
                <a href="contact.html" class="btn btn-primary">Get Free Quote</a>
                <a href="tel:7063148748" class="btn btn-secondary">Call Now</a>
            </div>
        </div>
    </section>

    <section class="trust-bar">
        <div class="container">
            <div class="trust-grid">
                <div class="trust-item">
                    <i>★</i>
                    <h4>5-Star Service</h4>
                </div>
                <div class="trust-item">
                    <i>⌂</i>
                    <h4>Local & Family Owned</h4>
                </div>
                <div class="trust-item">
                    <i>⚡</i>
                    <h4>Same-Day Service</h4>
                </div>
                <div class="trust-item">
                    <i>$</i>
                    <h4>Fair Pricing</h4>
                </div>
            </div>
        </div>
    </section>

    <section class="section bg-light">
        <div class="container">
            <h2>Our Services</h2>
            <div class="grid-2">
                <div class="card">
                    <h3>Residential Services</h3>
                    <p>Complete computer care for your home.</p>
                    <ul class="service-list">
                        <li><span>Computer Repair</span> <span class="price">$125</span></li>
                        <li><span>Virus Removal</span> <span class="price">$100</span></li>
                        <li><span>Computer Tune-up</span> <span class="price">$100</span></li>
                        <li><span>WiFi Setup</span> <span class="price">$150</span></li>
                    </ul>
                    <br>
                    <a href="services.html" class="btn btn-secondary">View All Services</a>
                </div>
                <div class="card">
                    <h3>Business Solutions</h3>
                    <p>Reliable IT infrastructure for your company.</p>
                    <ul class="service-list">
                        <li><span>Monthly IT Support</span> <span class="price">From $150/mo</span></li>
                        <li><span>Network Setup</span> <span class="price">$300 - $500</span></li>
                        <li><span>Cloud Services</span> <span class="price">From $500</span></li>
                        <li><span>Web & Email</span> <span class="price">From $500</span></li>
                    </ul>
                    <br>
                    <a href="services.html" class="btn btn-secondary">Business Solutions</a>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <h2>Best Value Packages</h2>
            <div class="grid-3">
                <div class="package-card">
                    <h3>New Computer Bundle</h3>
                    <div class="package-price">$200</div>
                    <ul>
                        <li>Data Transfer</li>
                        <li>Software Installation</li>
                        <li>Printer Setup</li>
                        <li>Email Configuration</li>
                    </ul>
                    <a href="contact.html" class="btn btn-secondary">Choose Bundle</a>
                </div>
                <div class="package-card featured">
                    <span style="background:var(--accent); color:white; padding:5px 10px; border-radius:4px; font-size:0.8rem; margin-bottom:10px; display:inline-block;">POPULAR</span>
                    <h3>Fresh Start</h3>
                    <div class="package-price">$250</div>
                    <p style="color: green; font-weight:bold;">Save $75</p>
                    <ul>
                        <li>Full Virus Removal</li>
                        <li>System Tune-Up</li>
                        <li>Data Backup</li>
                        <li>Security Software Install</li>
                    </ul>
                    <a href="contact.html" class="btn btn-primary">Choose Bundle</a>
                </div>
                <div class="package-card">
                    <h3>Smart Home Starter</h3>
                    <div class="package-price">$225</div>
                    <ul>
                        <li>3 Device Setups</li>
                        <li>App Integration</li>
                        <li>Voice Assistant Config</li>
                        <li>Training Session</li>
                    </ul>
                    <a href="contact.html" class="btn btn-secondary">Choose Bundle</a>
                </div>
            </div>
        </div>
    </section>

    <section class="section bg-light">
        <div class="container">
            <h2>Special Offers</h2>
            <div class="offers-grid">
                <div class="offer-card">
                    <h3>Senior Discount</h3>
                    <p>For our valued senior citizens</p>
                    <span class="offer-val">10% OFF</span>
                </div>
                <div class="offer-card">
                    <h3>New Client Special</h3>
                    <p>On your first major repair</p>
                    <span class="offer-val">$50 OFF</span>
                </div>
                <div class="offer-card">
                    <h3>Referral Bonus</h3>
                    <p>When you refer a friend</p>
                    <span class="offer-val">$25 CREDIT</span>
                </div>
            </div>
        </div>
    </section>

    <section class="section text-center">
        <div class="container">
            <h2>Ready to Fix Your Tech?</h2>
            <p style="margin-bottom: 20px;">Serving Cedartown and a 50-mile radius.</p>
            <a href="tel:7063148748" class="btn btn-primary">Call (706) 314-8748</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>Aegis IT Solutions</h4>
                    <p>IT Support Made Simple for homes and businesses in Georgia.</p>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact Us</h4>
                    <ul class="footer-links">
                        <li>Phone: (706) 314-8748</li>
                        <li>Email: info@aegisittech.com</li>
                        <li>Location: Cedartown, GA</li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2025 Aegis IT Solutions. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
"""

# --- SERVICES.HTML ---
files["services.html"] = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services | Aegis IT Solutions</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&amp;display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <header class="header">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="logo.jpg" alt="Aegis IT Solutions Logo" style="height: 80px; width: auto;">
                <span>Aegis IT Solutions</span>
            </a>
            <div class="mobile-toggle" id="mobile-menu">☰</div>
            <nav>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="services.html" class="active">Services</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li class="header-cta"><a href="tel:7063148748" class="btn btn-primary">Call (706) 314-8748</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="hero" style="padding: 60px 0;">
        <div class="container">
            <h1>Our Services & Pricing</h1>
            <p>Transparent pricing with no hidden fees.</p>
        </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="grid-2">
                <div>
                    <h2 style="text-align: left;">Residential Services</h2>
                    <div class="card">
                        <ul class="service-list">
                            <li><span>Computer Repair</span> <span class="price">$125</span></li>
                            <li><span>Virus & Malware Removal</span> <span class="price">$100</span></li>
                            <li><span>System Tune-up</span> <span class="price">$100</span></li>
                            <li><span>WiFi & Network Setup</span> <span class="price">$150</span></li>
                            <li><span>Smart Home Setup (per device)</span> <span class="price">$75</span></li>
                            <li><span>New Computer Setup</span> <span class="price">$75</span></li>
                            <li><span>Family Internet Safety</span> <span class="price">$200</span></li>
                            <li><span>Tech Training (per hour)</span> <span class="price">$60</span></li>
                        </ul>
                    </div>
                </div>

                <div>
                    <h2 style="text-align: left;">Business Services</h2>
                    <div class="card">
                        <ul class="service-list">
                            <li><span>Monthly IT Support</span> <span class="price">$150 - $600/mo</span></li>
                            <li><span>Network Cabling & Setup</span> <span class="price">$300 - $500</span></li>
                            <li><span>Cloud Services Migration</span> <span class="price">From $500</span></li>
                            <li><span>Website & Email Hosting</span> <span class="price">From $500</span></li>
                        </ul>
                        <div style="margin-top: 20px; padding: 15px; background: #f9f9f9; border-radius: 4px;">
                            <p><strong>Note for Businesses:</strong> Prices may vary based on the size of your office and complexity of the network. Call us for a free site survey.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section bg-light">
        <div class="container">
            <h2>Package Deals</h2>
            <div class="grid-3">
                <div class="package-card">
                    <h3>New Computer Bundle</h3>
                    <div class="package-price">$200</div>
                    <p>Perfect for setting up a new PC or Mac.</p>
                    <a href="contact.html" class="btn btn-secondary">Order Now</a>
                </div>
                <div class="package-card featured">
                    <h3>Fresh Start</h3>
                    <div class="package-price">$250</div>
                    <p>Revive your old slow computer.</p>
                    <a href="contact.html" class="btn btn-primary">Order Now</a>
                </div>
                <div class="package-card">
                    <h3>Smart Home Starter</h3>
                    <div class="package-price">$225</div>
                    <p>Automate your home with ease.</p>
                    <a href="contact.html" class="btn btn-secondary">Order Now</a>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>Aegis IT Solutions</h4>
                    <p>IT Support Made Simple.</p>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact Us</h4>
                    <ul class="footer-links">
                        <li>Phone: (706) 314-8748</li>
                        <li>Email: info@aegisittech.com</li>
                        <li>Location: Cedartown, GA</li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2025 Aegis IT Solutions. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>
"""

# --- ABOUT.HTML ---
files["about.html"] = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us | Aegis IT Solutions</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&amp;display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <header class="header">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="logo.jpg" alt="Aegis IT Solutions Logo" style="height: 80px; width: auto;">
                <span>Aegis IT Solutions</span>
            </a>
            <div class="mobile-toggle" id="mobile-menu">☰</div>
            <nav>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="about.html" class="active">About</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li class="header-cta"><a href="tel:7063148748" class="btn btn-primary">Call (706) 314-8748</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="hero" style="padding: 60px 0;">
        <div class="container">
            <h1>About Aegis IT</h1>
            <p>Local IT Support You Can Trust.</p>
        </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="grid-2">
                <div>
                    <h2>Our Story</h2>
                    <p>At Aegis IT Solutions, we believe technology should make your life easier, not harder. Based in Cedartown, GA, we are a family-owned business dedicated to providing honest, jargon-free IT support to our neighbors and local businesses.</p>
                    <br>
                    <p>We saw a need in our community for reliable tech support that doesn't cost a fortune. Whether you need a simple virus removal or a full business network installation, we treat every client like family.</p>
                </div>
                <div class="card" style="text-align: center;">
                    <div style="background: #eee; width: 150px; height: 150px; border-radius: 50%; margin: 0 auto 20px; display: flex; align-items: center; justify-content: center; color: #aaa;">Photo</div>
                    <h3>Brian Smith</h3>
                    <p>Owner & Lead Technician</p>
                    <p>With over 15 years of experience in IT, I started this company to bring enterprise-level support to our local community.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section bg-light">
        <div class="container">
            <h2>Our Core Values</h2>
            <div class="grid-2">
                <div class="card">
                    <h3 class="highlight">Honesty First</h3>
                    <p>We will never sell you hardware or software you don't need. We provide transparent assessments and quotes before starting any work.</p>
                </div>
                <div class="card">
                    <h3 class="highlight">No "Geek Speak"</h3>
                    <p>We explain problems and solutions in plain English, so you understand exactly what is happening with your technology.</p>
                </div>
                <div class="card">
                    <h3 class="highlight">Responsive Service</h3>
                    <p>When your tech breaks, you need help fast. We prioritize quick turnaround times and offer same-day service for emergencies.</p>
                </div>
                <div class="card">
                    <h3 class="highlight">Community Focused</h3>
                    <p>We are proud to serve Cedartown and the surrounding 50-mile radius. We are your neighbors, and we care about your success.</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>Aegis IT Solutions</h4>
                    <p>IT Support Made Simple.</p>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact Us</h4>
                    <ul class="footer-links">
                        <li>Phone: (706) 314-8748</li>
                        <li>Email: info@aegisittech.com</li>
                        <li>Location: Cedartown, GA</li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2025 Aegis IT Solutions. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>
"""

# --- CONTACT.HTML ---
files["contact.html"] = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us | Aegis IT Solutions</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&amp;display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <header class="header">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="logo.jpg" alt="Aegis IT Solutions Logo" style="height: 80px; width: auto;">
                <span>Aegis IT Solutions</span>
            </a>
            <div class="mobile-toggle" id="mobile-menu">☰</div>
            <nav>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li class="header-cta"><a href="tel:7063148748" class="btn btn-primary">Call (706) 314-8748</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="hero" style="padding: 60px 0;">
        <div class="container">
            <h1>Contact Us</h1>
            <p>We're here to help with your IT needs.</p>
        </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="contact-wrapper">
                <div>
                    <h2>Get In Touch</h2>
                    <div class="card">
                        <div class="contact-info-item">
                            <h4>Phone</h4>
                            <p><a href="tel:7063148748" class="highlight" style="font-weight:bold; font-size:1.2rem;">(706) 314-8748</a></p>
                        </div>
                        <div class="contact-info-item">
                            <h4>Email</h4>
                            <p>info@aegisittech.com</p>
                        </div>
                        <div class="contact-info-item">
                            <h4>Location</h4>
                            <p>Cedartown, GA</p>
                        </div>
                        <div class="contact-info-item">
                            <h4>Service Area</h4>
                            <p>We serve a 50-mile radius around Cedartown.</p>
                        </div>
                        <div class="contact-info-item">
                            <h4>Business Hours</h4>
                            <ul style="list-style: none; padding:0;">
                                <li><strong>Mon-Fri:</strong> 8:00 AM - 6:00 PM</li>
                                <li><strong>Saturday:</strong> 9:00 AM - 2:00 PM</li>
                                <li><strong>Sunday:</strong> Closed</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div>
                    <h2>Send a Message</h2>
                    <form class="card" id="contactForm">
                        <div class="form-group">
                            <label for="name">Full Name</label>
                            <input type="text" id="name" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number</label>
                            <input type="tel" id="phone" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email Address</label>
                            <input type="email" id="email" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="service">Interested Service</label>
                            <select id="service" class="form-control">
                                <option value="repair">Computer Repair</option>
                                <option value="virus">Virus Removal</option>
                                <option value="business">Business Support</option>
                                <option value="smart-home">Smart Home</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" class="form-control" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <section class="section bg-light">
        <div class="container">
            <h2>Frequently Asked Questions</h2>
            <div style="max-width: 800px; margin: 0 auto;">
                <details style="background:white; padding:15px; border-radius:8px; margin-bottom:10px; box-shadow:var(--shadow);">
                    <summary style="font-weight:600; cursor:pointer;">Do you charge for a diagnosis?</summary>
                    <p style="margin-top:10px;">We offer a free initial consultation over the phone. If we need to perform deep diagnostics in our lab, the fee is waived if you proceed with the repair.</p>
                </details>
                <details style="background:white; padding:15px; border-radius:8px; margin-bottom:10px; box-shadow:var(--shadow);">
                    <summary style="font-weight:600; cursor:pointer;">How long does a typical repair take?</summary>
                    <p style="margin-top:10px;">Most software issues and virus removals are completed within 24 hours. Hardware repairs depend on part availability, but usually take 2-3 days.</p>
                </details>
                <details style="background:white; padding:15px; border-radius:8px; margin-bottom:10px; box-shadow:var(--shadow);">
                    <summary style="font-weight:600; cursor:pointer;">Do you come to my house?</summary>
                    <p style="margin-top:10px;">Yes! We offer on-site support for both residential and business clients within our 50-mile service radius.</p>
                </details>
                <details style="background:white; padding:15px; border-radius:8px; margin-bottom:10px; box-shadow:var(--shadow);">
                    <summary style="font-weight:600; cursor:pointer;">Do you offer a warranty on repairs?</summary>
                    <p style="margin-top:10px;">Yes, all our labor is backed by a 30-day warranty. New hardware parts come with their respective manufacturer warranties.</p>
                </details>
                <details style="background:white; padding:15px; border-radius:8px; margin-bottom:10px; box-shadow:var(--shadow);">
                    <summary style="font-weight:600; cursor:pointer;">Can you help with Mac computers?</summary>
                    <p style="margin-top:10px;">Absolutely. We service both Windows PCs and Apple computers (iMacs, MacBooks).</p>
                </details>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>Aegis IT Solutions</h4>
                    <p>IT Support Made Simple.</p>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="services.html">Services</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact Us</h4>
                    <ul class="footer-links">
                        <li>Phone: (706) 314-8748</li>
                        <li>Email: info@aegisittech.com</li>
                        <li>Location: Cedartown, GA</li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2025 Aegis IT Solutions. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>
"""

# --- SCRIPT.JS ---
files["script.js"] = """document.addEventListener('DOMContentLoaded', () => {

    // --- Mobile Menu Toggle ---
    const mobileMenuBtn = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            // Change icon from hamburger to X when active
            if(navLinks.classList.contains('active')) {
                mobileMenuBtn.textContent = '✕';
            } else {
                mobileMenuBtn.textContent = '☰';
            }
        });
    }

    // --- Close Mobile Menu when clicking a link ---
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            mobileMenuBtn.textContent = '☰';
        });
    });

    // --- Contact Form Handling (Simulation) ---
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            // Simple validation check (HTML5 does most of it)
            const name = document.getElementById('name').value;
            const phone = document.getElementById('phone').value;

            if(name && phone) {
                alert(`Thank you, ${name}! We have received your request and will call you at ${phone} shortly.`);
                contactForm.reset();
            } else {
                alert('Please fill out all required fields.');
            }
        });
    }

    // --- Smooth Scrolling for Anchor Links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
"""

# 3. Create Files
for filename, content in files.items():
    with open(os.path.join(folder_name, filename), "w", encoding="utf-8") as f:
        f.write(content)

# 4. Zip the directory
shutil.make_archive(folder_name, 'zip', folder_name)

print(f"SUCCESS! 'Aegis_Website.zip' has been created.")
print(f"Please copy your 'logo.jpg' into the folder or upload it separately to Hostinger.")
