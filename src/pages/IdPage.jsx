import { useParams, useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function IdPage() {
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    if (parseInt(id) > 100) {
      navigate("/");
    }
  }, [id, navigate]);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>ID da URL: {id}</h2>
    </div>
  );
}
