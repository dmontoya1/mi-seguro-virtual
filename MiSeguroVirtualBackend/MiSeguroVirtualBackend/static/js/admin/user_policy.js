(function($) {
    $(document).ready(function(){
        $('.field-police_number').addClass('hidden');
        $('.field-taker_name').addClass('hidden');
        $('.field-taker_document').addClass('hidden');
        $('.field-insurance_file').addClass('hidden');
        $('.field-licensed_plate').addClass('hidden');


        $('#id_insurance').on('change', function(){
            if ($(this).val() === '5')
            {
                $('.field-police_number').addClass('hidden');
                $('.field-taker_name').addClass('hidden');
                $('.field-taker_document').addClass('hidden');
                $('.field-insurance_file').removeClass('hidden');
                $('.field-licensed_plate').removeClass('hidden');
            }
            else{
                $('.field-police_number').removeClass('hidden');
                $('.field-taker_name').removeClass('hidden');
                $('.field-taker_document').removeClass('hidden');
                $('.field-insurance_file').addClass('hidden');
                $('.field-licensed_plate').addClass('hidden');
            }
        })
    });
})(django.jQuery);
