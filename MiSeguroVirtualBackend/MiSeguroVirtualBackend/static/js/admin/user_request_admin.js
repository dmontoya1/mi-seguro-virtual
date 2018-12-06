(function($) {
    $(document).ready(function(){
        console.log('ready')
        if ($('.field-insurance p').text() === 'SOAT (Obligatorios)Seguro'){
            $('.field-police_number').addClass('hidden');
            $('.field-taker_name').addClass('hidden');
            $('.field-taker_document').addClass('hidden');
        }
        else{
            $('.field-insurance_file').addClass('hidden');
            $('.field-licensed_plate').addClass('hidden');
        }
    });
})(django.jQuery);