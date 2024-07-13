function validateForm() {
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const errorMessage = document.getElementById('error-message');

    // Simulando la validación del usuario
    const userExists = false; // Aquí puedes agregar la lógica para verificar si el usuario existe.

    if (!userExists) {
        // Mostrar mensaje de error
        errorMessage.style.display = 'block';

        // Añadir clases de error a los campos de entrada
        email.classList.add('is-invalid');
        password.classList.add('is-invalid');
        
        return false;
    }

    return true;
}