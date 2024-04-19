import React, { useState } from 'react';

function AgregarProductoForm() {
  const [producto, setProducto] = useState({
    nombre: '',
    descripcion: '',
    precio: ''
  });

  const handleChange = (e) => {
    setProducto({ ...producto, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/productos/agregar/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(producto),
      });
      if (response.ok) {
        console.log('Producto agregado con éxito');
        // Puedes manejar una lógica adicional aquí, como limpiar el formulario o redirigir.
      } else {
        console.error('Error al agregar el producto');
      }
    } catch (error) {
      console.error('Hubo un error al hacer la solicitud:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="nombre"
        type="text"
        placeholder="Nombre del Producto"
        value={producto.nombre}
        onChange={handleChange}
      />
      <textarea
        name="descripcion"
        placeholder="Descripción"
        value={producto.descripcion}
        onChange={handleChange}
      />
      <input
        name="precio"
        type="number"
        placeholder="Precio"
        value={producto.precio}
        onChange={handleChange}
      />
      <button type="submit">Agregar Producto</button>
    </form>
  );
}

export default AgregarProductoForm;