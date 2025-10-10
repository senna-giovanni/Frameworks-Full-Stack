import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import BuscadorPage from "./pages/BuscadorPage";
import ProfilePage from "./pages/ProfilePage";
import IdPage from "./pages/IdPage";
import NotFoundPage from "./pages/NotFoundPage";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<BuscadorPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/id/:id" element={<IdPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </Router>
  );
}

export default App;
