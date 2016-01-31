//active class on navbar depending on url
$(document).ready(function($){
	var path = window.location.pathname;
	var target = $('nav a[href="'+path+'"]');
	target.parent().addClass('active');
});

//http://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
//read preview image
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#preview_image').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
$("#id_image").change(function(){
    readURL(this);
});
