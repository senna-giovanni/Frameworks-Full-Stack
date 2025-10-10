export default function ProfileCard() {
  const profile = {
    nome: "Giovanni Bonfim",
    profissao: "Desenvolvedor Front-End",
    email: "giovanni@example.com",
  };

  return (
    <div style={cardStyle}>
      <h2>{profile.nome}</h2>
      <p>{profile.profissao}</p>
      <p>{profile.email}</p>
    </div>
  );
}

const cardStyle = {
  border: "1px solid #ccc",
  borderRadius: "10px",
  padding: "20px",
  maxWidth: "300px",
  margin: "40px auto",
  textAlign: "center",
  boxShadow: "0 2px 5px rgba(0,0,0,0.1)"
};
