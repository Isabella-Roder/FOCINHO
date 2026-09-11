import { useEffect, useState } from "react";


interface Cliente {
  id: number;
  nome: string;
  email: string;
  telefone: string;
  endereco: string | null;
}

export function App() {
  
  const [clientes, setClientes] = useState<Cliente[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/clientes")
      .then((res) => res.json())
      .then((data) => setClientes(data));
  }, []);

  return (
    <div>
      <h1>Focinho - Cliente</h1>

      <ul>
        {clientes.map((cliente) => (
          <li key={cliente.id}>
            {cliente.nome} - {cliente.email}
          </li>
        ))}
      </ul>
    </div>
  )
}