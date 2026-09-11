import React, { use, useEffect, useState } from "react";
import "./App.css";

interface Cliente {
  id: number;
  nome: string;
  email: string;
  telefone: string;
  endereco: string | null;
}

export function App() {
  
  const [clientes, setClientes] = useState<Cliente[]>([]);

  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [telefone, setTelefone] = useState("");
  const [endereco, setEndereco] = useState("");

  function carregarClientes() {
    fetch("http://127.0.0.1:5000/clientes")
      .then((res) => res.json())
      .then((data) => setClientes(data));
  }

  useEffect(() => {
    carregarClientes();
  }, []);

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    fetch("http://127.0.0.1:5000/clientes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome, email, telefone, endereco })
    }).then(() => {
      setNome("");
      setEmail("");
      setTelefone("");
      setEndereco("");
      carregarClientes();
    });
  }

  return (
    <div className="page">
      
      <header className="header">
        <h1>🐾 Focinho</h1>
        <p>Gestão de clientes do petshop</p>
      </header>



      <main className="content">
        <section className="card">
          <h2>Novo cliente</h2>
          <form onSubmit={handleSubmit} className="form">
            <input
              type="text"
              value={nome}
              placeholder="Nome"
              onChange={(e) => setNome(e.target.value)}
              required
            />
            <input
              type="email"
              value={email}
              placeholder="Email"
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <input
              type="text"
              value={telefone}
              placeholder="Telefone"
              onChange={(e) => setTelefone(e.target.value)}
              required
            />
            <input
              type="text"
              value={endereco}
              placeholder="Endereço"
              onChange={(e) => setEndereco(e.target.value)}
            />
            <button type="submit">Cadastrar</button>
          </form>
        </section>
      </main>

      <section className="card">
        <h2>Clientes cadastrados</h2>
        {clientes.length === 0 ? (
          <p className="empty">Nenhum cliente cadastrado ainda.</p>
        ) : (
          <ul className="lista">
            {clientes.map((cliente) => (
              <li key={cliente.id} className="item">
                <span className="item-nome">{cliente.nome}</span>
                <span className="item-detalhe">{cliente.email}</span>
                <span className="item-detalhe">{cliente.telefone}</span>
              </li>
            ))}
          </ul>
        )}
      </section>

    </div>
  )
}