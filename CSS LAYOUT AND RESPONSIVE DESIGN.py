<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Webpage with Flexbox and Grid</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
    }

    /* Navigation Bar */
    nav {
      background-color: #333;
      color: #fff;
      padding: 1rem;
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .nav-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      max-width: 1200px;
      margin: 0 auto;
    }

    .nav-container ul {
      display: flex;
      list-style: none;
    }

    .nav-container ul li {
      margin-left: 2rem;
    }

    .nav-container ul li a {
      color: #fff;
      text-decoration: none;
      font-size: 1rem;
    }

    .nav-container ul li a:hover {
      color: #ddd;
    }

    /* Main Content with Grid */
    .main-container {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 2rem;
      max-width: 1200px;
      margin: 2rem auto;
      padding: 0 1rem;
    }

    .content {
      background-color: #f4f4f4;
      padding: 2rem;
      border-radius: 8px;
    }

    .sidebar {
      background-color: #e0e0e0;
      padding: 2rem;
      border-radius: 8px;
    }

    /* Footer with Flexbox */
    footer {
      background-color: #333;
      color: #fff;
      padding: 1rem;
      margin-top: 2rem;
    }

    .footer-container {
      display: flex;
      justify-content: space-around;
      align-items: center;
      max-width: 1200px;
      margin: 0 auto;
      flex-wrap: wrap;
    }

    .footer-container div {
      margin: 1rem;
    }

    /* Media Queries for Responsiveness */

    /* Tablet (max-width: 768px) */
    @media (max-width: 768px) {
      .nav-container {
        flex-direction: column;
        align-items: flex-start;
      }

      .nav-container ul {
        margin-top: 1rem;
        flex-direction: column;
      }

      .nav-container ul li {
        margin: 0.5rem 0;
      }

      .main-container {
        grid-template-columns: 1fr;
        gap: 1rem;
      }

      .footer-container {
        flex-direction: column;
        text-align: center;
      }
    }

    /* Mobile (max-width: 480px) */
    @media (max-width: 480px) {
      .nav-container {
        padding: 0.5rem;
      }

      .nav-container h1 {
        font-size: 1.5rem;
      }

      .nav-container ul li a {
        font-size: 0.9rem;
      }

      .main-container {
        margin: 1rem;
        padding: 0 0.5rem;
      }

      .content, .sidebar {
        padding: 1rem;
      }

      .footer-container div {
        margin: 0.5rem;
      }
    }
  </style>
</head>
<body>
  <!-- Navigation Bar -->
  <nav>
    <div class="nav-container">
      <h1>My Website</h1>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </div>
  </nav>

  <!-- Main Content -->
  <div class="main-container">
    <div class="content">
      <h2>Welcome to Our Site</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
      <p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    </div>
    <div class="sidebar">
      <h3>Quick Links</h3>
      <ul>
        <li><a href="#link1">Link 1</a></li>
        <li><a href="#link2">Link 2</a></li>
        <li><a href="#link3">Link 3</a></li>
      </ul>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="footer-container">
      <div>
        <h4>Contact Us</h4>
        <p>Email: info@example.com</p>
      </div>
      <div>
        <h4>Follow Us</h4>
        <p>Social Media Links</p>
      </div>
    </div>
  </footer>
</body>
</html>