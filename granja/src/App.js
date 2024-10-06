import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Button, Form, Table, Alert } from 'react-bootstrap';

const API_URL = 'http://localhost:5000';

function App() {
  const [animales, setAnimales] = useState([]);
  const [clima, setClima] = useState(null);
  const [nuevoAnimal, setNuevoAnimal] = useState({ tipo: 'Vaca', edad: '1', peso: '100', raza: 'Holstein' });
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchAnimales();
  }, []);

  const fetchAnimales = async () => {
    try {
      const response = await fetch(`${API_URL}/animales`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setAnimales(data);
      setError(null);
    } catch (error) {
      console.error("Error fetching animales:", error);
      setError("Error al obtener los animales. Por favor, intenta de nuevo más tarde.");
    }
  };

  const agregarAnimal = async (e) => {
    e.preventDefault();
    try {
      const animalParaEnviar = {
        ...nuevoAnimal,
        edad: parseInt(nuevoAnimal.edad, 10),
        peso: parseFloat(nuevoAnimal.peso)
      };
      const response = await fetch(`${API_URL}/animales`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(animalParaEnviar),
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
      }
      await fetchAnimales();
      setNuevoAnimal({ tipo: 'Vaca', edad: '1', peso: '100', raza: 'Holstein' });
      setError(null);
    } catch (error) {
      console.error("Error agregando animal:", error);
      setError(`Error al agregar el animal: ${error.message}`);
    }
  };

  const simularDia = async () => {
    try {
      const response = await fetch(`${API_URL}/simular`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      if (data.animales) {
        setAnimales(data.animales);
      }
      if (data.clima) {
        setClima(data.clima);
      }
      setError(null);
    } catch (error) {
      console.error("Error simulando día:", error);
      setError("Error al simular el día. Por favor, intenta de nuevo más tarde.");
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNuevoAnimal(prev => ({ ...prev, [name]: value }));
  };

  return (
    <Container className="mt-4">
      <h1 className="mb-4">Simulador de Granja</h1>
      
      {error && <Alert variant="danger">{error}</Alert>}
      
      <Row className="mb-4">
        <Col>
          <Button onClick={simularDia}>Simular Día</Button>
        </Col>
      </Row>

      {clima && (
        <Alert variant="info">
          Clima: {clima.condicion}, Temperatura: {clima.temperatura}°C
        </Alert>
      )}

      <h2 className="mb-3">Agregar Animal</h2>
      <Form onSubmit={agregarAnimal}>
        <Row>
          <Col>
            <Form.Group>
              <Form.Label>Tipo</Form.Label>
              <Form.Control as="select" name="tipo" value={nuevoAnimal.tipo} onChange={handleInputChange}>
                <option>Vaca</option>
                <option>Gallina</option>
                <option>Oveja</option>
                <option>Caballo</option>
                <option>Cerdo</option>
              </Form.Control>
            </Form.Group>
          </Col>
          <Col>
            <Form.Group>
              <Form.Label>Edad</Form.Label>
              <Form.Control type="number" name="edad" value={nuevoAnimal.edad} onChange={handleInputChange} />
            </Form.Group>
          </Col>
          <Col>
            <Form.Group>
              <Form.Label>Peso</Form.Label>
              <Form.Control type="number" name="peso" value={nuevoAnimal.peso} onChange={handleInputChange} />
            </Form.Group>
          </Col>
          <Col>
            <Form.Group>
              <Form.Label>Raza</Form.Label>
              <Form.Control type="text" name="raza" value={nuevoAnimal.raza} onChange={handleInputChange} />
            </Form.Group>
          </Col>
          <Col>
            <Button type="submit" className="mt-4">Agregar</Button>
          </Col>
        </Row>
      </Form>

      <h2 className="mt-4 mb-3">Animales en la Granja</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Tipo</th>
            <th>Edad</th>
            <th>Peso</th>
            <th>Raza</th>
            <th>Salud</th>
            <th>Estado de Ánimo</th>
            <th>Energía</th>
            <th>Hambre</th>
          </tr>
        </thead>
        <tbody>
          {animales.map((animal, index) => (
            <tr key={index}>
              <td>{animal.tipo}</td>
              <td>{animal.edad}</td>
              <td>{animal.peso}</td>
              <td>{animal.raza}</td>
              <td>{animal.salud}</td>
              <td>{animal.estado_animo}</td>
              <td>{animal.energia}</td>
              <td>{animal.hambre}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
}

export default App;