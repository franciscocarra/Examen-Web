<script>
    {% if user.is_authenticated %}
    paypal.Button.render({
        // Configuración de PayPal
        env: 'sandbox',
        client: {
            sandbox: 'AW0VdaPcxSZOqeU6_M23LjBBCUj8XAxL1mGfjf7MnifWYm7uCw5QmfHuP2ed4gIMX5LN5-HPBKVJgRQQ',
            production: 'demo_production_client_id'
        },
        // Estilo del botón (opcional)
        locale: 'en_US',
        style: {
            size: 'small',
            color: 'gold',
            shape: 'pill',
        },
        // Habilitar el flujo de pago instantáneo (opcional)
        commit: true,
        // Configurar el pago
        payment: function (data, actions) {
            return actions.payment.create({
                transactions: [{
                    amount: {
                        total: '1.57',
                        currency: 'USD'
                    }
                }]
            });
        },
        // Ejecutar el pago
        onAuthorize: function (data, actions) {
            return actions.payment.execute().then(function () {
                window.alert('¡Gracias por tu compra!');
            });
        }
    }, '#paypal-button-1-sub');
    {% else %}
    // Redirigir a la página de inicio de sesión si el usuario no está autenticado
    window.location.href = "{% url 'login' %}";
    {% endif %}
</script>

<script>
    {% if user.is_authenticated %}
    paypal.Button.render({
        // Configuración de PayPal
        env: 'sandbox',
        client: {
            sandbox: 'AW0VdaPcxSZOqeU6_M23LjBBCUj8XAxL1mGfjf7MnifWYm7uCw5QmfHuP2ed4gIMX5LN5-HPBKVJgRQQ',
            production: 'demo_production_client_id'
        },
        // Estilo del botón (opcional)
        locale: 'en_US',
        style: {
            size: 'small',
            color: 'gold',
            shape: 'pill',
        },
        // Habilitar el flujo de pago instantáneo (opcional)
        commit: true,
        // Configurar el pago
        payment: function (data, actions) {
            return actions.payment.create({
                transactions: [{
                    amount: {
                        total: '2.63',
                        currency: 'USD'
                    }
                }]
            });
        },
        // Ejecutar el pago
        onAuthorize: function (data, actions) {
            return actions.payment.execute().then(function () {
                window.alert('¡Gracias por tu compra!');
            });
        }
    }, '#paypal-button-2-sub');
    {% else %}
    // Redirigir a la página de inicio de sesión si el usuario no está autenticado
    window.location.href = "{% url 'login' %}";
    {% endif %}
</script>

<script>
    {% if user.is_authenticated %}
    paypal.Button.render({
        // Configuración de PayPal
        env: 'sandbox',
        client: {
            sandbox: 'AW0VdaPcxSZOqeU6_M23LjBBCUj8XAxL1mGfjf7MnifWYm7uCw5QmfHuP2ed4gIMX5LN5-HPBKVJgRQQ',
            production: 'demo_production_client_id'
        },
        // Estilo del botón (opcional)
        locale: 'en_US',
        style: {
            size: 'small',
            color: 'gold',
            shape: 'pill',
        },
        // Habilitar el flujo de pago instantáneo (opcional)
        commit: true,
        // Configurar el pago
        payment: function (data, actions) {
            return actions.payment.create({
                transactions: [{
                    amount: {
                        total: '12.93',
                        currency: 'USD'
                    }
                }]
            });
        },
        // Ejecutar el pago
        onAuthorize: function (data, actions) {
            return actions.payment.execute().then(function () {
                window.alert('¡Gracias por tu compra!');
            });
        }
    }, '#paypal-button-3-sub');
    {% else %}
    // Redirigir a la página de inicio de sesión si el usuario no está autenticado
    window.location.href = "{% url 'login' %}";
    {% endif %}
</script>