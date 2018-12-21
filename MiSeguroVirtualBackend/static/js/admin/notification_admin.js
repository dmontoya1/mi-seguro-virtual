(function($) {
    $(document).ready(function(){
        $('#notification_form').on('submit', function(event) {
            event.preventDefault();
            form = $(this);
            if ($('#id_user').val() == ""){
                var c = confirm("Vas a enviar esta notificación a todos los usuarios. Deseas Continuar?");
                if (c == true){
                    form.off();
                    form.submit();
                }
            }
            else{
                var c = confirm("Vas a enviar esta notificación a solo un usuario. Deseas Continuar?");
                if (c == true){
                    form.off();
                    form.submit();
                }
            }} 
        );
    });
})(django.jQuery);