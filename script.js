$(document).ready(function(){

    console.log('Ready')

 // Fetch the current date and update it in the DOM
$(document).ready(function() {
    var currentDate = new Date();
    $('#date-display').text(currentDate.toLocaleDateString());
    
    // Handle the button click event to send the review to the server
    $('#analyze-button').click(function() {
        var reviewText = $('#review-text').val();
        
        // Ajax request
        $.ajax({
            type: 'POST',
            url: '/analyze',  // The URL to send the request to
            contentType: 'application/json',
            data: JSON.stringify({ 'customer_review': reviewText }),
            success: function(result) {
                // Extract sentiment and emoticon URL from the result
                var sentiment = result.sentiment;
                var emoticonPath = result.emoticon_path;

                // Update the DOM elements
                $('#sentiment-display').text(sentiment);
                $('#emoticon-image').attr('src', emoticonPath);

                // Show them
                $('#result-section').show();
            },

            //  if any error, run this function
            error : function(result){

                console.log(result)
            }
        })


        //  clearing the textbox after every button push
        $('#text').val("")
    })
        
})