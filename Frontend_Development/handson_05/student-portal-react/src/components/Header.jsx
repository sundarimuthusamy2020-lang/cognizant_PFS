function Header({ siteName, enrolledCount }) {
  return (
    <header className="header">
      <div className="logo">
        <h1>🎓 {siteName}</h1>
      </div>

      <nav className="navbar">
        <a href="#">Home</a>
        <a href="#">Courses</a>
        <a href="#">Profile</a>
      </nav>

      <div className="enrolled-badge">
        📚 Enrolled: <strong>{enrolledCount}</strong>
      </div>
    </header>
  );
}

export default Header;