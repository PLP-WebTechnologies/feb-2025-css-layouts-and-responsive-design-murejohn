<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Layout</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="logo">My Awesome Site</div>
            <ul class="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main class="content-grid">
        <section class="hero">
            <h1>Welcome!</h1>
            <p>This is the main hero section of our fantastic website. Check out the amazing content below!</p>
            <button>Learn More</button>
        </section>

        <section class="feature">
            <h2>Feature One</h2>
            <p>Short description of the first feature.</p>
        </section>

        <section class="feature">
            <h2>Feature Two</h2>
            <p>Brief explanation of the second feature.</p>
        </section>

        <section class="feature">
            <h2>Feature Three</h2>
            <p>Details about the third compelling feature.</p>
        </section>

        <aside class="sidebar">
            <h3>Sidebar</h3>
            <p>Some extra information or related links can go here.</p>
        </aside>

        <div class="ad">
            <p>Advertisement Space</p>
        </div>

        <div class="extra">
            <h3>Extra Content</h3>
            <p>More interesting stuff to explore.</p>
        </div>
    </main>

    <footer>
        <p>&copy; 2025 My Awesome Site</p>
    </footer>
</body>
</html>
body {
    font-family: sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}

/* Header and Navigation */
header {
    background-color: #333;
    color: white;
    padding: 1em 0;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
}

.logo {
    font-size: 1.5em;
    font-weight: bold;
}

.nav-links {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
}

.nav-links li a {
    color: white;
    text-decoration: none;
    padding: 0.5em 1em;
    margin-left: 1em;
}

.nav-links li a:hover {
    color: #ddd;
}

/* Main Content (using CSS Grid) */
.content-grid {
    display: grid;
    grid-template-columns: 1fr; /* Single column by default for mobile */
    gap: 20px;
    padding: 20px;
}

.hero {
    background-color: #e0f7fa;
    padding: 2em;
    border-radius: 5px;
    text-align: center;
}

.feature {
    background-color: #fff;
    padding: 1.5em;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.sidebar {
    background-color: #f9f9f9;
    padding: 1.5em;
    border: 1px solid #eee;
    border-radius: 5px;
}

.ad {
    background-color: #ffe0b2;
    padding: 1em;
    text-align: center;
    border-radius: 5px;
}

.extra {
    background-color: #e8f5e9;
    padding: 1.5em;
    border: 1px solid #dcedc8;
    border-radius: 5px;
}

/* Footer */
footer {
    text-align: center;
    padding: 1em 0;
    background-color: #333;
    color: white;
    margin-top: 20px;
}

/* Media Query for Tablets (min-width: 768px) */
@media (min-width: 768px) {
    .content-grid {
        grid-template-columns: repeat(2, 1fr); /* Two columns for tablets */
        grid-template-areas:
            "hero hero"
            "feature1 feature2"
            "feature3 sidebar"
            "ad extra";
    }

    .hero {
        grid-area: hero;
    }

    .feature:nth-child(2) { /* Feature One */
        grid-area: feature1;
    }

    .feature:nth-child(3) { /* Feature Two */
        grid-area: feature2;
    }

    .feature:nth-child(4) { /* Feature Three */
        grid-area: feature3;
    }

    .sidebar {
        grid-area: sidebar;
    }

    .ad {
        grid-area: ad;
    }

    .extra {
        grid-area: extra;
    }
}

/* Media Query for Desktops (min-width: 1024px) */
@media (min-width: 1024px) {
    .content-grid {
        grid-template-columns: 2fr 1fr 1fr; /* Three columns for desktops */
        grid-template-areas:
            "hero hero sidebar"
            "feature1 feature2 sidebar"
            "feature3 extra ad";
    }
}