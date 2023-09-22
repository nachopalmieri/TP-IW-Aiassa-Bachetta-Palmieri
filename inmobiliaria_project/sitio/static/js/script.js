  // Función para limpiar el placeholder cuando el usuario hace clic en el campo
  function clearPlaceholder(element) {
    element.placeholder = '';
  }
  // Función para mostrar u ocultar los campos de precio y cambiar el texto del botón
  function applyPriceFilter() {
    var precioContainer = document.getElementById('precio-options');

    if (precioContainer.style.display === 'none') {
      precioContainer.style.display = 'block';
    } else {
      precioContainer.style.display = 'none';
    }
  }

  function toggleAmbDormFilter() {
    var ambDormOptions = document.getElementById('amb-dorm-options');
    if (ambDormOptions.style.display === 'none') {
      ambDormOptions.style.display = 'block';
    } else {
      ambDormOptions.style.display = 'none';
    }
  }

  
  