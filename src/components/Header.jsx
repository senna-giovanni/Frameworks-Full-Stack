import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header style={styles.header}>
      <nav>
        <Link to="/" style={styles.link}>Buscador CEP</Link>
        <Link to="/profile" style={styles.link}>Profile</Link>
        <Link to="/id/42" style={styles.link}>Ver ID</Link>
      </nav>
    </header>
  );
}

const styles = {
  header: {
    display: "flex",
    justifyContent: "center",
    gap: "20px",
    padding: "10px",
    backgroundColor: "#282c34",
  },
  link: {
    color: "#61dafb",
    textDecoration: "none",
    fontWeight: "bold",
  },
};
