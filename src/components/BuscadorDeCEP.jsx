import { useState } from "react";

export default function BuscadorDeCEP() {
  const [cep, setCep] = useState("");
  const [dados, setDados] = useState(null);

  const buscarCEP = async () => {
    if (cep.length !== 8) {
      alert("Digite um CEP válido com 8 dígitos!");
      return;
    }

    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const data = await response.json();
    setDados(data);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "20px" }}>
      <h2>Buscador de CEP</h2>
      <input
        type="text"
        placeholder="Digite o CEP"
        value={cep}
        onChange={(e) => setCep(e.target.value)}
      />
      <button onClick={buscarCEP}>Buscar</button>
      {dados && (
        <div>
          <p><strong>Logradouro:</strong> {dados.logradouro}</p>
          <p><strong>Bairro:</strong> {dados.bairro}</p>
          <p><strong>Cidade:</strong> {dados.localidade}</p>
          <p><strong>UF:</strong> {dados.uf}</p>
        </div>
      )}
    </div>
  );
}
