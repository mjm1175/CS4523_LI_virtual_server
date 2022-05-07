// this is executed once when the page loads
$(document).ready(function() {
    //console.log("ANYTHING");
    //$('#upload-resume-direct').hide()
    //$('#upload-cover-direct').hide()

    // set things up so my function will be called when field_three changes
    $('#prof-resume').change(function() {
        valueSelected = document.querySelector('input[name="use_profile_resume"]:checked').value;
        if (valueSelected == 'No') {
            $('#upload-resume-direct').show();
        } else if (valueSelected == 'Yes') {
            $('#upload-resume-direct').hide();
        }
    });
    // set things up so my function will be called when field_three changes
    $('#prof-cover').change(function() {
        valueSelected = document.querySelector('input[name="use_profile_cover_letter"]:checked').value;
        if (valueSelected == 'No') {
            $('#upload-cover-direct').show();
        } else if (valueSelected == 'Yes') {
            $('#upload-cover-direct').hide();
        }
    });    
});
